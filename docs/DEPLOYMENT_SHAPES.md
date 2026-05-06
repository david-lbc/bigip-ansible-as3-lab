# Deployment Shapes

This lab intentionally separates product/demo flow from reusable BIG-IP
automation primitives.

## 1. DO Base Config

Use Declarative Onboarding for base BIG-IP setup:

- hostname and system behavior
- DNS and NTP
- module provisioning
- VLANs
- self IPs
- routes and management routes

Lab files:

- `atc_check_playbook.yml`
- `group_vars/bigip/base_config.yml`
- `gen_do.yml`
- `deploy_do.yml`
- `roles/bigip_do_gen`
- `roles/bigip_do_deploy`

## 2. AS3 Application Services

Use AS3 for declarative L4-L7 app services. The lab renders AS3 with Ansible
variables and Jinja templates, validates the declaration with `jsonschema`, and
posts it to the AS3 endpoint.

Lab files:

- `group_vars/bigip/APP-*.yml`
- `gen_as3.yml`
- `artifact_summary_playbook.yml`
- `as3_dry_run_playbook.yml`
- `deploy_as3.yml`
- `as3_cleanup_playbook.yml`
- `roles/bigip_as3_gen`
- `roles/bigip_as3_deploy`

The lab defaults AS3 `updateMode` to `selective`. F5 documents that selective
mode modifies only tenants present in the declaration, while complete mode can
remove omitted tenants.

## 3. Non-AS3 Imperative Modules

Use `f5networks.f5_modules` when the lesson is about imperative object
lifecycle, module behavior, or a BIG-IP feature not represented in this AS3
template set.

Lab files:

- `group_vars/bigip/imperative_apps.yml`
- `imperative_preview_playbook.yml`
- `imperative_deploy_playbook.yml`
- `imperative_cleanup_playbook.yml`
- `roles/bigip_imperative_preview`
- `roles/bigip_imperative_deploy`
- `roles/bigip_imperative_cleanup`

## 4. Rundeck Self-Service

Rundeck owns the self-service catalog experience. It collects options and runs
the playbooks. It does not own BIG-IP semantics.

Lab files:

- `docker-compose.yml`
- `rundeck/Dockerfile`
- `rundeck/jobs/bigip-self-service-lab.yml`

The Rundeck flow includes generate/review/dry-run steps before deploy jobs.

## 5. MCP/AI Optional Exercises

MCP servers should expose typed BIG-IP capabilities, not this whole lab as one
magic command. The lab can use MCP later for explanation, validation,
translation, and troubleshooting exercises.

The DO MCP tracking issue is:

- https://gitlab.thelbc.io/cute-pm/cute-bigip-mcp/-/work_items/297
