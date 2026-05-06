#!/usr/bin/env python3
"""Convert a comma-separated Rundeck option into Ansible extra vars."""

import json
import re
import sys


def main() -> int:
    raw_apps = sys.argv[1] if len(sys.argv) > 1 else ""
    tenant = sys.argv[2] if len(sys.argv) > 2 else "partition_1"
    apps = [app.strip() for app in raw_apps.replace("\n", ",").split(",") if app.strip()]
    invalid = [app for app in apps if not re.fullmatch(r"[A-Za-z0-9_.-]+", app)]
    if invalid:
        print(f"Invalid AS3 app name(s): {', '.join(invalid)}", file=sys.stderr)
        return 2
    if not re.fullmatch(r"[A-Za-z0-9_.-]+", tenant):
        print(f"Invalid AS3 tenant name: {tenant}", file=sys.stderr)
        return 2

    print(json.dumps({"tenants": {tenant: {"apps": apps}}}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
