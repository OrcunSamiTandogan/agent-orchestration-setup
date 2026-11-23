# Agensi submission: Agent Orchestration Setup

Copy only the content inside each block into the matching Agensi field. This listing is the free **setup guide skill**; the complete desktop application and its installer remain on GitHub. The skill does not execute the setup and the marketplace ZIP does not contain the desktop application.

## 1. Skill ZIP Upload and Agensi tools

- Upload [agent-orchestration-setup-skill.zip](agensi/agent-orchestration-setup-skill.zip).
- It contains one file, [SKILL.md](agensi/SKILL.md), at its root. Do not upload the GitHub source ZIP here.
- Leave **Agensi tools** empty. No paid tool or add-on is required by the skill.

## 2. Skill Details

**Skill logo:** Upload [skill-logo.png](agensi/skill-logo.png), the 512 × 512 PNG.

### Skill Name

```text
Agent Orchestration Setup
```

### Summary

```text
Set up your first local coding-agent workspace. Pick Pi with NVIDIA, DSH with EVREN, or both. Get the right Claude Code or Codex install prompt and a short checklist to verify your first task.
```

### Full Description

````markdown
## Get your first local coding agents working

Agent Orchestration Setup helps you choose a route and turn it into a checklist you can follow. Tell it which operating system you use, whether you already use Claude Code or Codex, and what you want to set up: Pi, DSH, or both.

### What you get

- A setup plan for your operating system and chosen route.
- The matching copyable prompt for Claude Code or Codex in the [English GitHub guide](https://github.com/OrcunSamiTandogan/agent-orchestration-setup#readme).
- A checklist to open the workshop, start the selected session, and verify what actually works.
- For Pi, a [small coding exercise](https://github.com/OrcunSamiTandogan/agent-orchestration-setup/blob/master/demo/GOREV.md) with two tests you can run yourself; for DSH, a text-response check.

### Before you start

The free skill provides instructions. It does not read your files, take your API keys, or install software. An approved install runs separately on your computer. Pi uses an NVIDIA key; DSH uses an EVREN key. Enter your key in the local app, not in an agent chat. Provider limits and charges are separate from the free skill.

Ubuntu 24.04 is the reference Linux setup. macOS and Windows via WSL2 are preview routes. The desktop app and instructions are available directly from GitHub under the MIT license; Agensi is optional.
````

## 3. See it in action (demo)

### The request (what the buyer types)

```text
I’m on Ubuntu 24.04. I already use Codex CLI and have an NVIDIA key. I only want Pi. Give me a setup plan and show me how to check that it worked. Do not run or install anything.
```

### The result (what your agent delivers)

This is the complete reply from a local rehearsal of the guide instructions. It is not a recording of the Agensi MCP and does not claim an installation or a provider call.

```markdown
**Your setup: Ubuntu 24.04 → Codex CLI → Pi only → NVIDIA.** Ubuntu 24.04 is the reference Linux setup. Codex helps with installation; Pi uses your existing NVIDIA key.

1. Open the [English README](https://github.com/OrcunSamiTandogan/agent-orchestration-setup#readme), expand **Pi only**, and select the **Codex** box beneath it.
2. Copy the entire prompt and paste it into Codex CLI running in a terminal on your computer. Keep normal tool permissions and review any installation prompts. When asked for your NVIDIA key, enter it locally in the app, never in chat.

**Check that it worked:**
- Open the workshop and read the setup report. Only Pi should be checked. Note whether it says installed, already present, skipped, or blocked.
- Launch Pi and send a short test message. A reply checks the NVIDIA connection separately; an installed status doesn’t prove the connection works.
- Try the [slug exercise](https://github.com/OrcunSamiTandogan/agent-orchestration-setup/blob/master/demo/GOREV.md). Look for two passing tests: one for normal slug formatting and one for converting Turkish characters.

I haven’t run or installed anything.
```

## 4. Compatibility

### Compatibility Note

```text
The skill generates a setup plan in a compatible agent. The separate local installer is guided through Claude Code or Codex CLI. Ubuntu 24.04 is the reference platform. macOS and Windows via WSL2 are previews; there is no native Windows app.
```

## 5. Pricing

Select **Free**, not **One-time** or **Subscription**. A model provider's quota or billing is separate.

## Tags, Categories, Usecases

- **Category:** Agents & Orchestration.
- **Tags:** `agent-orchestration`, `claude-code`, `codex-cli`, `pi`, `deepseek-harness`, `tmux`.
- **Use cases** (one item each):

```text
Choose a local coding-agent setup for Ubuntu, macOS, or Windows via WSL2
Get the correct copyable setup prompt for Claude Code or Codex CLI
Verify your first local agent session and complete a small coding exercise
```

## Permissions

These settings describe the **Agensi guide skill**, not the separate local installation.

| Field | Value |
|---|---|
| Requires | Leave empty. The guide collects setup choices in chat only. |
| Optional | `Local Claude Code or Codex CLI for the separate installation` |
| Nothing to install | Check for this guide skill only. The desktop workshop is a separate install. |
| Tools Used | Leave all boxes unchecked. The guide neither runs commands nor opens links or files itself. |
| Needs access to | Leave empty. No connected service or provider key is used by the guide. |
| Other tool | Leave blank. |
| File Scopes | Leave blank. |

### Note for buyers

```text
This skill produces a plan, not an install. Continue in your own terminal using the linked README. Enter provider keys only in the local app. You can use the open-source GitHub project without Agensi.
```

### Notes

```text
No tool access is needed by the Agensi skill. If you later approve an installation in your local coding agent, that separate process may need terminal, network, and file access. Pi and DSH credentials are configured outside this skill.
```

## Extra Details

If the optional section offers matching fields, use the following. Otherwise keep it empty rather than repeat the full description.

| Suggested field | Copyable value |
|---|---|
| Output | Platform-specific setup plan, a matching install prompt link, and a short first-task checklist. |
| Inputs | Operating system, Claude Code or Codex, and Pi, DSH, or both. No API keys. |
| Version | 1.0.0 (guide skill, not desktop application version). |
| Source / repository | https://github.com/OrcunSamiTandogan/agent-orchestration-setup |
| License | MIT. |

## FAQ

### What does Agent Orchestration Setup do?

```text
It helps you pick Pi, DSH, or both, find the correct setup prompt for your assistant, and confirm what is ready before trying your first coding task. It does not install software by itself.
```

### Which AI agents support Agent Orchestration Setup?

```text
The Agensi guide can be loaded by a compatible agent. The repository documents the actual local install with Claude Code and Codex CLI, with separate copyable prompts for each.
```

### How do I use Agent Orchestration Setup?

```text
Tell the guide your operating system, the local assistant you use, and your preferred route. Open the linked English README, copy the matching prompt into your local terminal assistant, and review each proposed installation step. Follow the verification checklist before a real task.
```

### Do I have to pay or share an API key?

```text
No for the guide. The workshop is open source. Pi uses your NVIDIA account, and DSH uses your EVREN account; provider terms and quotas still apply. Never put a provider key in Agensi, an agent chat, or a screenshot.
```

## Screenshots and Demo video URL

- **Screenshots:** Upload [english-first-run.png](agensi/english-first-run.png) as the first image. It shows the installed English app in a clean test profile with no keys or personal data. The original screenshots of the Agensi form are reference material, not listing images.
- **Demo video URL:** Leave blank until a public video actually shows this English setup. Do not enter a local video path or an unpublished URL.

## Documentation Link

```text
https://github.com/OrcunSamiTandogan/agent-orchestration-setup#readme
```

Check the preview and the declared permissions, then choose **Submit for review** yourself. No submission or publication to Agensi is implied by this file.

[Agensi packaging requirements](https://www.agensi.io/docs/packaging) · [Website submission guide](https://www.agensi.io/docs/submit-on-the-website)
