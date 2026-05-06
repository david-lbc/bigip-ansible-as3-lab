# 00 - Automation Toolchain Readiness

Goal: confirm whether the lab BIG-IP has the extensions needed by later
exercises.

Inspect:

- `inventory.yml`
- `atc_check_playbook.yml`
- `do_check_playbook.yml`

Run:

```bash
ansible-playbook atc_check_playbook.yml
```

Expected result:

- AS3 returns HTTP 200 when Application Services 3 is installed.
- DO returns HTTP 200 when Declarative Onboarding is installed.
- HTTP 404 usually means the extension is not installed.

Next:

- If AS3 is missing, install AS3 before the AS3 app exercises.
- If DO is missing, install DO before the base-config exercise.
