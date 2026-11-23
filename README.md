# Agent Orchestration Setup

Start Pi, DSH, Claude Code, Codex, or a plain terminal from one desktop window. Pi and DSH run independently. You do not need Claude Code or Codex to use them.

## Set up with Claude Code or Codex

The [EVREN](https://evren.ssyz.org.tr/) service is open to Turkish citizens and uses Türkiye’s e-Devlet identity verification ([university announcement](https://www.ktu.edu.tr/ofyazilim/duyuru/evren-platformu)). If you do not have EVREN access, choose **Pi only** and use NVIDIA instead.

Choose what to install, then expand **Claude Code** or **Codex** and copy the complete prompt into that tool's terminal. No coding agent installed? Use the [manual setup guide](docs/manuel-kurulum.md).

### Pi and DSH

<details>
<summary>Claude Code</summary>

```text
You are running in Claude Code on my computer. Help me set up Agent Orchestration Setup.
My choice is Pi and DSH. Verify Pi and both DSH entry points. Do not ask me to choose the tools again.
Read KURULUM-PROMPTU.md and the guide for my operating system in the official repository before running any installer:
https://github.com/OrcunSamiTandogan/agent-orchestration-setup
https://github.com/OrcunSamiTandogan/agent-orchestration-setup/blob/master/KURULUM-PROMPTU.md
Use normal permissions. Do not ask for, read, print, or test with my API keys. Show your plan before installing anything, and keep the normal approval prompts enabled. If a file or official download is unavailable, stop and report it.
```

</details>

<details>
<summary>Codex</summary>

```text
You are running in Codex on my computer. Help me set up Agent Orchestration Setup.
My choice is Pi and DSH. Verify Pi and both DSH entry points. Do not ask me to choose the tools again.
Read KURULUM-PROMPTU.md and the guide for my operating system in the official repository before running any installer:
https://github.com/OrcunSamiTandogan/agent-orchestration-setup
https://github.com/OrcunSamiTandogan/agent-orchestration-setup/blob/master/KURULUM-PROMPTU.md
Use normal permissions. Do not ask for, read, print, or test with my API keys. Show your plan before installing anything, and keep the normal approval prompts enabled. If a file or official download is unavailable, stop and report it.
```

</details>

### Pi only

<details>
<summary>Claude Code</summary>

```text
You are running in Claude Code on my computer. Help me set up Agent Orchestration Setup.
My choice is Pi only. Do not inspect, install, or configure DSH or EVREN. Do not ask me to choose the tools again.
Read KURULUM-PROMPTU.md and the guide for my operating system in the official repository before running any installer:
https://github.com/OrcunSamiTandogan/agent-orchestration-setup
https://github.com/OrcunSamiTandogan/agent-orchestration-setup/blob/master/KURULUM-PROMPTU.md
Use normal permissions. Do not ask for, read, print, or test with my API keys. Show your plan before installing anything, and keep the normal approval prompts enabled. If a file or official download is unavailable, stop and report it.
```

</details>

<details>
<summary>Codex</summary>

```text
You are running in Codex on my computer. Help me set up Agent Orchestration Setup.
My choice is Pi only. Do not inspect, install, or configure DSH or EVREN. Do not ask me to choose the tools again.
Read KURULUM-PROMPTU.md and the guide for my operating system in the official repository before running any installer:
https://github.com/OrcunSamiTandogan/agent-orchestration-setup
https://github.com/OrcunSamiTandogan/agent-orchestration-setup/blob/master/KURULUM-PROMPTU.md
Use normal permissions. Do not ask for, read, print, or test with my API keys. Show your plan before installing anything, and keep the normal approval prompts enabled. If a file or official download is unavailable, stop and report it.
```

</details>

### DSH only

<details>
<summary>Claude Code</summary>

```text
You are running in Claude Code on my computer. Help me set up Agent Orchestration Setup.
My choice is DSH only. Verify DSH CLI and DSH Web. Do not inspect, install, or configure Pi or NVIDIA. Do not ask me to choose the tools again.
Read KURULUM-PROMPTU.md and the guide for my operating system in the official repository before running any installer:
https://github.com/OrcunSamiTandogan/agent-orchestration-setup
https://github.com/OrcunSamiTandogan/agent-orchestration-setup/blob/master/KURULUM-PROMPTU.md
Use normal permissions. Do not ask for, read, print, or test with my API keys. Show your plan before installing anything, and keep the normal approval prompts enabled. If a file or official download is unavailable, stop and report it.
```

</details>

<details>
<summary>Codex</summary>

```text
You are running in Codex on my computer. Help me set up Agent Orchestration Setup.
My choice is DSH only. Verify DSH CLI and DSH Web. Do not inspect, install, or configure Pi or NVIDIA. Do not ask me to choose the tools again.
Read KURULUM-PROMPTU.md and the guide for my operating system in the official repository before running any installer:
https://github.com/OrcunSamiTandogan/agent-orchestration-setup
https://github.com/OrcunSamiTandogan/agent-orchestration-setup/blob/master/KURULUM-PROMPTU.md
Use normal permissions. Do not ask for, read, print, or test with my API keys. Show your plan before installing anything, and keep the normal approval prompts enabled. If a file or official download is unavailable, stop and report it.
```

</details>

## Download and install

[Download the source ZIP](https://github.com/OrcunSamiTandogan/agent-orchestration-setup/archive/refs/heads/master.zip). A GitHub account and a Git clone are not required.

| Platform | Guide | What has been verified |
|---|---|---|
| Ubuntu 24.04 | [Linux](docs/linux.md) | Source project: isolated installation and generated launcher. See [verification notes](docs/kalite.md) for setup-specific evidence. |
| macOS | [macOS](docs/macos.md) | Source-built app preview; Finder and desktop flow are not verified. |
| Windows | [Windows](docs/windows.md) | WSL 2 and WSLg preview. No native Windows executable; desktop flow is not verified. |

## Open your first session

| In the app | Use this local key field | Model used by this setup |
|---|---|---|
| **Pi** | **NVIDIA API key** | MiniMax M3.1 Flash by default; change with `/model`. |
| **DSH CLI** or **DSH Web** | **EVREN API key** | DeepSeek V4.1 Flash. |

1. Save only the key for the tool you chose, directly in the app's masked field. Do not paste keys into agent chats, commits, terminal commands, or project `.env` files.
2. Choose a trusted project folder for **Pi** or **DSH CLI**, then open that row. **DSH Web** opens the official browser UI and has no tmux session.
3. If prompted to install a missing tool, review the command and proceed with ordinary approvals. Pi requires Node.js 22.19+; DSH requires Node.js 24.9+. Check Node and npm in the app's own **Terminal**.
4. If you choose to make a live request after setup, start with `Reply with HELLO. Do not change any files.` This sends text to your provider and may use your account quota.

Already installed? **Verify with Claude** and **Verify with Codex** check first and report. They are not installers. Review changes before approving any repair.

[DSH details](docs/evren-dsh.md) · [FAQ](docs/sss.md) · [First Pi coding task](demo/GOREV.md) · [Contributing](CONTRIBUTING.md) · [Changes](CHANGELOG.md)

Already using the Turkish edition? Read the [shared installation and upstream note](UPSTREAM.md) before switching.

## Agensi companion

The free Agensi guide is separate from the desktop app and does not run an installer. [How to use the skill with Claude Code or Codex](docs/agensi.md) · [Skill source](agensi/SKILL.md) · [Paste-ready listing answers](agensi-answers.md)

## License and attribution

MIT; see [LICENSE](LICENSE) for the original copyright notice. This English derivative is based on [Ajan Atölyesi](https://github.com/OrcunSamiTandogan/ajan-atolyesi). Third-party tools and providers have their own terms and licenses.

Report setup issues with OS, app version, what failed, and sanitized output. Never attach credentials or unredacted logs. For vulnerabilities follow [the security policy](SECURITY.md).
