# First-run checklist

Start at the first step that fails. Keep your existing installation and sessions intact while checking.

| What you see | What to check next |
|---|---|
| The app opened in English | English is the default. Choose **Türkçe (TR)** under **Language / Dil** in the left sidebar. Reopen the app when convenient. The choice is saved and selecting it does not close running sessions. This changes the app interface, not the model or provider. |
| Not sure which path to choose | Pick **Pi only** if you have NVIDIA access and want file-editing agents. Pick **DSH only** if you have an EVREN API key and want this setup's text-only DSH sessions. Pick **Pi and DSH** only if you want both. No EVREN access? Use Pi if you can access NVIDIA; an account or provider quota is not guaranteed. |
| Claude Code or Codex cannot find the downloaded installer | Use the [GitHub source ZIP](https://github.com/OrcunSamiTandogan/agent-orchestration-setup/archive/refs/heads/master.zip), not the Agensi skill ZIP. Extract it before opening a terminal in that folder. If using an agent on Windows, start it inside the Ubuntu WSL 2 distro. |
| No desktop window | Follow the platform guide for [Ubuntu](linux.md), [macOS](macos.md), or [Windows/WSL](windows.md). The Windows app needs WSLg. On macOS and Windows the GUI flow is still a preview; do not disable desktop security features to make it launch. |
| Install Pi or Install DSH is blocked | In the app’s **Terminal**, run `node -v`, `npm -v`, and `tmux -V`. Pi needs Node 22.19+; DSH needs 24.9+. If Node or npm is missing or too old, follow the [official Node.js downloads](https://nodejs.org/en/download), choose a supported version that meets your route, reopen the app, and check its terminal again. A version available only in a login shell may not be on the app’s PATH. |
| npm reports `ENOSPC` | Free space on the filesystem holding the app profile and npm cache before trying again. On Ubuntu, the tested DSH package used about 1.3 GiB plus 227 MiB of npm cache; leave several GB free for dependencies and working files. This is a local installation error, not a provider problem. |
| The key says Saved but the model does not answer | **Saved** means the key was written locally, not that the provider accepted it. Check the matching provider account and model access. For 401/403 check key or model authorization; for 429 check quota or rate limits. Do not paste the key in a help request. |
| DSH CLI says it cannot verify the session | An older or unrelated tmux session may already use `aa-evren-cli`. The app does not attach to or close it automatically. Check it yourself; keep any work you still need before ending or renaming it, then retry. |
| Agensi cannot find the skill | The listing needs to be approved and published. Check the connected Agensi account and use the published name. If that still blocks you, the [GitHub route](../README.md#set-up-with-claude-code-or-codex) works without the marketplace. |
| Your first session opens | A shell opening does not prove a model is connected. If you choose to use provider quota, send a one-line reply request. Then try the [two-test Pi exercise](../demo/GOREV.md) or a short text-only DSH task. |

When asking for help, include your OS, selected route, app version, exact failed step and a sanitized error. Do not attach credentials, full environment dumps, or private session logs.
