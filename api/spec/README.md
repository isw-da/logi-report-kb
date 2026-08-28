# Machine-readable Logi Report Server Web API spec

- `logireport-openapi.yaml` — the vendor's shipped spec, byte-for-byte
- `logireport-openapi.json` — same content as JSON, for tools that prefer it
- `SPEC.sha256` — tamper/provenance hash, checked by `scripts/verify_api.py`
- `build_endpoints.py` — regenerates `../ENDPOINTS.md` from the spec
- `PROVENANCE.md` — where it came from, how it compares with Composer, and the
  two verification checks that were tried and discarded

Regenerate the index after replacing the spec:

```bash
python3 api/spec/build_endpoints.py && python3 scripts/verify_api.py
```

Refresh from a running server (any 26.x install):

```bash
docker cp <container>:/opt/LogiReport/Server/help/webapi/logireportserver.yaml \
  api/spec/logireport-openapi.yaml
shasum -a 256 api/spec/logireport-openapi.yaml | awk '{print $1}' > api/spec/SPEC.sha256
python3 api/spec/build_endpoints.py && python3 scripts/verify_api.py
```
