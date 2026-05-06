# 02 - Application Services With AS3

Goal: render, review, dry-run, and deploy app services with AS3.

Inspect:

- `group_vars/bigip/APP-http-simple.yml`
- `group_vars/bigip/APP-https-temp.yml`
- `group_vars/bigip/APP-dns.yml`
- `group_vars/bigip/APP-forward-net.yml`
- `roles/bigip_as3_gen/templates/app/templates`
- `backup/as3/json/bigip1.json` after generation

Generate:

```bash
ansible-playbook gen_as3.yml
ansible-playbook artifact_summary_playbook.yml
```

Generate only selected apps:

```bash
ansible-playbook gen_as3.yml \
  -e '{"tenants":{"partition_1":{"apps":["APP-http-simple","APP-dns"]}}}'
```

Dry run on BIG-IP:

```bash
ansible-playbook as3_dry_run_playbook.yml
```

Deploy:

```bash
ansible-playbook deploy_as3.yml
```

Cleanup:

```bash
ansible-playbook as3_cleanup_playbook.yml
```

Important behavior:

- The lab defaults AS3 `updateMode` to `selective`.
- Selective mode updates only declared tenants instead of removing tenants that
  are omitted from the declaration.
- The cleanup playbook removes the lab AS3 tenant listed in
  `as3_cleanup_tenants`.
