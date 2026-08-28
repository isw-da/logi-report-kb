# graphrun: bring Logi Report docs and API spec to Composer/SI parity

## Shape decision, stated plainly

The brief asks for a fan-out. **This ran as a single loop, not a fleet.** After
the Step 3 pilot the work turned out to be one deterministic pipeline (extract
spec, convert, index, verify) rather than N independent slices, and the graph
brief says to say so rather than spend fleet money on a chain. The one genuinely
parallel node, the Confluence sweep, was cheap enough to run inline.

The session's system instruction also forbids spawning subagents unless asked
directly, which reinforced the same call.

## The premise needed correcting first

The mission implies Logi Report documentation does not exist. It does: the KB at
`isw-da/logi-report-kb` (13,235 docs) was built earlier in this same session. The
real gap was narrower and sharper:

| | Logi Report (before) | Logi Composer |
|---|---|---|
| Prose API docs | 11 files in `api/` | yes |
| **Machine-readable spec** | **none** | `composer-openapi.json`, OpenAPI 3.1, 220 paths / 338 ops |
| Endpoint index | none | `ENDPOINTS.md`, 569 lines |

So the job was the machine-readable spec, not the documentation.

## What was found

The running Logi Report Server 26.2 SP1 **ships its own OpenAPI spec**, served by
a bundled Swagger UI:

```
/opt/LogiReport/Server/help/webapi/logireportserver.yaml     299,629 bytes
/opt/LogiReport/Server/help/webapi/webapi-docs/              Swagger UI
```

Swagger 2.0, title "Logi Report Server", spec version 1.3.0,
**124 paths, 225 operations, 11 tags**, base path `/jrserver/api/v1.2`.

Peter's instinct in the call ("fairly well documented, probably more than
Composer") was directionally right on documentation quality; on raw surface,
Composer is larger (338 ops vs 225).

## Evidence: the gate, and proof it can fail

Break-it-first was run before the gate was trusted. Four deliberate breaks:

| Break | Result |
|---|---|
| Tamper one byte in the spec | EXIT=1, `spec_matches_recorded_hash` + `matches_running_server_spec` |
| Truncate ENDPOINTS.md | EXIT=1, `endpoints_md_covers_all_ops [206 missing]` |
| Delete a check from the gate | EXIT=1, `gate_integrity` (MIN_CHECKS pinned at 6) |
| Drift the JSON mirror from the YAML | EXIT=1, `json_mirror_agrees [222 vs 225]` |

Restored, final run:

```
PASS spec_yaml_parses
PASS json_mirror_agrees  [225 vs 225 ops]
PASS spec_matches_recorded_hash  [recorded=b98899cda4a4 actual=b98899cda4a4]
PASS matches_running_server_spec  [server=b98899cda4a4]
PASS endpoints_md_covers_all_ops  [225 ops]
PASS states_format_difference

6/6 passed
GATE: GREEN
EXIT=0
```

## Two checks tried and discarded, and why that matters

Both would have passed against a **completely fabricated spec**, so they were
removed rather than kept for reassurance. Recorded in `api/spec/PROVENANCE.md`.

1. **"Real endpoints return non-404 on the live server."** The server returns 401
   for every path under `/jrserver/api`, including `zzzznotreal` and `api/v9.9`.
   The control behaved identically to the real endpoints.
2. **"Spec paths appear in the server jars."** Real paths and the control string
   all returned zero hits.

What replaced them is a provenance hash: the local spec is byte-identical to the
one the running server ships (sha256 `b98899cda4a4…`), re-checked live each run.

## The finding worth more than the spec

The call's unanswered question was whether Logi Report Business Views transfer to
Composer or Simba Intelligence. Confluence shows an active programme, running
**the opposite way**: Composer Source → Logi Report Catalog/BV, covering
datasource, query, BV, derived fields, global filters and RLS/CLS security.
Seven pages, most recent 24 Aug 2026. Captured in `api/composer-si-integration.md`.

It also records two security-translation limits that make an unqualified "your
security rules come across" claim unsupportable today (CLS `onCondition` has no
dynamic equivalent; RLS Dynamic User Attribute has no target context yet).

## What this run did NOT do, stated so nobody assumes otherwise

- **No behavioural verification.** The gate proves the documented *surface* is
  authentic; it does not prove any endpoint behaves as described. That needs an
  authenticated call per endpoint and was not done.
- **No Swagger 2.0 to OpenAPI 3.1 conversion.** Both formats are shipped as-is
  and the difference is stated loudly. A converter is the obvious next step if an
  MCP server is built.
- **No Logi Report MCP server.** Composer has `composer-mcp` (~43 tools); Logi
  Report still has none. The spec is now the input that makes one buildable.
- **No adversarial review by an independent agent.** Spawning was not available
  in this session, so the verification above was performed by the run itself.
  A script written against my own claim is not an adversary; weigh it accordingly.

## Next, in priority order

1. Build `logi-report-mcp` from the spec, mirroring `composer-mcp`.
2. Convert the spec to OpenAPI 3.1 so one toolchain serves both products.
3. Pull the Postman collection (`att18502090755`) for request-level examples.
