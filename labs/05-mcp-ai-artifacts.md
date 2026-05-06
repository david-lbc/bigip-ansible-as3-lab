# 05 - MCP and AI Artifact Exercises

Goal: use generated artifacts and typed MCP tools as learning aids.

Good prompts to test with the generated files:

- Explain the generated DO declaration in `backup/do/json/bigip1.json`.
- Summarize the tenants and apps in `backup/as3/json/bigip1.json`.
- Compare `backup/as3/json/bigip1.json` with `backup/imperative/bigip1.yml`.
- Identify which BIG-IP objects should appear after the AS3 deploy.
- Explain how to clean up the AS3 and imperative examples.

Good typed MCP exercise ideas:

- Check AS3 readiness before running AS3 jobs.
- Export a live lab virtual server chain as AS3.
- Use QKView facts to confirm software version and provisioned modules.
- Analyze a pcap for traffic to one lab virtual server.

Layer boundary:

- MCP tools should expose typed BIG-IP capabilities.
- This lab owns sequencing, examples, and learning flow.
