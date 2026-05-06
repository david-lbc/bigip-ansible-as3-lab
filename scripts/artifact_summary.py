#!/usr/bin/env python3
"""Summarize generated lab artifacts without printing full declarations."""

import argparse
import json
from pathlib import Path


def load_json(path: Path):
    if not path.exists():
        return None
    with path.open() as fh:
        return json.load(fh)


def display_path(path: Path):
    try:
        return str(path.resolve().relative_to(Path.cwd().resolve()))
    except ValueError:
        return str(path)


def summarize_as3(path: Path):
    declaration = load_json(path)
    if declaration is None:
        return {"exists": False, "path": display_path(path)}

    adc = declaration.get("declaration", {})
    tenants = {}
    for tenant_name, tenant_body in adc.items():
        if not isinstance(tenant_body, dict) or tenant_body.get("class") != "Tenant":
            continue
        apps = [
            name
            for name, body in tenant_body.items()
            if isinstance(body, dict) and body.get("class") == "Application"
        ]
        tenants[tenant_name] = sorted(apps)

    return {
        "exists": True,
        "path": display_path(path),
        "updateMode": adc.get("updateMode"),
        "tenants": tenants,
    }


def summarize_do(path: Path):
    declaration = load_json(path)
    if declaration is None:
        return {"exists": False, "path": display_path(path)}

    common = declaration.get("Common", {})
    classes = {
        name: body.get("class")
        for name, body in common.items()
        if isinstance(body, dict) and "class" in body
    }
    return {
        "exists": True,
        "path": display_path(path),
        "classes": classes,
    }


def summarize_imperative(path: Path):
    return {"exists": path.exists(), "path": display_path(path)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", required=True)
    parser.add_argument("--backup-root", required=True)
    args = parser.parse_args()

    root = Path(args.backup_root)
    summary = {
        "host": args.host,
        "as3": summarize_as3(root / "as3" / "json" / f"{args.host}.json"),
        "do": summarize_do(root / "do" / "json" / f"{args.host}.json"),
        "imperative": summarize_imperative(root / "imperative" / f"{args.host}.yml"),
    }
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
