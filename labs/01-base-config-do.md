# 01 - Base Config With Declarative Onboarding

Goal: render and optionally deploy base BIG-IP configuration with DO.

Inspect:

- `group_vars/bigip/base_config.yml`
- `roles/bigip_do_gen/templates/declaration.yml.j2`
- `backup/do/json/bigip1.json` after generation

Generate:

```bash
ansible-playbook gen_do.yml
ansible-playbook artifact_summary_playbook.yml
```

Deploy:

```bash
ansible-playbook deploy_do.yml
```

Expected BIG-IP areas:

- System hostname/settings
- DNS
- NTP
- LTM provisioning
- VLANs
- Self IPs
- Static route

Cleanup/reset:

Base networking cleanup is environment-specific. For now, re-run DO with a
known-good base declaration or rebuild the lab BIG-IP snapshot.
