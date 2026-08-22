#!/usr/bin/env python3
"""Pull current Logi Report documentation into docs/current/.

Sources, both open Zendesk Help Center APIs, no auth (verified by the sweep-field
node, 2026-08-22). The /en-us/ locale segment is mandatory; the locale-less path
301s.

  docs-report.zendesk.com               v23, v24, v25   ~2,418 articles
  logi-report-v26.insightsoftware.com   v26             ~1,473 articles

Polite by construction: one request at a time, a pause between pages, a real
User-Agent, and a hard page cap that is REPORTED rather than silent.

This mirrors insightsoftware's own documentation. Whether it may be republished
is a licence question this script does not answer and must not be assumed.
"""
import html, json, os, re, sys, time, urllib.request, urllib.error

KB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(KB, "docs", "current")

HOSTS = [
    ("docs-report.zendesk.com", "v23-v25"),
    ("logi-report-v26.insightsoftware.com", "v26"),
]
UA = "logi-report-kb-mirror/1.0 (documentation archive; contact a@hasan.co)"
PAUSE = 0.4
MAX_PAGES = 400          # generous; breaching it is reported, never silent


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                               "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def fetch_all(host, kind):
    """kind is 'articles', 'sections' or 'categories'."""
    out, page, url = [], 0, "https://%s/api/v2/help_center/en-us/%s.json?per_page=100" % (host, kind)
    while url:
        page += 1
        if page > MAX_PAGES:
            print("  !! PAGE CAP %d HIT for %s/%s; %d collected, MORE REMAIN"
                  % (MAX_PAGES, host, kind, len(out)), file=sys.stderr)
            break
        try:
            data = get(url)
        except urllib.error.HTTPError as e:
            print("  !! HTTP %s on %s" % (e.code, url), file=sys.stderr)
            break
        out.extend(data.get(kind, []))
        url = data.get("next_page")
        sys.stdout.write("\r  %s %s: %d" % (host, kind, len(out))); sys.stdout.flush()
        time.sleep(PAUSE)
    print()
    return out


TAG = re.compile(r"<[^>]+>")
CELL = re.compile(r"<t[dh][^>]*>(.*?)</t[dh]>", re.I | re.S)
ROW = re.compile(r"<tr[^>]*>(.*?)</tr>", re.I | re.S)
TABLE = re.compile(r"<table[^>]*>(.*?)</table>", re.I | re.S)


def _cell(c):
    """Flatten one cell to a single markdown-table-safe line."""
    c = re.sub(r"<br\s*/?>", " ", c, flags=re.I)
    c = re.sub(r"</p>", " ", c, flags=re.I)
    c = TAG.sub("", c)
    c = html.unescape(c)
    return re.sub(r"\s+", " ", c).replace("|", "\\|").strip()


def _table(m):
    """Render an HTML table as a real markdown table. Property tables are the
    core reference content for building reports, so losing their structure
    loses most of the value of this corpus."""
    rows = []
    for r in ROW.findall(m.group(1)):
        cells = [_cell(c) for c in CELL.findall(r)]
        if any(cells):
            rows.append(cells)
    if not rows:
        return "\n"
    width = max(len(r) for r in rows)
    rows = [r + [""] * (width - len(r)) for r in rows]
    head, body = rows[0], rows[1:]
    out = ["", "| " + " | ".join(head) + " |",
           "|" + "|".join([" --- "] * width) + "|"]
    out += ["| " + " | ".join(r) + " |" for r in body]
    return "\n".join(out) + "\n"


def to_markdown(body):
    """Zendesk serves HTML. Tables become real markdown tables; everything else
    is flattened with entities decoded. The source_url in the frontmatter is the
    authority if the conversion loses nuance."""
    if not body:
        return ""
    s = body
    s = TABLE.sub(_table, s)
    s = re.sub(r"<br\s*/?>", "\n", s, flags=re.I)
    s = re.sub(r"</(p|div|tr|li|h[1-6])>", "\n", s, flags=re.I)
    s = re.sub(r"<li[^>]*>", "- ", s, flags=re.I)
    s = re.sub(r"<h1[^>]*>", "\n# ", s, flags=re.I)
    s = re.sub(r"<h2[^>]*>", "\n## ", s, flags=re.I)
    s = re.sub(r"<h3[^>]*>", "\n### ", s, flags=re.I)
    s = re.sub(r"<h[456][^>]*>", "\n#### ", s, flags=re.I)
    s = TAG.sub("", s)
    s = html.unescape(s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def slug(t):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", (t or "").lower())).strip("-")[:80] or "untitled"


def main():
    os.makedirs(OUT, exist_ok=True)
    total = 0
    provenance = []
    for host, label in HOSTS:
        print("== %s (%s)" % (host, label))
        sections = {s["id"]: s for s in fetch_all(host, "sections")}
        articles = fetch_all(host, "articles")
        if not articles:
            print("  !! nothing pulled from %s" % host, file=sys.stderr)
            provenance.append({"host": host, "label": label, "articles": 0,
                               "sections": len(sections), "status": "FAILED"})
            continue
        for a in articles:
            sec = sections.get(a.get("section_id"), {})
            secname = slug(sec.get("name") or "unsectioned")
            d = os.path.join(OUT, label, secname)
            os.makedirs(d, exist_ok=True)
            path = os.path.join(d, "%s-%s.md" % (a["id"], slug(a.get("title"))))
            fm = [
                "---",
                'title: "%s"' % (a.get("title") or "").replace('"', "'"),
                "id: %s" % a["id"],
                'section: "%s"' % (sec.get("name") or "Unsectioned").replace('"', "'"),
                'category: "Logi Report"',
                "url: %s" % a.get("html_url", ""),
                "updated_at: %s" % a.get("updated_at", ""),
                "source_host: %s" % host,
                "---",
                "",
            ]
            with open(path, "w", encoding="utf-8") as fh:
                fh.write("\n".join(fm) + to_markdown(a.get("body")) + "\n")
            total += 1
        provenance.append({"host": host, "label": label, "articles": len(articles),
                           "sections": len(sections), "status": "ok"})
        print("  wrote %d articles across %d sections" % (len(articles), len(sections)))

    with open(os.path.join(OUT, "PROVENANCE.json"), "w", encoding="utf-8") as fh:
        json.dump({"pulled_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                   "sources": provenance, "total_articles": total}, fh, indent=1)
    print("TOTAL pulled: %d" % total)


if __name__ == "__main__":
    main()
