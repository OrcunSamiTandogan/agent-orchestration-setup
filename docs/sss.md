# Frequently asked questions

**Do I need to install both?** No. Use Pi only, DSH only, or both. Pi uses NVIDIA; DSH uses EVREN. Those are separate provider keys.

**Do I need Claude Code or Codex?** No. They can help set up or check the app if already installed; [manual setup](manuel-kurulum.md) is equally valid.

**Can I paste my key into the setup prompt?** No. Use only the masked local input. Do not share the app’s credentials file or an unredacted log.

**Why is my installed tool missing in the app?** Check its version and PATH in the app’s **Terminal**, not only your login shell. Pi requires Node.js 22.19+; DSH requires 24.9+. Check npm and tmux where applicable before reinstalling anything.

**What’s the difference between DSH CLI and Web?** The former is a tmux-backed terminal tied to the SDK; the latter uses the official DeepSeek browser interface. See [DSH](evren-dsh.md).

**What if the provider is slow or unavailable?** Check your provider’s access and quota before altering the installation. In Pi, `/model` lets you choose a different NVIDIA model. DSH uses DeepSeek V4.1 Flash and does not fall back silently.

**Did you test macOS and Windows?** They are previews. See [what was verified](kalite.md).
