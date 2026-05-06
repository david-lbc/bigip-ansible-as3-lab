# MCP and AI Exercises

This repo can be a good place to show AI-assisted BIG-IP work, but the layer
boundary matters.

The MCP server should expose typed BIG-IP primitives. This lab should compose
those primitives into demos, explanations, or Rundeck-hosted exercises.

## Good MCP Fits

- Detect whether AS3 is installed and ready.
- Validate or render typed AS3 declarations.
- Export a live virtual server chain as AS3 for migration learning.
- Read typed system/base config state before a DO lesson.
- Transfer and inspect QKView artifacts for troubleshooting.
- Analyze pcaps for a VIP/pool troubleshooting exercise.

## Avoid

- A single MCP command that runs this whole lab.
- Raw iControl REST passthrough as a substitute for missing typed tools.
- Prompt/prose parsing that decides which BIG-IP mutation to run.
- Lab-specific environment assumptions inside the MCP server.

## Suggested Exercises

1. Ask the AI to explain the rendered DO declaration in `backup/do/json`.
2. Ask the AI to compare an AS3 app declaration with the non-AS3 module preview.
3. Use AS3 export tooling to reverse-engineer a live lab VIP into a declaration.
4. Use QKView analysis to identify current BIG-IP version/modules before
   picking an exercise.
5. Use pcap analysis to debug traffic for one deployed VIP.
6. Use the artifact summary output to decide which generated declaration should
   be reviewed before deploy.
7. Ask for cleanup guidance based only on the generated AS3 and imperative
   artifacts.

## Tracking

Typed Declarative Onboarding support for `cute-bigip-mcp` is tracked here:

https://gitlab.thelbc.io/cute-pm/cute-bigip-mcp/-/work_items/297
