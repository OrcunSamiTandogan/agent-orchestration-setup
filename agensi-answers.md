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

The [EVREN](https://evren.ssyz.org.tr/) service is open to Turkish citizens and uses Türkiye’s e-Devlet identity verification ([university announcement](https://www.ktu.edu.tr/ofyazilim/duyuru/evren-platformu)). If you do not have EVREN access, choose **Pi only** and use NVIDIA instead.

Ubuntu 24.04 is the reference Linux setup. macOS and Windows via WSL2 are preview routes. The desktop app and instructions are available directly from GitHub under the MIT license; Agensi is optional. You can also follow the [terminal-only guide](https://github.com/OrcunSamiTandogan/agent-orchestration-setup/blob/master/docs/manuel-kurulum.md) and start with only Pi or standalone DSH. Standalone DSH uses a direct DeepSeek key in that example.
````

## 3. See it in action (demo)

### The request (what the buyer types)

```text
On Ubuntu 24.04, I have NVIDIA access and want to learn Pi in a plain terminal. I do not have Claude Code or Codex installed on that target computer. Tell me where to start, without installing, running or changing anything.
```

### The result (what your agent delivers)

Actual output from a Codex CLI session using the same project-local skill as the upload ZIP. This is a planning demonstration, not a recording of Agensi delivery, an installation, or a provider call.

```markdown
Use the **Pi with NVIDIA** section of the manual setup guide. Ubuntu 24.04 is the reference Linux setup, and Pi runs directly in a plain terminal without Claude Code or Codex. Follow Pi’s local authentication instructions for your NVIDIA access. [Manual setup guide](https://github.com/OrcunSamiTandogan/agent-orchestration-setup/blob/master/docs/manuel-kurulum.md)

When you’re ready to try it later, `pi --version` checks the local CLI. For an optional model check that may use NVIDIA quota, run `pi -p "Reply with exactly one line: Hello from Pi."` A version number confirms the CLI responds. A model reply confirms the provider request worked.

For now, open the manual guide and read the Pi with NVIDIA section.
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
| Version | 1.0.2 (guide skill, not desktop application version). |
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
Connect Claude Code or Codex CLI to Agensi with MCP, then select Use this skill or ask for Agent Orchestration Setup by name. Tell it your operating system and preferred route. The guide points you to the matching local installation prompt. Start here: https://github.com/OrcunSamiTandogan/agent-orchestration-setup/blob/master/docs/agensi.md
```

### Do I have to pay or share an API key?

```text
No for the guide. The workshop is open source. Pi uses your NVIDIA account, and DSH uses your EVREN account; provider terms and quotas still apply. Never put a provider key in Agensi, an agent chat, or a screenshot.
```

### Who can use the EVREN route?

```text
EVREN is open to Turkish citizens and uses Türkiye’s e-Devlet identity verification. You need an EVREN API key for DSH. If you do not have EVREN access, choose Pi only and use an NVIDIA account.
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
