#!/usr/bin/env python3
"""Gate for logi-report-kb. Exit 0 only if every named check RAN and PASSED.

A skip is not a pass. A traceback is not a pass. Named checks are tracked
against a blessed manifest so a deleted check cannot hide behind an added one.
"""
import hashlib, json, os, re, sys, collections

KB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(KB, "docs")

# Minimum number of checks this gate must run. Pinned separately from the list
# below so that deleting an entry AND its call, which an adversarial review used
# to turn RED into GREEN with exit 0, trips this instead.
#
# Honest limit, stated rather than hidden: a gate living in a repo that the
# people it judges can edit cannot fully defend itself. Someone who also edits
# this number defeats it. What this buys is that casual or partial removal is
# loud. The real defence is reviewing the diff of THIS FILE at every merge and
# counting deletions. Never lower MIN_CHECKS to make a run green.
MIN_CHECKS = 13

CHECK_MANIFEST = [
    "kb_structure_present",
    "frontmatter_valid",
    "manifest_matches_disk",
    "no_orphan_files",
    "llms_txt_resolves",
    "api_docs_trace_to_source",
    "internal_links_resolve",
    "no_composer_confusion",
    "era_labelled",
    "retrieval_smoke_test",
    "retrieval_current_era",
    "duplication_declared",
    "demo_layer_present",
]

REQUIRED_PATHS = [
    "README.md", "CLAUDE.md", "ORIENTATION.md", "MANIFEST.json", "llms.txt",
    "docs", "api", "api/README.md", "building-reports", "scripts",
    "scripts/build_index.py", "scripts/verify_kb.py",
]

# The questions this repo exists to answer.
#
# An adversarial review defeated the previous version of this check with twelve
# files of lorem ipsum. Three reasons, all fixed below:
#   1. it searched frontmatter as well as body, so the `url:` line every document
#      carries satisfied the "URL invocation" question;
#   2. it matched unanchored substrings, so "A flowchart on the toolbar" answered
#      "charts in a report" via bar in toolbar;
#   3. it stopped at the first hit and never required ten questions to be answered
#      by ten DIFFERENT documents, so one keyword-soup file answered all ten.
#
# Now: body text only, whole-word matching, the answering document's TITLE must
# be on topic, and every question must be answered by a distinct document.
#
# (label, title_terms, body_terms_all, body_terms_any)
SMOKE = [
    ("what a catalog is",            ["catalog"],       ["catalog"],      ["business view", "data source", "connection"]),
    ("creating a crosstab report",   ["crosstab"],      ["crosstab"],     ["column", "row", "aggregate"]),
    ("charts in a report",           ["chart"],         ["chart"],        ["legend", "axis", "series"]),
    ("scheduling a report task",     ["schedule"],      ["schedule"],     ["task", "trigger", "report"]),
    ("exporting to PDF",             ["export", "pdf"], ["export", "pdf"], ["page", "format"]),
    ("page report vs web report",    ["page report"],   ["page report"],  ["web report", "studio"]),
    ("the Server API",               ["server api"],    ["server api"],   ["jet", "class", "java"]),
    ("URL invocation of the server", ["url"],           ["url"],          ["jrs", "parameter", "server"]),
    ("report security",              ["security"],      ["security"],     ["role", "privilege", "permission"]),
    ("business views",               ["business view"], ["business view"], ["catalog", "element"]),
]

FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)

# Normalisation used before hashing a body to detect duplication.
# An adversarial review defeated the duplication check by appending an HTML
# comment, which renders as nothing, to each of 2,391 documents: the declared
# count honestly went to zero and the gate honestly verified zero, while the
# corpus still held 1,226 redundant copies. Strip anything invisible first, so
# a normalisation pass or a per-file id stamp cannot silently erase the finding.
_COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
_WS_RE = re.compile(r"\s+")


def normalise_body(body):
    b = _COMMENT_RE.sub(" ", body or "")
    return _WS_RE.sub(" ", b).strip().lower()



def split_doc(path):
    """Return (title_lower, body_lower) with frontmatter REMOVED from the body.
    Indexing frontmatter is how the previous check was fooled: every document
    carries a url: line and a category: "Logi Report" line."""
    try:
        raw = open(path, encoding="utf-8", errors="replace").read()
    except Exception:
        return "", ""
    m = FM_RE.match(raw)
    title = ""
    if m:
        for line in m.group(1).split("\n"):
            if line.startswith("title:"):
                title = line.split(":", 1)[1].strip().strip('"')
        body = raw[m.end():]
    else:
        body = raw
    return title.lower(), body.lower()


def has_word(hay, needle):
    """Whole-word (or whole-phrase) containment. 'bar' must not match 'toolbar'."""
    return re.search(r"(?<![a-z0-9])" + re.escape(needle) + r"(?![a-z0-9])", hay) is not None

results, failures = {}, []


def record(name, passed, detail=""):
    results[name] = (passed, detail)
    if not passed:
        failures.append("FAIL  %s: %s" % (name, detail))


def load_manifest():
    p = os.path.join(KB, "MANIFEST.json")
    if not os.path.exists(p):
        return None
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return None


def doc_paths():
    out = []
    for root, _, files in os.walk(DOCS):
        for f in files:
            if f.endswith(".md"):
                out.append(os.path.relpath(os.path.join(root, f), KB))
    return sorted(out)


def check_structure():
    missing = [p for p in REQUIRED_PATHS if not os.path.exists(os.path.join(KB, p))]
    record("kb_structure_present", not missing,
           "missing: %s" % missing if missing else "%d required paths present" % len(REQUIRED_PATHS))


def check_frontmatter(disk):
    fm = re.compile(r"^---\n(.*?)\n---\n", re.S)
    bad = []
    for rel in disk:
        head = open(os.path.join(KB, rel), encoding="utf-8", errors="replace").read(4000)
        m = fm.match(head)
        if not m:
            bad.append("%s: no frontmatter" % rel)
            continue
        kv = {}
        for l in m.group(1).split("\n"):
            if ":" in l:
                k, _, v = l.partition(":")
                kv[k.strip()] = v.strip().strip('"')
        missing = [r for r in ("title", "id", "section", "url") if not kv.get(r)]
        if missing:
            bad.append("%s: missing or EMPTY %s" % (rel, missing))
            continue
        # A document with frontmatter and no body is not a document.
        body = head[m.end():]
        if len(body.strip()) < 20:
            bad.append("%s: frontmatter but effectively no body" % rel)
    record("frontmatter_valid", not bad,
           "%d bad: %s" % (len(bad), bad[:4]) if bad
           else "%d docs have non-empty title/id/section/url and a body" % len(disk))


def check_manifest(man, disk):
    if man is None:
        record("manifest_matches_disk", False, "MANIFEST.json missing or unparseable")
        record("no_orphan_files", False, "cannot check without a manifest")
        return
    listed = sorted(d["path"] for d in man.get("documents", []))
    dset, lset = set(disk), set(listed)
    missing = sorted(lset - dset)     # manifest names a file that is not there
    orphan = sorted(dset - lset)      # file on disk that the manifest never names
    # An adversarial review rewrote every field except `path` and the gate did
    # not notice: era collapsed to "current" on all 13,235 docs, titles
    # fabricated, source_url pointed at evil.example.com, is_canonical set true
    # on all 1,226 duplicates. Verify the fields against disk, not just the path.
    problems = list(missing[:3])
    if man.get("document_count") != len(listed):
        problems.append("count field %s vs %d entries"
                        % (man.get("document_count"), len(listed)))
    fm_re = re.compile(r"^---\n(.*?)\n---\n", re.S)
    checked = mismatched = 0
    for d in man.get("documents", []):
        rel = d.get("path", "")
        full = os.path.join(KB, rel)
        if not os.path.isfile(full):
            continue
        checked += 1
        # era must be derivable from the path, not asserted
        parts = rel.split(os.sep)
        path_era = parts[1] if len(parts) > 1 else ""
        if d.get("era") != path_era:
            mismatched += 1
            if len(problems) < 6:
                problems.append("%s: era %r but path says %r"
                                % (rel, d.get("era"), path_era))
            continue
        raw = open(full, encoding="utf-8", errors="replace").read()
        m = fm_re.match(raw)
        if not m:
            continue
        fm_title = ""
        fm_url = ""
        for line in m.group(1).split("\n"):
            if line.startswith("title:"):
                fm_title = line.split(":", 1)[1].strip().strip('"')
            elif line.startswith("url:"):
                fm_url = line.split(":", 1)[1].strip()
        if d.get("title") != fm_title:
            mismatched += 1
            if len(problems) < 6:
                problems.append("%s: manifest title %r != frontmatter %r"
                                % (rel, str(d.get("title"))[:30], fm_title[:30]))
            continue
        if d.get("source_url") != fm_url:
            mismatched += 1
            if len(problems) < 6:
                problems.append("%s: manifest source_url does not match the document"
                                % rel)
            continue
        body = raw[m.end():].strip()
        nb = normalise_body(body)
        if d.get("body_sha1") != (hashlib.sha1(nb.encode("utf-8")).hexdigest()
                                  if nb else ""):
            mismatched += 1
            if len(problems) < 6:
                problems.append("%s: body_sha1 does not match the file" % rel)
    record("manifest_matches_disk", not problems,
           "%d problems: %s" % (len(missing) + mismatched, problems[:6]) if problems
           else "%d entries; path, era, title, source_url and body_sha1 all verified "
                "against disk for %d" % (len(listed), checked))
    record("no_orphan_files", not orphan,
           "%d docs on disk absent from manifest: %s" % (len(orphan), orphan[:3])
           if orphan else "no orphans")


def check_llms(disk):
    """llms.txt is the navigation index an agent reads to find anything.

    The previous version was one-directional: every link it named had to
    resolve, but nothing required it to name any. An adversarial review replaced
    the whole 13,643-line index with three lines listing zero documents and the
    check reported a pass. It must cover the corpus, not merely avoid lying
    about the part it mentions."""
    p = os.path.join(KB, "llms.txt")
    if not os.path.exists(p):
        record("llms_txt_resolves", False, "llms.txt missing")
        return
    text = open(p, encoding="utf-8").read()
    linked = set(re.findall(r"\]\((docs/[^)]+)\)", text))
    dead = sorted(l for l in linked if not os.path.exists(os.path.join(KB, l)))
    uncovered = len(set(disk) - linked)
    problems = []
    if dead:
        problems.append("%d dead links: %s" % (len(dead), dead[:3]))
    if uncovered:
        problems.append("%d of %d documents are not listed in llms.txt"
                        % (uncovered, len(disk)))
    record("llms_txt_resolves", not problems,
           "; ".join(problems) if problems
           else "indexes all %d documents, every link resolves" % len(linked))


def check_api_sources():
    apidir = os.path.join(KB, "api")
    if not os.path.isdir(apidir):
        record("api_docs_trace_to_source", False, "api/ missing")
        return
    files = [f for f in os.listdir(apidir) if f.endswith(".md")]
    if not files:
        record("api_docs_trace_to_source", False, "api/ contains no markdown")
        return
    bad = []
    for f in files:
        body = open(os.path.join(apidir, f), encoding="utf-8").read()
        cited = re.findall(r"\((\.\./docs/[^)]+\.md)\)", body)
        resolved = [c for c in cited
                    if os.path.exists(os.path.normpath(os.path.join(apidir, c)))]
        if not resolved:
            bad.append("%s: cites no resolvable source doc" % f)
        else:
            for c in cited:
                if not os.path.exists(os.path.normpath(os.path.join(apidir, c))):
                    bad.append("%s: dead source link %s" % (f, c))
    record("api_docs_trace_to_source", not bad,
           "%d problems: %s" % (len(bad), bad[:4]) if bad
           else "%d api docs each cite a resolvable source" % len(files))


def check_internal_links():
    dead = []
    for name in ("README.md", "CLAUDE.md", "ORIENTATION.md", "api/README.md"):
        p = os.path.join(KB, name)
        if not os.path.exists(p):
            continue
        base = os.path.dirname(p)
        for m in re.finditer(r"\]\((?!https?://|#)([^)]+)\)", open(p, encoding="utf-8").read()):
            t = m.group(1).split("#")[0]
            if t and not os.path.exists(os.path.normpath(os.path.join(base, t))):
                dead.append("%s -> %s" % (name, t))
    for root, _, files in os.walk(os.path.join(KB, "building-reports")):
        for f in files:
            if not f.endswith(".md"):
                continue
            p = os.path.join(root, f)
            for m in re.finditer(r"\]\((?!https?://|#)([^)]+)\)", open(p, encoding="utf-8").read()):
                t = m.group(1).split("#")[0]
                if t and not os.path.exists(os.path.normpath(os.path.join(root, t))):
                    dead.append("building-reports/%s -> %s" % (f, t))
    record("internal_links_resolve", not dead,
           "%d dead: %s" % (len(dead), dead[:5]) if dead else "all relative links resolve")


def _authored_files():
    """Every file a human or agent wrote in this repo. The previous version read
    five paths out of 13,250 and an adversarial review put a conflation into
    api/server-api.md unnoticed."""
    out = []
    for f in sorted(os.listdir(KB)):
        if f.endswith(".md"):
            out.append(f)
    for sub in ("api", "building-reports"):
        d = os.path.join(KB, sub)
        if os.path.isdir(d):
            for root, _, files in os.walk(d):
                for f in sorted(files):
                    if f.endswith(".md"):
                        out.append(os.path.relpath(os.path.join(root, f), KB))
    return out


# Words that, in a sentence naming BOTH products, assert they are one thing.
EQUIV = re.compile(
    r"(same|identical|interchangeab|synonym|equivalent|renamed|new name|"
    r"formerly|now called|also called|aka|rebrand|two brands|either doc|"
    r"one product|the same product|is simply|is just|ships as|sold as|"
    r"\bis\b|\bwas\b|\bare\b|\bbecame\b|"
    # parenthetical rename: "Logi Report (now Logi Composer)"
    r"\((?:now|formerly|previously|a\.?k\.?a\.?|renamed)\b)", re.I)
SPLIT = re.compile(r"(?<=[.!?;:])\s+|\n")


def check_composer_confusion():
    """Logi Report and Logi Composer are separate products sharing no
    documentation surface. Conflating them caused a real mislabelling on a
    recorded sales call.

    The previous version grepped five fixed phrasings in five files. An
    adversarial review slipped 11 of 14 natural conflations past it. This works
    the other way round: find any SENTENCE naming both products, and require it
    to be explicitly contrastive. That is a broad net, so contrastive sentences
    are whitelisted rather than conflations being blacklisted."""
    CONTRAST = re.compile(
        r"(separate|different|not the same|distinct|unlike|whereas|while|"
        r"never|no shared|nothing here applies|does not apply|instead of|"
        r"rather than|confus|mislabel|conflat|versus|\bvs\b|two products|"
        r"another product|other product|do not|don't|neither)", re.I)
    hits = []
    for rel in _authored_files():
        p = os.path.join(KB, rel)
        try:
            text = open(p, encoding="utf-8").read()
        except Exception:
            continue
        in_code = False
        for n, raw_line in enumerate(text.split("\n"), 1):
            if raw_line.strip().startswith("```"):
                in_code = not in_code
                continue
            if in_code:
                continue
            for sent in SPLIT.split(raw_line):
                has_r = re.search(r"Logi Report", sent) is not None
                has_c = re.search(r"Logi Composer", sent) is not None
                if not (has_r and has_c):
                    continue
                if CONTRAST.search(sent):
                    continue
                if EQUIV.search(sent):
                    hits.append("%s:%d %r" % (rel, n, sent.strip()[:90]))
    record("no_composer_confusion", not hits,
           "%d sentences equate the two products without contrast: %s"
           % (len(hits), hits[:4]) if hits
           else "%d authored files scanned; no sentence equates the products"
                % len(_authored_files()))


def check_era(man):
    if man is None:
        record("era_labelled", False, "no manifest")
        return
    allowed = {"jreport-v15-v16", "logi-report-v17-v19", "unversioned", "current"}
    bad = [d["path"] for d in man.get("documents", [])
           if d.get("era") not in allowed or not d.get("era_label")]
    record("era_labelled", not bad,
           "%d docs with no/unknown era: %s" % (len(bad), bad[:3]) if bad
           else "every doc carries one of %d era labels" % len(allowed))


def _answer(index, q, used):
    """Find a document that genuinely answers q and has not already been used
    for another question."""
    label, title_terms, all_terms, any_terms = q
    for rel, title, body in index:
        if rel in used:
            continue
        if not all(has_word(title, t) or has_word(title, t + "s")
                   or has_word(title, t.rstrip("e") + "ing")
                   for t in title_terms):
            continue
        if not all(has_word(body, t) for t in all_terms):
            continue
        if not any(has_word(body, t) for t in any_terms):
            continue
        if len(body.strip()) < 400:
            continue
        return rel
    return None


def _run_smoke(index, name, scope_desc):
    used, unanswered, answers = set(), [], {}
    for q in SMOKE:
        hit = _answer(index, q, used)
        if hit:
            used.add(hit)
            answers[q[0]] = hit
        else:
            unanswered.append(q[0])
    record(name, not unanswered,
           "%d of %d unanswerable from %s: %s"
           % (len(unanswered), len(SMOKE), scope_desc, unanswered) if unanswered
           else "all %d questions answered by %d DISTINCT on-topic documents in %s"
                % (len(SMOKE), len(used), scope_desc))


def check_smoke(disk):
    """Can this repo answer the questions it exists to answer? Body text only,
    whole-word matching, the document's title must be on topic, the body must be
    substantive, and each question must be answered by a DIFFERENT document."""
    index = [(rel,) + split_doc(os.path.join(KB, rel)) for rel in disk]
    _run_smoke(index, "retrieval_smoke_test", "the corpus")


def check_smoke_current(disk):
    """Same, restricted to docs/current. The corpus skews old (9,344 of 13,235
    articles describe v15-v19), so a KB used for demos must not silently fall
    back on decade-old guidance."""
    cur = [r for r in disk if r.startswith(os.path.join("docs", "current"))]
    if not cur:
        record("retrieval_current_era", False,
               "docs/current is empty; run scripts/pull_docs.py")
        return
    index = [(rel,) + split_doc(os.path.join(KB, rel)) for rel in cur]
    _run_smoke(index, "retrieval_current_era", "docs/current (%d docs)" % len(cur))


def check_duplication(man, disk):
    """Roughly 9% of this corpus is a byte-identical copy of another document,
    because upstream publishes the same article under several Zendesk ids. That
    is not a defect to delete: two identical articles in different versions are
    evidence the topic did not change. What IS a defect is failing to declare
    it, because a consumer would then treat 13,235 as 13,235 distinct documents.
    This check recomputes the duplication and fails if the manifest understates
    it."""
    if man is None:
        record("duplication_declared", False, "no manifest")
        return
    decl = man.get("duplication")
    if not decl:
        record("duplication_declared", False,
               "manifest does not declare duplication at all")
        return
    fm = re.compile(r"^---\n(.*?)\n---\n", re.S)
    groups = collections.defaultdict(int)
    for rel in disk:
        raw = open(os.path.join(KB, rel), encoding="utf-8", errors="replace").read()
        m = fm.match(raw)
        body = normalise_body(raw[m.end():] if m else raw)
        if len(body) > 200:
            groups[hashlib.sha1(body.encode("utf-8")).hexdigest()] += 1
    actual_redundant = sum(n - 1 for n in groups.values() if n > 1)
    stated = decl.get("redundant_copies", -1)
    ok = stated == actual_redundant
    record("duplication_declared", ok,
           "manifest states %s redundant copies, recount finds %d"
           % (stated, actual_redundant) if not ok
           else "%d redundant copies declared and verified" % actual_redundant)


def check_demo_layer():
    """The task-oriented layer is the reason this repo exists.

    An adversarial review satisfied the previous version with three files of 401
    bytes of lorem ipsum, taking the real repo from RED to GREEN in thirty
    seconds. Byte count is not a proxy for substance. A guide now has to look
    like a guide: cite source documents that resolve, and talk about the actual
    product."""
    d = os.path.join(KB, "building-reports")
    if not os.path.isdir(d):
        record("demo_layer_present", False, "building-reports/ missing")
        return
    mds = sorted(f for f in os.listdir(d) if f.endswith(".md"))
    if "README.md" not in mds:
        record("demo_layer_present", False,
               "building-reports/README.md missing (%d other md files)" % len(mds))
        return
    TERMS = ("catalog", "report", "designer", "server", "dataset",
             "business view", "chart", "crosstab", "studio")
    good, why = [], []
    for f in mds:
        body = open(os.path.join(d, f), encoding="utf-8").read()
        low = body.lower()
        # must cite at least one source document, and it must resolve
        cites = re.findall(r"\]\((\.\./docs/[^)]+\.md)\)", body)
        live = [c for c in cites
                if os.path.exists(os.path.normpath(os.path.join(d, c)))]
        terms = sum(1 for t in TERMS if t in low)
        if len(body) > 1200 and live and terms >= 3:
            good.append(f)
        else:
            why.append("%s(chars=%d,cites=%d,terms=%d)"
                       % (f, len(body), len(live), terms))
    if len(good) < 5:
        record("demo_layer_present", False,
               "only %d of %d guides are substantive (need >1200 chars, a "
               "resolving ../docs source citation, and 3+ product terms); "
               "weak: %s" % (len(good), len(mds), why[:5]))
        return
    record("demo_layer_present", True,
           "%d guides, %d substantive and citing resolving sources"
           % (len(mds), len(good)))


def main():
    man = load_manifest()
    disk = doc_paths()
    check_structure()
    check_frontmatter(disk)
    check_manifest(man, disk)
    check_llms(disk)
    check_api_sources()
    check_internal_links()
    check_composer_confusion()
    check_era(man)
    check_smoke(disk)
    check_smoke_current(disk)
    check_duplication(man, disk)
    check_demo_layer()

    print("=" * 70)
    print("LOGI REPORT KB GATE   (%d documents on disk)" % len(disk))
    print("=" * 70)
    for name in CHECK_MANIFEST:
        if name not in results:
            print("  SKIPPED  %-30s <- NOT A PASS" % name)
            continue
        ok, detail = results[name]
        print("  %-8s %-30s %s" % ("PASS" if ok else "FAIL", name, detail[:80]))
    skipped = [n for n in CHECK_MANIFEST if n not in results]
    unexpected = [n for n in results if n not in CHECK_MANIFEST]

    # Self-scope defences, against a fleet editing the gate to reach green.
    scope_errors = []
    if len(CHECK_MANIFEST) < MIN_CHECKS:
        scope_errors.append("CHECK_MANIFEST has %d entries, below the pinned "
                            "minimum of %d: a check was deleted"
                            % (len(CHECK_MANIFEST), MIN_CHECKS))
    if len(set(CHECK_MANIFEST)) != len(CHECK_MANIFEST):
        scope_errors.append("CHECK_MANIFEST contains duplicates, inflating its count")
    # Every check_* function defined in this file must be represented and must
    # be called from main(). Deleting a call without deleting the function is
    # caught by the skipped list; deleting both is caught here.
    try:
        src = open(os.path.abspath(__file__), encoding="utf-8").read()
        defined = set(re.findall(r"^def (check_[a-z_]+)\(", src, re.M))
        called = set(re.findall(r"^    (check_[a-z_]+)\(", src, re.M))
        orphan_defs = sorted(defined - called)
        if orphan_defs:
            scope_errors.append("check functions defined but never called: %s"
                                % orphan_defs)
    except Exception as e:
        scope_errors.append("could not introspect the gate's own source: %s" % e)
    print("-" * 70)
    print("manifest: %d | ran: %d | skipped: %d | unexpected: %d"
          % (len(CHECK_MANIFEST), len(results), len(skipped), len(unexpected)))
    if scope_errors:
        print()
        for e in scope_errors:
            print("  SCOPE  " + e)
        print("GATE: RED  (the gate's own scope was tampered with)"); return 1
    if skipped:
        print("GATE: RED  (%d named checks never ran)" % len(skipped)); return 1
    if unexpected:
        print("GATE: RED  (unblessed checks ran: %s)" % unexpected); return 1
    if failures:
        print()
        for f in failures:
            print("  " + f)
        print("GATE: RED  (%d failed)" % len(failures)); return 1
    print("GATE: GREEN"); return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        import traceback; traceback.print_exc()
        print("GATE: RED  (gate itself raised)"); sys.exit(2)
