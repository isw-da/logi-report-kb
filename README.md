# Logi Report documentation, made machine-readable

## What this repository is, and what is in it

This repository is **public**. It is an unofficial, community mirror of
insightsoftware's published Logi Report and JReport documentation, maintained by
Amin Hasan so that a person or an AI assistant can search it offline and answer
from the right version. It is not an insightsoftware product, it is not an
official distribution, and nothing here is endorsed by insightsoftware. Ownership
and the licence position are set out in [`NOTICE`](NOTICE).

**What it contains.** 13,235 mirrored documentation articles, roughly 91MB of
text, pulled from three publicly readable help centres; the Server Web API
definition the product itself ships; a set of authored orientation, API and
task guides written over that corpus; and two verification gates.

**What it deliberately does not contain**, checked rather than assumed:

- **No credentials of any kind.** No licence keys, tokens, passwords or host
  details. Two internal pages found during research do expose a licence key and
  host credentials in plain text; they were never cited and their contents were
  never copied here.
- **No internal issue-tracker or wiki content.** An earlier revision of
  `ORIENTATION.md` cited internal Jira issue keys and described an unapproved
  internal naming proposal taken from a personal wiki space. Both were removed
  before this repository was shared. Where the underlying fact is supportable
  from a public source, it was kept and re-cited to that source; where it was
  not, it was dropped.
- **No customer names, deployed customer artefacts or NDA-tagged material.**
- **No product binaries, jars or installers.** The API spec was copied out of a
  running server; the server is not here.

Anything that should not be public, tell a@hasan.co and it comes out.

**How to depend on this repo is in [`CONSUMING.md`](CONSUMING.md)**: how to pin a
version, how to run the gates, and what is deliberately not in here.


A clean, searchable mirror of the Logi Report product documentation, organised so
a person or an AI assistant can find the right page and answer from it, with the
version era of every page stated on the page itself.

**Read [ORIENTATION.md](ORIENTATION.md) first.** Logi Report is a renamed
product (JReport, renamed at v17 in 2020) whose name collides with an unrelated
Logi Analytics product from 2004, whose version series skips v20 to v22, and
whose documentation lives on three different hosts. Answering from the corpus
without that context produces confident wrong answers, and has done.

## What's in it

Four eras, each a directory under [`docs/`](docs/), each article a markdown file
with frontmatter (`title`, `id`, `section`, `url`, plus `era` and `era_label`).

| Directory | Era | Articles | Source |
|---|---|---|---|
| `docs/jreport-v15-v16/` | product named Logi JReport, v15 and v16 | 2,637 | devnet.logianalytics.com |
| `docs/logi-report-v17-v19/` | after the v17 rename, v17 to v19 | 5,039 | devnet.logianalytics.com |
| `docs/unversioned/` | no version stated by the source | 1,668 | devnet.logianalytics.com |
| `docs/current/v23-v25/` | v23, v24, v25 | 2,418 | docs-report.zendesk.com |
| `docs/current/v26/` | v26, the current line | 1,473 | logi-report-v26.insightsoftware.com |

9,344 articles from devnet, 3,891 from the two current hosts, 13,235 in total.

Alongside the documents:

- [`MANIFEST.json`](MANIFEST.json), one machine-readable index of every
  document: path, title, Zendesk id, section, era, era label, source URL and
  the source's own last-updated date. Point a script or an agent at this to
  enumerate the corpus.
- [`llms.txt`](llms.txt), the same index in the llms.txt convention, grouped by
  era and section.
- `api/`, the reference for Logi Report's programmable surfaces (Java API,
  JavaScript API and URL invocation), each page citing the source document it
  was derived from.
- `building-reports/`, task-shaped guides assembled from the corpus.
- `CLAUDE.md`, the instructions for an agent working inside this repository.

## Provenance

Three sources, all pulled through the public Zendesk Help Center API. No token
is needed; the token route in Zendesk's own guides is for admin actions and does
not apply to reading published articles. The `/en-us/` locale segment is
mandatory, the locale-less path returns a 301.

**devnet.logianalytics.com** carries v15 to v19 and nothing after. Its last
article predates 1 February 2023: 6,113 of its Logi Report articles date to 2021
and 3,165 to 2022. That is a hosting artefact, not a signal about the product.
The documentation moved off devnet at the 23.1 release, and moved again for v26.
See ORIENTATION.md for the full account.

**docs-report.zendesk.com** carries v23, v24 and v25. Its oldest articles were
created on 23 January 2023, days before 23.1 shipped. v23 is marked Archive.

**logi-report-v26.insightsoftware.com** carries v26, the current line. Its Logi
Report category was last updated on 31 July 2026. Designer is section
45189079491341 and Server is section 45202990176141. The devnet index still
points at two older v26 section ids that no longer resolve.

Snapshot taken 22 August 2026.

## How to refresh it

Two steps, in order.

1. `scripts/pull_docs.py` re-pulls the current-era articles from the two Zendesk
   hosts into `docs/current/` and writes `docs/current/PROVENANCE.json` (pull
   timestamp, per-host article and section counts, status). It requests one page
   at a time with a pause between pages, and reports any page cap it hits rather
   than truncating silently.
2. [`scripts/build_index.py`](scripts/build_index.py) rebuilds
   [`MANIFEST.json`](MANIFEST.json) and [`llms.txt`](llms.txt) from the document
   frontmatter. It is mechanical on purpose, so code does it rather than an
   agent. Run it after any change to `docs/`.

## How it is verified

Two gates.

[`scripts/verify_kb.py`](scripts/verify_kb.py) covers the corpus. It exits 0 only
when every named check both ran and passed; a skipped check is reported as RED,
and the checks are tracked against a blessed manifest so a deleted check cannot
hide behind an added one.

[`scripts/verify_api.py`](scripts/verify_api.py) covers the Web API spec, in six
checks. One of them compares the committed spec against the one inside a running
Logi Report Server container, and reports NOT APPLICABLE, by name and counted,
where no such container exists. Where the container is reachable and the hash
differs, it still fails hard.

```
python3 -m pip install pyyaml      # verify_api.py parses the Swagger spec
python3 scripts/verify_kb.py
echo $?
python3 scripts/verify_api.py
echo $?
```

Both gates are green at `master`. `verify_kb.py` was red for a period after the
Web API spec layer was added, on `api_docs_trace_to_source`; that is settled and
`CONSUMING.md` records how. No release is cut while a gate is red, which is the
system working.

Thirteen checks in `verify_kb.py`, of which four are worth knowing about:

- `no_orphan_files` and `manifest_matches_disk` compare the manifest and the
  tree in both directions, so neither a stale index nor an unindexed file
  passes.
- `era_labelled` fails if any document lacks an era, which is what stops a v16
  answer being served as if it were current.
- `no_composer_confusion` greps the authored files for text equating Logi Report
  with Logi Composer. They are separate products; see ORIENTATION.md.
- `retrieval_smoke_test` asks ten real questions (what a catalog is, building a
  crosstab, scheduling a task, page report against web report, the Server API,
  URL invocation) and fails if the corpus cannot answer one of them. It would
  fail if the content were deleted, which is the point.

## Honest limits

- **The assistant retrieves, it does not know.** Answer quality depends on what
  got indexed and how the question is phrased. It can still fetch the wrong
  page, and across four eras the wrong page is often a real page from the wrong
  version. Always check the `era_label` on what comes back.
- **This is a snapshot.** Logi Report is actively developed; 26.3 and 26.4 were
  in flight when this was pulled. Re-run the pull before relying on version
  detail.
- **A fourth documentation move is in progress**, off Zendesk and MadCap Flare
  to Mintlify. When it lands, `scripts/pull_docs.py` will need a new source.
- **The devnet era is over-represented.** 9,344 of 13,235 articles describe v15
  to v19, so naive retrieval skews old. Prefer `docs/current/` for anything a
  customer is running today.
- **Reference boilerplate is thin by design.** The largest per-widget property
  and dialog-box sections of the devnet corpus were low-yield and are not the
  strength of this mirror.
- **Licence.** This mirrors insightsoftware's documentation, and that content
  remains insightsoftware's. The crawler policy on the current hosts permits
  fetching the article paths and the help centre API, but a crawler policy is not
  a redistribution licence, and no terms-of-use page granting one was found. The
  full position, including what is and is not being claimed, is in
  [`NOTICE`](NOTICE).
