#!/usr/bin/env python3
"""Gate for the Logi Report Web API spec.

Every check here was chosen because it FAILS when the thing it guards is broken.
Two checks were tried and discarded during construction, and they are recorded in
api/spec/PROVENANCE.md so nobody re-adds them:

  - "endpoint returns non-404 on the live server": discarded. The server returns
    401 for every path under /jrserver/api, including fabricated ones, so it
    cannot tell a real endpoint from an invented one.
  - "spec path appears in the server jars": discarded. Real paths and the control
    string all returned zero hits, so it proves nothing.

MIN_CHECKS is pinned so deleting a check fails the gate rather than shrinking it.
"""
import hashlib, json, os, sys, subprocess

try:
    import yaml
except ImportError:
    print("FAIL setup: pyyaml not installed"); sys.exit(1)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SPEC_Y = os.path.join(ROOT, "api", "spec", "logireport-openapi.yaml")
SPEC_J = os.path.join(ROOT, "api", "spec", "logireport-openapi.json")
ENDPOINTS = os.path.join(ROOT, "api", "ENDPOINTS.md")
HASHFILE = os.path.join(ROOT, "api", "spec", "SPEC.sha256")
METHODS = ("get", "post", "put", "delete", "patch", "head", "options")
MIN_CHECKS = 6            # pinned: deleting a check must fail the gate
CONTAINER = "logireport"
CONTAINER_PATH = "/opt/LogiReport/Server/help/webapi/logireportserver.yaml"

results = []
def check(name, ok, detail=""):
    """ok: True pass, False fail, None NOT APPLICABLE.

    NOT APPLICABLE is for a check whose subject is genuinely absent from this
    machine, not for one that is inconvenient. It is printed, counted, and
    summarised at the end. A silent skip reads as a pass, which is the failure
    this gate exists to prevent.
    """
    results.append((name, ok, detail))
    print({True: "PASS ", False: "FAIL ", None: "N/A  "}[ok] + name +
          (f"  [{detail}]" if detail else ""))

def ops_of(spec):
    return [(p, m) for p, it in (spec.get("paths") or {}).items()
            for m in (it or {}) if m.lower() in METHODS]

def main():
    # 1. spec parses
    try:
        spec = yaml.safe_load(open(SPEC_Y))
        check("spec_yaml_parses", isinstance(spec, dict) and bool(spec.get("paths")))
    except Exception as e:
        check("spec_yaml_parses", False, str(e)[:60]); spec = {}

    # 2. json mirror agrees with yaml
    try:
        js = json.load(open(SPEC_J))
        check("json_mirror_agrees", ops_of(js) == ops_of(spec),
              f"{len(ops_of(js))} vs {len(ops_of(spec))} ops")
    except Exception as e:
        check("json_mirror_agrees", False, str(e)[:60])

    # 3. tamper check against the recorded hash
    digest = hashlib.sha256(open(SPEC_Y, "rb").read()).hexdigest()
    recorded = open(HASHFILE).read().split()[0].strip() if os.path.exists(HASHFILE) else None
    check("spec_matches_recorded_hash", recorded == digest,
          f"recorded={str(recorded)[:12]} actual={digest[:12]}")

    # 4. provenance: identical to what the running server ships.
    #
    # This check needs a Logi Report Server container running on THIS machine.
    # It is the strongest evidence in the file when it can run, and it can only
    # run where the container is. Before this was split out, the check passed on
    # the one laptop with the container up and failed everywhere else, including
    # in CI, which made the gate a statement about the machine rather than about
    # the repository.
    #
    # So: container reachable and hash differs is a hard FAIL and always will be.
    # Container absent is NOT APPLICABLE, named and counted. Docker present but
    # the container missing is also NOT APPLICABLE. A docker error that is
    # neither of those still fails, because an unexplained error is not an
    # absence.
    try:
        which = subprocess.run(["docker", "version", "--format", "{{.Server.Version}}"],
                               capture_output=True, text=True, timeout=25)
        if which.returncode != 0:
            check("matches_running_server_spec", None,
                  "no docker daemon on this machine")
        else:
            ps = subprocess.run(["docker", "ps", "--filter", f"name=^{CONTAINER}$",
                                 "--format", "{{.Names}}"],
                                capture_output=True, text=True, timeout=25)
            if ps.returncode != 0:
                # docker answered `version` and then refused `ps`. Permission
                # denied on the socket is the realistic case. Empty stdout would
                # otherwise read as "the container is not here", which turns a
                # broken environment into a clean NOT APPLICABLE. An error is not
                # an absence.
                check("matches_running_server_spec", False,
                      f"docker ps failed: {ps.stderr.strip()[:70]}")
            elif CONTAINER not in ps.stdout.split():
                check("matches_running_server_spec", None,
                      f"container '{CONTAINER}' is not running here")
            else:
                out = subprocess.run(["docker", "exec", CONTAINER, "sha256sum", CONTAINER_PATH],
                                     capture_output=True, text=True, timeout=25)
                live = out.stdout.split()[0] if out.returncode == 0 and out.stdout else None
                check("matches_running_server_spec", live == digest,
                      f"server={str(live)[:12]}" if live
                      else f"container up but the spec could not be read: "
                           f"{out.stderr.strip()[:60]}")
    except FileNotFoundError:
        check("matches_running_server_spec", None, "docker is not installed here")
    except Exception as e:
        check("matches_running_server_spec", False, str(e)[:60])

    # 5. ENDPOINTS.md covers EVERY operation (catches silent truncation)
    try:
        md = open(ENDPOINTS).read()
        base = spec.get("basePath", "") or ""
        missing = [f"{m.upper()} {base}{p}" for p, m in ops_of(spec)
                   if f"`{m.upper()} {base}{p}`" not in md]
        check("endpoints_md_covers_all_ops", not missing,
              f"{len(missing)} missing" if missing else f"{len(ops_of(spec))} ops")
    except Exception as e:
        check("endpoints_md_covers_all_ops", False, str(e)[:60])

    # 6. ENDPOINTS.md states the format difference vs Composer (stops silent drift
    #    back into implying the two specs are interchangeable)
    try:
        md = open(ENDPOINTS).read()
        check("states_format_difference", "Swagger 2.0" in md and "OpenAPI 3.1.0" in md)
    except Exception as e:
        check("states_format_difference", False, str(e)[:60])

    # anti-shrink: the gate must not be quietly reduced
    if len(results) < MIN_CHECKS:
        print(f"\nFAIL gate_integrity: {len(results)} checks ran, MIN_CHECKS={MIN_CHECKS}")
        return 1

    failed = [n for n, ok, _ in results if ok is False]
    na = [n for n, ok, _ in results if ok is None]
    print(f"\n{len(results) - len(failed) - len(na)}/{len(results)} passed, "
          f"{len(na)} not applicable, {len(failed)} failed")
    if na:
        print("NOT APPLICABLE on this machine: " + ", ".join(na))
    if failed:
        print("GATE: RED -> " + ", ".join(failed)); return 1
    print("GATE: GREEN"); return 0

if __name__ == "__main__":
    sys.exit(main())
