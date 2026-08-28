# Using this repo, and the others alongside it

These repositories are a shared knowledge base for insightsoftware's Logi Composer, Simba
Intelligence and Logi Report. They are maintained by Amin Hasan and anyone on the team is
welcome to clone, pin, fork or open an issue against them.

## The set

| Repo | What it holds | Refresh |
|---|---|---|
| [`isw-da/logi-si-docs`](https://github.com/isw-da/logi-si-docs) | Documentation mirror: SI, Composer v25 and v26, the legacy devnet archive, and the Composer OpenAPI specs | **Automatic**, weekly |
| [`isw-da/composer-mcp`](https://github.com/isw-da/composer-mcp) | Composer REST API as MCP tools, with guards, plus the reference docs | Manual |
| [`isw-da/simba-intelligence-skill`](https://github.com/isw-da/simba-intelligence-skill) | SI install, configuration and troubleshooting skills | Manual |
| [`isw-da/symphony-dashboard-builder-skill`](https://github.com/isw-da/symphony-dashboard-builder-skill) | Building Composer dashboards server side, and the client-side assembly around them | Manual |
| [`isw-da/simba-intelligence-mcp`](https://github.com/isw-da/simba-intelligence-mcp) | SI API as MCP tools (private) | Manual |
| [`isw-da/logi-report-kb`](https://github.com/isw-da/logi-report-kb) | Logi Report and JReport documentation and API surface | **Automatic**, weekly, but only the 3,891 current articles. The 9,344-article devnet archive is frozen because that host is dead, and `api/` needs a running instance CI cannot reach |

## This repo is private, and must stay private

Decided from an audit of its own contents, not assumed. `README.md` sets out the full
reasoning; the short version:

1. **It mirrors 13,235 pages of insightsoftware's product documentation.** The source help
   centres are publicly readable and their `robots.txt` permits crawling, but crawling
   permission is not a redistribution licence.
2. **`ORIENTATION.md` cites internal Jira issues**, which is useful provenance internally and
   an information leak publicly.
3. **`ORIENTATION.md` describes an unapproved internal FY27 naming proposal**, drawn from a
   Confluence space explicitly marked "not yet approved".

Nothing here carries credentials.

**To get access**, ask Amin Hasan or anyone with owner rights on the `isw-da` organisation to
add you to the repo. If you want a public version, the Jira citations and the FY27 proposal
have to come out first and the documentation licence question has to be settled properly.
That is a decision for someone with the authority to make it, and it has not been made.

## Current status: this repo has no release, and here is exactly why

`scripts/verify_kb.py` is **RED at `master`**, and has been since commit `e18200e`, which
added the Web API spec layer. It fails one check, `api_docs_trace_to_source`:

```
FAIL api_docs_trace_to_source: 2 problems:
  ['ENDPOINTS.md: cites no resolvable source doc',
   'composer-si-integration.md: cites no resolvable source doc']
```

The check requires every file in `api/` to cite at least one resolvable `../docs/*.md`. Both
of those files have real provenance that is not a corpus document: `ENDPOINTS.md` is derived
from `logireportserver.yaml` shipped inside the server, and `composer-si-integration.md`
cites Confluence page ids. So the finding is not "these files are unsourced", it is "the
check asks a question these two files cannot answer".

Either answer is defensible and both are somebody's call, not a formality:

- **Give the two files a corpus citation** if an honest one exists, or
- **Widen the check** so a file may instead declare a provenance the gate can verify: the
  spec file exists and its hash matches `SPEC.sha256`, or the Confluence ids are present and
  the file says the claim rests on them.

What is not defensible is deleting the check or exempting the files by name, which would turn
a real question into a green tick. Until it is settled, pushing a `v*` tag will run the
workflow, the workflow will run both gates, and the release will not be cut. That is the
system working.

## Pin a version, do not track a branch

Every repo cuts tagged releases. The default branch moves, sometimes several times a day,
and it moves because something turned out to be wrong. Pin unless you want that.

```bash
git clone --branch v0.1.0 --depth 1 https://github.com/isw-da/logi-report-kb.git
```

This repo has no tag yet, for the reason above. Until it does, clone `master` and run the
gates yourself.

## What this repo holds

A searchable mirror of the Logi Report documentation, organised so a person or an agent can
find the right page and answer from it, with the version era stated on every page.

| Directory | What it is |
|---|---|
| `docs/` | 13,235 articles across four eras, each with frontmatter naming its era, source and last-updated date |
| `api/` | The programmable surface: Catalog, Design, Server, Security, Information Bus, JavaScript, RMI, servlet integration, URL invocation, and the Server RESTful Web API |
| `api/spec/` | The Server Web API as Swagger 2.0 and JSON, 124 paths and 225 operations, copied out of a running 26.2 SP1 container with its hash recorded |
| `building-reports/` | The task-oriented layer over the corpus: how to actually build the thing |
| `MANIFEST.json`, `llms.txt` | Machine-readable index of every document, and the entry point for an agent |

**Read [`ORIENTATION.md`](ORIENTATION.md) first.** Logi Report is a renamed product whose
name collides with an unrelated 2004 product, whose version series skips v20 to v22, and
whose documentation lives on three hosts. Answering from the corpus without that context
produces confident wrong answers, and has done.

## How to trust what you read here

Two gates, both runnable from a fresh clone:

```bash
python3 -m pip install pyyaml     # verify_api.py parses the Swagger spec

python3 scripts/verify_kb.py
echo $?                           # on its own line: a pipe reports the pipe's status, not the gate's

python3 scripts/verify_api.py
echo $?
```

`verify_kb.py` runs 13 named checks against a pinned manifest, so a deleted check fails the
gate rather than shrinking it. It has been beaten before and hardened each time: an
adversarial review once defeated the retrieval check with twelve files of lorem ipsum, so it
now requires ten questions to be answered by ten distinct documents whose titles are on topic,
matching whole words in body text only.

`verify_api.py` runs 6 checks. One of them, `matches_running_server_spec`, compares the
committed spec against the one inside a running Logi Report Server container. That check now
reports **NOT APPLICABLE** where no docker daemon or no such container exists, by name and
counted in the summary, rather than failing. A docker that answers `version` and then refuses
`ps`, which is what a permission problem on the socket looks like, still fails: an error is
not an absence, and a fresh review caught that case reading as a clean skip. Before that split it passed on the one laptop with the
container up and failed everywhere else, which made the gate a statement about the machine
rather than about the repository. Where the container IS reachable and the hash differs, it
still fails hard, and always will.

A skip is always named and counted, never silent.

## What is deliberately not here

- **No credentials.** Two Confluence pages found during research expose a licence key and
  host credentials in plain text. They were deliberately never cited and their contents were
  never copied here. Whoever owns those pages should be told.
- **No customer names, deployed customer artefacts, or NDA-tagged material.**
- **No product binaries, jars or installers.** The spec was copied out of a running server;
  the server is not in here.
- **No reconstructed API prose.** `api/spec/` is the vendor's own definition, and
  `api/spec/PROVENANCE.md` records the two checks that were tried, found to prove nothing,
  and discarded, so nobody re-adds them.

## Contributing

Open an issue or a pull request. Two asks:

1. **Run the gates before you open it.** If your change makes a claim, the gate should be
   the thing that proves it, and if no existing check covers your claim, add one.
2. **Say how you know.** A file and line, a command and its output, a Confluence page id or
   a Jira key. "I believe" is fine as long as it says so; the corpus already contains several
   confident claims that turned out to be wrong, and each one cost somebody a day.
