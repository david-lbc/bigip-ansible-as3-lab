# Rundeck Lab

Rundeck is the self-service catalog layer for this repo. The jobs call the
same playbooks you can run locally, which keeps the lab easy to inspect.

## Start Rundeck

```bash
docker compose up --build
```

Open:

```text
http://localhost:4440
```

The stock local login is `admin/admin`.

## Import Jobs

Create a project named `BIGIP-Lab`, then import:

```bash
docker compose exec rundeck bash -lc \
  'export RD_URL=http://localhost:4440 RD_USER=admin RD_PASSWORD=admin;
   rd projects create -p BIGIP-Lab || true;
   rd jobs load -p BIGIP-Lab -F yaml -f /home/rundeck/lab/rundeck/jobs/bigip-self-service-lab.yml'
```

You can also create the project and import
`rundeck/jobs/bigip-self-service-lab.yml` from the UI.

## Job Flow

Start with the readiness check:

1. `00 - Check Automation Toolchain readiness`

Run the base-config jobs first:

1. `01 - Check DO readiness`
2. `02 - Generate DO base config`
3. `03 - Deploy DO base config`

Then run AS3 app jobs:

1. `04 - Generate AS3 apps`
2. `05 - Review generated artifacts`
3. `06 - AS3 dry run`
4. `07 - Deploy AS3 apps`

Use the non-AS3 jobs for comparison:

1. `08 - Preview imperative app`
2. `09 - Deploy imperative app`

Cleanup jobs are available when you finish testing:

1. `10 - Cleanup AS3 lab tenants`
2. `11 - Cleanup imperative app`

## Options

Most jobs include `limit`, which maps to an Ansible inventory host or group.

The AS3 generate job includes `as3_apps`, a comma-separated list such as:

```text
APP-http-simple,APP-dns
```

The job converts that into Ansible extra vars with
`scripts/as3_apps_extra_vars.py`, overriding the tenant app list for that run.
The `as3_tenant` option defaults to `partition_1`.

## Notes

- Keep secrets out of job definitions. Use environment variables, Rundeck key
  storage, or a vault workflow for anything beyond the local `admin/admin` lab.
- Rundeck is not replacing Ansible or AS3 here. It is a friendlier front door
  for running the same automation paths.
- If the DO extension is not installed on the BIG-IP, the DO readiness/deploy
  jobs will fail until the extension is added.

## Rundeck Key Storage

For the quick lab, the mounted repo inventory defaults to `admin/admin`.

For shared demos, store the password in Rundeck key storage and inject it as
`BIGIP_ADMIN_PASSWORD` for job execution. One simple pattern is:

1. Store the password at a key path such as
   `keys/project/BIGIP-Lab/bigip-admin-password`.
2. Add a secure job option named `bigip_password`.
3. Prefix the job command with
   `BIGIP_ADMIN_PASSWORD='${option.bigip_password}'`.

That keeps the playbooks unchanged while moving the secret out of the repo.
