# Where this spec came from, and what it is worth

## Source

`logireportserver.yaml`, copied out of a running Logi Report Server **26.2 SP1**
container from:

```
/opt/LogiReport/Server/help/webapi/logireportserver.yaml
```

The server ships a bundled Swagger UI at `help/webapi/webapi-docs/` whose
`swagger-initializer.js` loads `../logireportserver.yaml`. So this is the
vendor's own published API definition, not something reconstructed from prose.

- **Spec format:** Swagger 2.0 (`swagger: "2.0"`), title "Logi Report Server",
  spec version 1.3.0
- **Base path:** `/jrserver/api/v1.2`
- **124 paths, 225 operations, 11 tags**
- SHA-256 recorded in `SPEC.sha256` and re-checked against the running container
  by `scripts/verify_api.py`

## How this compares with Composer

| | Logi Report | Logi Composer |
|---|---|---|
| Spec format | **Swagger 2.0** | **OpenAPI 3.1.0** |
| Paths | 124 | 220 |
| Operations | 225 | 338 |
| Tags | 11 | 75 |
| How obtained | shipped file inside the server install | pulled from a live `/composer/api-docs` |

**The format difference is the practical catch.** Anything consuming both (an MCP
server, a codegen step, a validator) must either handle Swagger 2.0 and OpenAPI
3.1 or convert one to the other. Do not assume a tool that works against
`composer-openapi.json` will work here unchanged.

## Two checks that were tried and discarded

Recorded so nobody adds them back believing they prove something.

**1. "A real endpoint returns non-404 on the live server."** Discarded. The server
returns **401 for every path under `/jrserver/api`**, including fabricated ones:

```
/jrserver/api/v1.2/bookmark      401     (real)
/jrserver/api/v1.2/zzzznotreal   401     (invented)
/jrserver/api/v9.9/tree          401     (invented version)
```

The control returned exactly what the real endpoints returned, so the check
cannot distinguish a genuine endpoint from an invented one. It would have passed
against a completely fabricated spec.

**2. "A spec path appears as a string in the server jars."** Discarded. Real paths
(`bookmark/default/clear`, `node/rptcatrelation`, `sso/register`) and the control
string all returned **zero** matching jars. It proves nothing either way.

## What the gate actually proves, and what it does not

**Proves:** the spec in this repo is byte-identical to the one the running 26.2
SP1 server ships, the JSON mirror agrees with the YAML, and `ENDPOINTS.md` lists
every one of the 225 operations with none silently dropped.

**Does not prove:** that every documented endpoint behaves as described, or that
the server implements nothing beyond the spec. Verifying behaviour needs an
authenticated call per endpoint, which has not been done. Treat the spec as
authoritative on **surface**, not on **behaviour**.
