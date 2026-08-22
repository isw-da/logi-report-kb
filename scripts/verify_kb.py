#!/usr/bin/env python3
"""Gate for logi-report-kb. Exit 0 only if every named check RAN and PASSED.

A skip is not a pass. A traceback is not a pass. Named checks are tracked
against a blessed manifest so a deleted check cannot hide behind an added one.
"""
import json, os, re, sys, collections

KB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(KB, "docs")

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
]

REQUIRED_PATHS = [
    "README.md", "CLAUDE.md", "ORIENTATION.md", "MANIFEST.json", "llms.txt",
    "docs", "api", "api/README.md", "building-reports", "scripts",
    "scripts/build_index.py", "scripts/verify_kb.py",
]

# The questions this repo exists to answer. Each must be answerable from a file
# that actually contains the terms. Would fail if the content were deleted.
SMOKE = [
    ("what a catalog is",            ["catalog"], ["business view", "data source"]),
    ("creating a crosstab report",   ["crosstab"], ["column", "row"]),
    ("charts in a report",           ["chart"],   ["bar", "legend"]),
    ("scheduling a report task",     ["schedul"], ["task"]),
    ("exporting to PDF",             ["export"],  ["pdf"]),
    ("page report vs web report",    ["page report"], ["web report"]),
    ("the Server API",               ["server api"], ["jet."]),
    ("URL invocation of the server", ["url"], ["jrs.", "report"]),
    ("report security",              ["security"], ["role", "user"]),
    ("business views",               ["business view"], ["catalog"]),
]

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
        keys = {l.partition(":")[0].strip() for l in m.group(1).split("\n") if ":" in l}
        for req in ("title", "id", "section", "url"):
            if req not in keys:
                bad.append("%s: missing %s" % (rel, req))
                break
    record("frontmatter_valid", not bad,
           "%d bad: %s" % (len(bad), bad[:4]) if bad else "%d docs have title/id/section/url" % len(disk))


def check_manifest(man, disk):
    if man is None:
        record("manifest_matches_disk", False, "MANIFEST.json missing or unparseable")
        record("no_orphan_files", False, "cannot check without a manifest")
        return
    listed = sorted(d["path"] for d in man.get("documents", []))
    dset, lset = set(disk), set(listed)
    missing = sorted(lset - dset)     # manifest names a file that is not there
    orphan = sorted(dset - lset)      # file on disk that the manifest never names
    record("manifest_matches_disk", not missing and man.get("document_count") == len(listed),
           "%d manifest entries have no file (%s); count field %s vs %d entries"
           % (len(missing), missing[:3], man.get("document_count"), len(listed))
           if (missing or man.get("document_count") != len(listed))
           else "%d entries, all resolve, count field agrees" % len(listed))
    record("no_orphan_files", not orphan,
           "%d docs on disk absent from manifest: %s" % (len(orphan), orphan[:3])
           if orphan else "no orphans")


def check_llms(disk):
    p = os.path.join(KB, "llms.txt")
    if not os.path.exists(p):
        record("llms_txt_resolves", False, "llms.txt missing")
        return
    dead = []
    for m in re.finditer(r"\]\((docs/[^)]+)\)", open(p, encoding="utf-8").read()):
        if not os.path.exists(os.path.join(KB, m.group(1))):
            dead.append(m.group(1))
    record("llms_txt_resolves", not dead,
           "%d dead links: %s" % (len(dead), dead[:3]) if dead else "all llms.txt paths resolve")


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


def check_composer_confusion():
    """Logi Report and Logi Composer are separate products with no shared doc
    surface. A KB that blurs them reproduces a real mislabelling that has already
    happened in a live deal. Authored files must not equate them."""
    patterns = [
        r"Logi Report,? (?:also |now |formerly )?(?:known as|called|renamed to|is) Logi Composer",
        r"Logi Composer,? (?:also |now |formerly )?(?:known as|called|renamed to|is) Logi Report",
        r"Logi Report (?:and|or) Logi Composer are (?:the same|one product)",
        r"Logi Report (?:was |has been )?(?:renamed|rebranded) (?:to|as) Logi Composer",
    ]
    hits = []
    for name in ("README.md", "CLAUDE.md", "ORIENTATION.md", "api/README.md"):
        p = os.path.join(KB, name)
        if not os.path.exists(p):
            continue
        body = open(p, encoding="utf-8").read()
        for pat in patterns:
            for m in re.finditer(pat, body, re.I):
                hits.append("%s: %r" % (name, m.group(0)[:60]))
    for root, _, files in os.walk(os.path.join(KB, "building-reports")):
        for f in files:
            if not f.endswith(".md"):
                continue
            body = open(os.path.join(root, f), encoding="utf-8").read()
            for pat in patterns:
                for m in re.finditer(pat, body, re.I):
                    hits.append("building-reports/%s: %r" % (f, m.group(0)[:60]))
    record("no_composer_confusion", not hits,
           "%d conflations: %s" % (len(hits), hits[:3]) if hits
           else "no file equates Logi Report with Logi Composer")


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


def check_smoke(disk):
    """The check that tests the real path: can this repo answer the questions it
    exists to answer? Fails if the content were deleted."""
    index = []
    for rel in disk:
        try:
            index.append((rel, open(os.path.join(KB, rel), encoding="utf-8",
                                    errors="replace").read().lower()))
        except Exception:
            pass
    unanswered = []
    for label, must, also in SMOKE:
        hit = None
        for rel, body in index:
            if all(t in body for t in must) and any(t in body for t in also):
                hit = rel
                break
        if not hit:
            unanswered.append(label)
    record("retrieval_smoke_test", not unanswered,
           "%d of %d demo questions unanswerable: %s"
           % (len(unanswered), len(SMOKE), unanswered)
           if unanswered else "all %d demo questions answerable from the corpus" % len(SMOKE))


def check_smoke_current(disk):
    """Stronger than retrieval_smoke_test: the same demo questions must be
    answerable from docs/current alone. The corpus skews old (9,344 of 13,235
    articles describe v15-v19), so a KB used for demos must not silently fall
    back on decade-old guidance. If a refresh breaks the current pull, this is
    the check that notices."""
    cur = [r for r in disk if r.startswith(os.path.join("docs", "current"))]
    if not cur:
        record("retrieval_current_era", False, "docs/current is empty; run scripts/pull_docs.py")
        return
    index = []
    for rel in cur:
        try:
            index.append(open(os.path.join(KB, rel), encoding="utf-8",
                              errors="replace").read().lower())
        except Exception:
            pass
    unanswered = [label for label, must, also in SMOKE
                  if not any(all(t in b for t in must) and any(t in b for t in also)
                             for b in index)]
    record("retrieval_current_era", not unanswered,
           "%d of %d unanswerable from docs/current: %s"
           % (len(unanswered), len(SMOKE), unanswered) if unanswered
           else "all %d demo questions answerable from the %d current-era docs"
                % (len(SMOKE), len(cur)))


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
    print("-" * 70)
    print("manifest: %d | ran: %d | skipped: %d | unexpected: %d"
          % (len(CHECK_MANIFEST), len(results), len(skipped), len(unexpected)))
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
