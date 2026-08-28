# Using this repo, and the others alongside it

These repositories are a shared knowledge base for insightsoftware's Logi Composer, Simba
Intelligence and Logi Report. They are maintained by Amin Hasan and anyone on the team is
welcome to clone, pin, fork or open an issue against them.

## The set

<!-- toolkit-table: generated from toolkit.json, do not edit by hand -->

| Repo | What it holds | Refresh |
|---|---|---|
| [`isw-da/logi-si-docs`](https://github.com/isw-da/logi-si-docs) | Documentation mirror: SI, Composer v25 and v26, the legacy devnet archive, and the Composer OpenAPI specs | **Automatic**, weekly |
| [`isw-da/composer-mcp`](https://github.com/isw-da/composer-mcp) | Composer REST API as MCP tools, with guards, plus the reference docs | Manual |
| [`isw-da/simba-intelligence-skill`](https://github.com/isw-da/simba-intelligence-skill) | SI install, configuration and troubleshooting skills | Manual |
| [`isw-da/symphony-dashboard-builder-skill`](https://github.com/isw-da/symphony-dashboard-builder-skill) | Building Composer dashboards server side, and the client-side assembly around them | Manual |
| [`isw-da/simba-intelligence-mcp`](https://github.com/isw-da/simba-intelligence-mcp) | SI API as MCP tools (private) | Manual |
| [`isw-da/logi-report-kb`](https://github.com/isw-da/logi-report-kb) | Logi Report and JReport documentation and API surface | **Automatic**, weekly, but only the 3,891 current articles. The 9,344-article devnet archive is frozen because that host is dead, and `api/` needs a running instance CI cannot reach |

<!-- /toolkit-table -->

## This repo is public, and here is what that means

This repository is open on GitHub. It is an unofficial mirror of insightsoftware's
**published** Logi Report and JReport documentation, maintained by Amin Hasan. It is not an
insightsoftware product and it is not an official distribution. Ownership and the licence
position are in [`NOTICE`](NOTICE); `README.md` sets out the contents.

Because it is public, three things were stripped before it was shared, and must not come
back:

1. **Internal issue-tracker references.** An earlier revision of `ORIENTATION.md` cited Jira
   issue keys, board numbers and internal repository names. They are gone. Where the fact
   they supported is visible in the public documentation, it was kept and re-cited there.
2. **An unapproved internal naming proposal** taken from a personal wiki space and marked
   "not yet approved". Removed entirely. It was never a product name and stating it as one
   would have been wrong even internally.
3. **Internal commercial and sales material**: entitlement SOPs, SKU wording, sales-enablement
   greps, a recorded prospect call and the roadmap deck. All removed.

**No credentials of any kind are here.** That was checked rather than assumed: no key
material, no host credentials, no tokens, in any file or in the mirrored corpus.

If you find something here that should not be public, mail a@hasan.co and it comes out. Note
that removing a file from the working tree does not remove it from git history; anything that
needs to leave the history is a separate, deliberate rewrite.

## Current status

Both gates are green at `master`, and `v0.2.0` is tagged. `verify_kb.py` was red for a period
after commit `e18200e` added the Web API spec layer, on `api_docs_trace_to_source`: the check
requires every file in `api/` to cite at least one resolvable `../docs/*.md`, and two files
had real provenance that was not a corpus document. That was settled by widening the check to
accept a verifiable spec provenance, and by holding back the file whose only provenance was
internal wiki pages. The check itself was not deleted and no file is exempted by name, which
would have turned a real question into a green tick.

## Pin a version, do not track a branch

Every repo cuts tagged releases. The default branch moves, sometimes several times a day,
and it moves because something turned out to be wrong. Pin unless you want that.

```bash
git clone --branch v0.2.0 --depth 1 https://github.com/isw-da/logi-report-kb.git
```

`v0.2.0` is the current tag. Run the gates yourself after cloning either way; they are the
thing that proves the claims.

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

- **No credentials.** No key material, host credentials or tokens, in any file or anywhere in
  the mirrored corpus. Checked, not assumed.
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
2. **Say how you know.** A file and line, a command and its output, or a public source URL.
   "I believe" is fine as long as it says so; the corpus already contains several confident
   claims that turned out to be wrong, and each one cost somebody a day. Because this repo is
   public, cite a public source: do not paste internal issue keys, wiki page ids or customer
   detail into it.
