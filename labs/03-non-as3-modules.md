# 03 - Non-AS3 App With BIG-IP Modules

Goal: compare the AS3 path with an imperative object-by-object deployment.

Inspect:

- `group_vars/bigip/imperative_apps.yml`
- `roles/bigip_imperative_preview/templates/plan.yml.j2`
- `roles/bigip_imperative_deploy/tasks/main.yml`
- `backup/imperative/bigip1.yml` after preview

Preview:

```bash
ansible-playbook imperative_preview_playbook.yml
ansible-playbook artifact_summary_playbook.yml
```

Deploy:

```bash
ansible-playbook imperative_deploy_playbook.yml
```

Deploy and save config:

```bash
ansible-playbook imperative_deploy_playbook.yml -e imperative_save_config=true
```

Cleanup:

```bash
ansible-playbook imperative_cleanup_playbook.yml
```

Discussion points:

- The module path is explicit and familiar to many BIG-IP operators.
- The AS3 path is usually cleaner for app service intent.
- Some BIG-IP features may still need imperative modules until a declarative
  shape is designed for them.
