# Manual setup

You do not need Claude Code or Codex. Pick **Pi and DSH**, **Pi only**, or **DSH only**, and skip the other sections. Start from the [platform-specific installer](../README.md#download-and-install) if you want the desktop app. When using the app, the tools can be installed from their respective rows and keys belong only in its masked local fields.

## Pi from a terminal

Install Pi from the [official quickstart](https://docs.pi.dev/latest/quickstart). Use Node.js 22.19+ for Pi, then confirm `pi --version`. Launch `pi`, select NVIDIA NIM through `/login`, and enter the key in Pi’s local key input, not the conversation. Use `/model` to choose a model. If you want a persistent terminal, start `tmux new-session -A -s aos-pi-manual` before launching Pi; press Ctrl+B then D to detach without ending the session.

## DSH from a terminal

Use Node.js 24.9+ and npm. Check the [official DeepSeek Harness package](https://github.com/deepseek-ai/deepseek-harness/tree/master/apps/cli) and the pinned version before installing. Do not run global npm installs with sudo.

```bash
npm install -g @deepseek-ai/dsh@0.2.2-rc.5
dsh --version
```

Standalone dsh's direct DeepSeek provider needs a DeepSeek key, not an EVREN key. For **DSH via EVREN**, use this project's [DSH CLI or DSH Web](evren-dsh.md) after installing the [source ZIP](https://github.com/OrcunSamiTandogan/agent-orchestration-setup/archive/refs/heads/master.zip). The CLI has an independent tmux terminal; the Web option uses the official browser UI.

Never paste keys into agent prompts, source files, screenshots, commits, or visible shell commands.
