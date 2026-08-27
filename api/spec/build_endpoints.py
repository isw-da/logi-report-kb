#!/usr/bin/env python3
"""Generate ENDPOINTS.md from the shipped Logi Report Server OpenAPI spec.

Deliberately mirrors the shape of si-docs-mirror/composer-api/ENDPOINTS.md so the
two products are readable side by side. The spec is Swagger 2.0 (the server ships
it that way); Composer's is OpenAPI 3.1. That difference is stated, not hidden.
"""
import yaml, json, sys, os, collections

HERE = os.path.dirname(os.path.abspath(__file__))
SPEC = os.path.join(HERE, "logireport-openapi.yaml")
OUT  = os.path.join(HERE, "..", "ENDPOINTS.md")
METHODS = ("get", "post", "put", "delete", "patch", "head", "options")

def load():
    with open(SPEC) as f:
        return yaml.safe_load(f)

def operations(spec):
    """Yield (tag, method, path, summary) for every operation."""
    base = spec.get("basePath", "") or ""
    for path, item in (spec.get("paths") or {}).items():
        for method, op in (item or {}).items():
            if method.lower() not in METHODS:
                continue
            op = op or {}
            tags = op.get("tags") or ["untagged"]
            summary = (op.get("summary") or op.get("description") or "").strip()
            summary = summary.split("\n")[0]
            yield tags[0], method.upper(), base + path, summary

def main():
    spec = load()
    info = spec.get("info", {})
    ops = sorted(operations(spec), key=lambda r: (r[0].lower(), r[2], r[1]))
    by_tag = collections.OrderedDict()
    for tag, m, p, s in ops:
        by_tag.setdefault(tag, []).append((m, p, s))

    version = spec.get("openapi") or ("Swagger " + spec.get("swagger", "?"))
    lines = [
        "# Logi Report Server Web API — endpoint index",
        "",
        f"Source: `logireportserver.yaml`, shipped inside Logi Report Server at",
        f"`/opt/LogiReport/Server/help/webapi/logireportserver.yaml` and served by the",
        f"bundled Swagger UI at `/help/webapi/webapi-docs/`. Extracted from a running",
        f"**{info.get('title','Logi Report Server')} {info.get('version','')}** instance "
        f"(product build 26.2 SP1).",
        "",
        f"**{len(ops)} operations across {len(by_tag)} tags, over {len(spec.get('paths') or {})} paths.**",
        "",
        f"Spec format: **{version}**. Note this differs from Composer, whose spec is",
        "OpenAPI 3.1.0 (`si-docs-mirror/composer-api/composer-openapi.json`). Any tool",
        "consuming both must handle the two formats, or convert. Machine-readable copies",
        "here: `spec/logireport-openapi.yaml` and `spec/logireport-openapi.json`.",
        "",
    ]
    if spec.get("basePath"):
        lines += [f"All paths below are shown with the spec's `basePath` (`{spec['basePath']}`) applied.", ""]

    for tag, entries in by_tag.items():
        lines.append(f"## {tag}")
        lines.append("")
        for m, p, s in entries:
            lines.append(f"- `{m} {p}`" + (f" — {s}" if s else ""))
        lines.append("")

    with open(OUT, "w") as f:
        f.write("\n".join(lines))
    print(f"wrote {OUT}: {len(ops)} operations, {len(by_tag)} tags")

if __name__ == "__main__":
    main()
