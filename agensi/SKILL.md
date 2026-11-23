---
name: agent-orchestration-setup
description: Build a personal setup plan for local coding agents with Claude Code or Codex. Choose Pi with NVIDIA, DSH with EVREN, or both, then get the official installation and first-task checklist.
version: 1.0.1
docs_url: https://github.com/OrcunSamiTandogan/agent-orchestration-setup#readme
---

# Agent Orchestration Setup

Help a beginner choose and verify a local Agent Orchestration Setup. This skill is a guided handoff, not an installer. It uses only the details the user shares in chat. Do not run commands, read local files, browse, install software or request credentials. Do not infer that anything on the user's machine has been verified.

1. If missing, ask in one question for the operating system (Ubuntu, macOS, or Windows), the installer assistant they already use (Claude Code or Codex), and the desired path (Pi, DSH, or both). Don't ask again about choices they gave.
2. Explain only the path they chose. Pi uses an NVIDIA key; DSH uses an EVREN key. An existing Claude Code or Codex session is the installation assistant, not the model account for Pi or DSH. If they select DSH, say that [EVREN](https://evren.ssyz.org.tr/) is open to Turkish citizens and uses e-Devlet verification ([university announcement](https://www.ktu.edu.tr/ofyazilim/duyuru/evren-platformu)). If they do not have EVREN access, recommend Pi only with an NVIDIA account instead. Do not ask for citizenship status, government credentials or ID. Only say a key is ready if the user says so. Don't ask for the key value.
3. Link to the [English README](https://github.com/OrcunSamiTandogan/agent-orchestration-setup#readme). Tell them to expand **Pi only**, **DSH only** or **Pi and DSH** as applicable, choose the **Claude Code** or **Codex** box beneath that heading, and paste the entire prompt into the matching assistant running in a terminal on their own computer. Keep normal tool permissions and review installation prompts. The user enters the matching provider key locally in the app, never in chat.
4. State support honestly: Ubuntu 24.04 is the reference Linux setup; macOS and Windows via WSL2 are preview routes. If the user has another operating system, say it is not covered here.
5. Provide a compact checklist: open the workshop, see only the path(s) selected for setup reported as checked, launch the selected provider's session, and report installed, already present, skipped or blocked. Separate setup checks from provider responses. For Pi, link the [slug exercise](https://github.com/OrcunSamiTandogan/agent-orchestration-setup/blob/master/demo/GOREV.md) and describe the two expected passing tests. For DSH, suggest a one-line text reply first; this DSH terminal does not edit files. Never claim a test passed unless the user provided that result.

Return a short plan with the selected path, README section, verification checklist and next step. Do not promise free provider usage, higher quotas, or access to another agent's native team features.
