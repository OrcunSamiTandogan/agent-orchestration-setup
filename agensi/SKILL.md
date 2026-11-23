---
name: agent-orchestration-setup
description: Build a personal setup plan for local coding agents with Claude Code or Codex. Choose Pi with NVIDIA, DSH with EVREN, or both, then get the official installation and first-task checklist.
version: 1.0.2
docs_url: https://github.com/OrcunSamiTandogan/agent-orchestration-setup#readme
---

# Agent Orchestration Setup

Help a beginner choose and verify a local Agent Orchestration Setup. This skill is a guided handoff, not an installer. It uses only the details the user shares in chat. Do not run commands, read local files, browse, install software or request credentials. Do not infer that anything on the user's machine has been verified.

1. Keep the user's facts. If needed, ask once for operating system, preferred tool (Pi, DSH, or both), and whether they want the desktop workshop or a plain terminal. Ask which installer assistant they use (Claude Code, Codex, or neither) only when they want the workshop.
2. Apply the relevant provider rules. Pi uses NVIDIA. The desktop workshop's DSH uses EVREN; standalone DSH in the manual example uses a direct DeepSeek API key, not EVREN. [EVREN](https://evren.ssyz.org.tr/) is open to Turkish citizens and uses e-Devlet verification ([university announcement](https://www.ktu.edu.tr/ofyazilim/duyuru/evren-platformu)). If a chosen route is blocked, explain the blocker and list only viable alternatives. Do not output install or verification steps for a blocked route, and do not switch the user's choice without asking. Do not request key values, government credentials, citizenship status, or ID. Do not promise free provider usage or quota.
3. Use exactly one of these paths:
   - **Plain terminal:** Link the [manual setup guide](https://github.com/OrcunSamiTandogan/agent-orchestration-setup/blob/master/docs/manuel-kurulum.md). Tell the user which section to follow, how to check the local CLI version, and how to try a one-line reply if they choose to use quota. Do not mention opening the workshop, an in-app report, a workshop key field or a Claude/Codex install prompt. Standalone key entry follows that tool's local authentication instructions.
   - **Desktop workshop:** Link the [English README](https://github.com/OrcunSamiTandogan/agent-orchestration-setup#readme). Send the user to **Pi only**, **DSH only**, or **Pi and DSH** and the matching Claude Code or Codex box, or to the manual/platform guide if they have neither local assistant. Keep normal approvals; the user enters the appropriate provider key in the masked app field. Verify the selected tool in the setup report and then open its session. A version or opened terminal is not proof of a model reply.
4. Ubuntu 24.04 is the reference Linux setup. The desktop app on macOS and Windows is a preview. For Windows, the local assistant and CLI tools must be inside Ubuntu on WSL 2, not in native PowerShell. The desktop app additionally needs WSLg. If a different OS is requested, state it is not covered.
5. Optional first exercise: for Pi, link the [two-test exercise](https://github.com/OrcunSamiTandogan/agent-orchestration-setup/blob/master/demo/GOREV.md) and distinguish expected from observed results. For the workshop's DSH route, use one short text reply; that route does not edit project files. Finish with one next step. Never claim that anything has been installed, verified or run unless the user provides that result.
