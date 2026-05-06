# 04 - Rundeck Self-Service Catalog

Goal: run the lab through Rundeck Open Source jobs.

Start:

```bash
docker compose up --build
```

Open:

```text
http://localhost:4440
```

Import jobs:

```bash
docker compose exec rundeck bash -lc \
  'export RD_URL=http://localhost:4440 RD_USER=admin RD_PASSWORD=admin;
   rd projects create -p BIGIP-Lab || true;
   rd jobs load -p BIGIP-Lab -F yaml -f /home/rundeck/lab/rundeck/jobs/bigip-self-service-lab.yml'
```

Suggested order:

1. `00 - Check Automation Toolchain readiness`
2. `02 - Generate DO base config`
3. `03 - Deploy DO base config`
4. `04 - Generate AS3 apps`
5. `05 - Review generated artifacts`
6. `06 - AS3 dry run`
7. `07 - Deploy AS3 apps`
8. `08 - Preview imperative app`
9. `09 - Deploy imperative app`
10. Cleanup jobs when finished

Credential reminder:

- `admin/admin` is only for the local lab.
- Use environment variables, Rundeck key storage, or vault-backed secrets for
  anything shared.
