# Use the Agensi guide skill

The **Agent Orchestration Setup** guide is free. Agensi delivers it through its MCP connection rather than as a ZIP for learners to install. The ZIP in this repository is for creators submitting the listing. The [open-source desktop app and all six setup prompts](../README.md#set-up-with-claude-code-or-codex) work independently of Agensi.

## Option A: Use the guide on Agensi

Once the listing is published, sign in to [Agensi](https://www.agensi.io/) and connect **one** terminal assistant using the instructions below. As of the current [Agensi connection guide](https://www.agensi.io/docs/mcp-setup), connecting another app with the same account disconnects the existing one. These are optional configuration steps you run yourself; the desktop installer does not connect Agensi.

### Claude Code

From a normal local terminal:

```bash
claude mcp add --transport http agensi https://mcp.agensi.io/mcp/auth
```

Open Claude Code, run `/mcp`, choose **agensi**, then **Authenticate**. Complete sign-in in the browser with your Agensi account.

### Codex CLI

From a normal local terminal:

```bash
codex mcp add agensi --url https://mcp.agensi.io/mcp/auth
codex mcp login agensi
```

Complete sign-in in the browser and open Codex CLI. Do not paste an Agensi, NVIDIA, or EVREN token into the chat for this step. Read the browser authorization screen before you grant access. Agensi offers paid tools elsewhere, but this guide does not need them or any purchase.

### Run the guide

Find **Agent Orchestration Setup** on Agensi and select **Use this skill**, or paste this into the assistant you connected. Edit the operating system, assistant and route to match your computer:

```text
Use the free Agensi skill "Agent Orchestration Setup". I use Ubuntu 24.04 and Codex CLI, and I want Pi only. Give me the correct setup prompt and a verification checklist. Do not install or run anything.
```

If the assistant cannot find the listing, check whether it has been approved and published, confirm the right account is connected, or use Option B. The guide does not install software. It tells you which installer prompt to copy, where to paste it, and what to verify. See [Agensi's skill-use guide](https://www.agensi.io/docs/use-a-skill).

## Option B: Skip Agensi and use GitHub

1. Open the [English README](../README.md#set-up-with-claude-code-or-codex). Choose **Pi only**, **DSH only**, or **Pi and DSH**. Pick the Claude Code or Codex prompt under that heading and paste it into the corresponding local terminal assistant. If neither is installed, use the [manual setup guide](manuel-kurulum.md).
2. Review installation steps using normal permissions. Open the desktop app and save the matching key in its masked field. Pi uses NVIDIA; DSH uses [EVREN](evren-dsh.md), which is open to Turkish citizens and uses e-Devlet identity verification. If EVREN is not available to you, choose Pi with an NVIDIA account.
3. Open the selected session. If you want to test provider connectivity, send a short text request; this may use provider quota. For Pi, try the [first coding exercise](../demo/GOREV.md). DSH in this setup is text-only, so use a simple text response as its first check.

Ubuntu 24.04 is the reference platform. macOS and Windows via WSL2 are preview routes. Agensi sign-in, an app install, and a live model response are three separate checks.
