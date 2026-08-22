#!/usr/bin/env python3
"""Build MANIFEST.json and llms.txt from the document frontmatter.

Mechanical, so code does it rather than an agent. Re-run after any doc change;
verify_kb.py fails if the manifest and the tree disagree in either direction.
"""
import hashlib, json, os, re, sys

KB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(KB, "docs")

ERA_LABEL = {
    "jreport-v15-v16":     "JReport era (v15-v16, product named Logi JReport)",
    "logi-report-v17-v19": "Logi Report era (v17-v19, after the v17 rename)",
    "unversioned":         "Version not stated by the source; era unknown",
    "current":             "Current era (v23-v26)",
}

FM = re.compile(r"^---\n(.*?)\n---\n", re.S)


def parse_frontmatter(path):
    head = open(path, encoding="utf-8", errors="replace").read(4000)
    m = FM.match(head)
    if not m:
        return None
    out = {}
    for line in m.group(1).split("\n"):
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        out[k.strip()] = v.strip().strip('"')
    return out


def main():
    # Walk to arbitrary depth. docs/<era>/<section>/ is two deep but
    # docs/current/<line>/<section>/ is three, and indexing only two levels
    # silently omitted every current document. The gate caught it; do not
    # reintroduce a fixed depth here.
    entries = []
    for root, _, files in os.walk(DOCS):
        for name in sorted(files):
            if not name.endswith(".md"):
                continue
            full = os.path.join(root, name)
            rel = os.path.relpath(full, KB)
            parts = rel.split(os.sep)
            era = parts[1] if len(parts) > 1 else "unversioned"
            section = parts[-2] if len(parts) > 2 else era
            fm = parse_frontmatter(full)
            if fm is None:
                print("NO FRONTMATTER: %s" % rel, file=sys.stderr)
                fm = {}
            body = ""
            try:
                raw = open(full, encoding="utf-8", errors="replace").read()
                mm = FM.match(raw)
                body = raw[mm.end():] if mm else raw
            except Exception:
                pass
            body = body.strip()
            entries.append({
                "path": rel,
                "body_sha1": hashlib.sha1(body.encode("utf-8")).hexdigest() if body else "",
                "body_chars": len(body),
                # The unversioned bucket is not one era: it mixes pre- and
                # post-rename articles. Flagging the pre-rename naming lets a
                # consumer see that without the run guessing an era the source
                # never states.
                "uses_jreport_naming": "Logi JReport" in body,
                "title": fm.get("title", ""),
                "id": fm.get("id", ""),
                "section": fm.get("section", section),
                "product": fm.get("category", "Logi Report"),
                "era": era,
                "era_label": ERA_LABEL.get(era, era),
                "source_url": fm.get("url", ""),
                "updated_at": fm.get("updated_at", ""),
                "source_host": fm.get("source_host", "devnet.logianalytics.com"),
            })
    entries.sort(key=lambda e: e["path"])

    # Upstream publishes the same article under several Zendesk ids, both across
    # Designer/Server and across versions. Roughly 9% of the corpus is a
    # byte-identical copy of another document. Do NOT delete these: a v25 and a
    # v26 article being identical is itself the useful fact that the topic did
    # not change. Instead declare the duplication so a consumer can collapse it
    # at query time without losing data.
    groups = {}
    for e in entries:
        if e["body_sha1"] and e["body_chars"] > 200:
            groups.setdefault(e["body_sha1"], []).append(e["path"])
    dup = {k: v for k, v in groups.items() if len(v) > 1}
    canonical = {}
    for sha, paths in dup.items():
        # prefer the newest era as canonical, then the shortest path
        rank = {"current": 0, "logi-report-v17-v19": 1, "unversioned": 2,
                "jreport-v15-v16": 3}
        best = sorted(paths, key=lambda p: (rank.get(p.split(os.sep)[1], 9), len(p), p))[0]
        for p2 in paths:
            canonical[p2] = best
    for e in entries:
        c = canonical.get(e["path"])
        e["duplicate_group"] = e["body_sha1"] if c else ""
        e["is_canonical"] = (c == e["path"]) if c else True

    n_dup_docs = sum(1 for e in entries if e["duplicate_group"])
    n_redundant = n_dup_docs - len({e["duplicate_group"] for e in entries
                                    if e["duplicate_group"]})
    manifest = {
        "name": "logi-report-kb",
        "description": "Logi Report documentation and API knowledge base",
        "document_count": len(entries),
        "duplication": {
            "documents_in_a_duplicate_group": n_dup_docs,
            "redundant_copies": n_redundant,
            "note": "Upstream publishes the same article under multiple Zendesk "
                    "ids, across Designer/Server and across versions. Nothing is "
                    "deleted: two identical articles in different versions are "
                    "evidence the topic did not change. Filter on is_canonical "
                    "to collapse duplicates at query time.",
        },
        "eras": {e: sum(1 for x in entries if x["era"] == e)
                 for e in sorted({x["era"] for x in entries})},
        "documents": entries,
    }
    with open(os.path.join(KB, "MANIFEST.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=1, ensure_ascii=False)

    lines = ["# Logi Report knowledge base", "",
             "> Documentation and API reference for Logi Report, formerly JReport.",
             "> %d documents. See CLAUDE.md for how to use this repo." % len(entries), ""]
    for era in sorted({x["era"] for x in entries}):
        lines.append("## %s" % ERA_LABEL.get(era, era))
        lines.append("")
        cur = None
        for e in [x for x in entries if x["era"] == era]:
            if e["section"] != cur:
                cur = e["section"]
                lines.append("### %s" % cur)
            lines.append("- [%s](%s)" % (e["title"] or os.path.basename(e["path"]), e["path"]))
        lines.append("")
    open(os.path.join(KB, "llms.txt"), "w", encoding="utf-8").write("\n".join(lines) + "\n")

    print("MANIFEST.json: %d documents" % len(entries))
    for k, v in manifest["eras"].items():
        print("  %-22s %d" % (k, v))


if __name__ == "__main__":
    main()
