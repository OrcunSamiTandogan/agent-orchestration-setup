# macOS preview

This source installer builds a GTK `.app` on the Mac. It is not a downloaded signed or notarized build. Installation, Finder launch, and the embedded terminal have not been verified on a real Mac.

1. Set up [Homebrew](https://brew.sh/) using its official instructions, including the PATH step.
2. Install dependencies: `brew install gtk+3 vte3 pygobject3 tmux`.
3. [Download the source ZIP](https://github.com/OrcunSamiTandogan/agent-orchestration-setup/archive/refs/heads/master.zip), extract it, and run `bash kur-macos.sh` in the extracted folder.
4. In Finder, use **Go → Go to Folder** (⇧⌘G), enter `~/Applications`, and open **Ajan Atölyesi / Agent Workshop**. This is your user Applications folder, not the system folder. The installer currently keeps the legacy on-disk filename: `open "$HOME/Applications/Ajan Atölyesi.app"` is the equivalent Terminal command.

Use the app’s **Terminal** to check `node -v` and `npm -v`. Node installations available only through a shell initialization script may not be visible when launched from Finder. If macOS shows a security warning, verify the source and follow [Apple’s guidance](https://support.apple.com/en-us/102445). Do not disable Gatekeeper.

[Open your first session](../README.md#open-your-first-session)
