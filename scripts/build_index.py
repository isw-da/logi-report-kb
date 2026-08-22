#!/usr/bin/env python3
"""Build MANIFEST.json and llms.txt from the document frontmatter.

Mechanical, so code does it rather than an agent. Re-run after any doc change;
verify_kb.py fails if the manifest and the tree disagree in either direction.
"""
import json, os, re, sys

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
    entries = []
    for era in sorted(os.listdir(DOCS)):
        eradir = os.path.join(DOCS, era)
        if not os.path.isdir(eradir):
            continue
        for section in sorted(os.listdir(eradir)):
            secdir = os.path.join(eradir, section)
            if not os.path.isdir(secdir):
                continue
            for name in sorted(os.listdir(secdir)):
                if not name.endswith(".md"):
                    continue
                full = os.path.join(secdir, name)
                rel = os.path.relpath(full, KB)
                fm = parse_frontmatter(full)
                if fm is None:
                    print("NO FRONTMATTER: %s" % rel, file=sys.stderr)
                    fm = {}
                entries.append({
                    "path": rel,
                    "title": fm.get("title", ""),
                    "id": fm.get("id", ""),
                    "section": fm.get("section", section),
                    "product": fm.get("category", "Logi Report"),
                    "era": era,
                    "era_label": ERA_LABEL.get(era, era),
                    "source_url": fm.get("url", ""),
                    "updated_at": fm.get("updated_at", ""),
                })

    manifest = {
        "name": "logi-report-kb",
        "description": "Logi Report documentation and API knowledge base",
        "document_count": len(entries),
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
