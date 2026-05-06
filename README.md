# BIG-IP Ansible, AS3, DO, and Rundeck Lab

This repo is a learning lab for different BIG-IP automation shapes. It is not
intended to be a production opinion about how every BIG-IP should be managed.

The lab shows four paths:

- Declarative Onboarding (DO) for base BIG-IP config such as DNS, NTP,
  provisioning, VLANs, self IPs, and routes.
- AS3 with Ansible and Jinja for declarative application services.
- Non-AS3 Ansible modules for imperative, object-by-object deployment.
- Rundeck Open Source as a self-service job catalog that runs the playbooks.

## Local Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
ansible-galaxy collection install -r collections/requirements.yml -p ./collections
```

The inventory defaults to `admin/admin` for a lab BIG-IP. Override without
editing files when needed:

```bash
export BIGIP_ADMIN_USER=admin
export BIGIP_ADMIN_PASSWORD=admin
export BIGIP_MGMT_PORT=443
```

Generate everything without deploying:

```bash
ansible-playbook atc_check_playbook.yml
ansible-playbook gen_do.yml
ansible-playbook gen_as3.yml
ansible-playbook artifact_summary_playbook.yml
ansible-playbook imperative_preview_playbook.yml
```

Deploy in the normal lab order:

```bash
ansible-playbook do_check_playbook.yml
ansible-playbook gen_do.yml
ansible-playbook deploy_do.yml
ansible-playbook gen_as3.yml
ansible-playbook as3_dry_run_playbook.yml
ansible-playbook deploy_as3.yml
```

The non-AS3 example is separate on purpose:

```bash
ansible-playbook imperative_preview_playbook.yml
ansible-playbook imperative_deploy_playbook.yml
```

Generated declarations and previews land under `backup/`.

Cleanup examples:

```bash
ansible-playbook as3_cleanup_playbook.yml
ansible-playbook imperative_cleanup_playbook.yml
```

## AS3 Apps

The `bigip_as3_gen` role uses app templates under
`roles/bigip_as3_gen/templates/app/templates`.

Included AS3 app shapes:

- `http`
- `https`
- `dns`
- `forward`

The default app list is in `host_vars/bigip1.yml`. Override it from the CLI or
Rundeck:

```bash
ansible-playbook gen_as3.yml \
  -e '{"tenants":{"partition_1":{"apps":["APP-http-simple","APP-dns"]}}}'
```

This lab defaults AS3 `updateMode` to `selective`, which means AS3 only updates
tenants defined in the declaration instead of removing omitted tenants.

## Rundeck

Run the bundled Rundeck Open Source lab:

```bash
docker compose up --build
```

Then open `http://localhost:4440`. See `docs/RUNDECK_LAB.md` for project and
job import steps.

## Docs

- `docs/DEPLOYMENT_SHAPES.md` explains which layer owns each kind of work.
- `docs/RUNDECK_LAB.md` walks through the self-service Rundeck setup.
- `docs/MCP_AI_EXERCISES.md` outlines optional MCP/AI learning exercises.
- `labs/` contains short hands-on exercise guides.
- `REFERENCE.md` keeps the detailed AS3 variable reference.

## Reference

The AS3 variable reference can be found under `REFERENCE.md`.

## General Tips

On macOS, if you see an error around `fork()`, set this in your shell profile:

```bash
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
```

Some macOS Python environments also need extra care around VMware `pyVmomi`
dependencies when using the optional OVA deployment playbook.
