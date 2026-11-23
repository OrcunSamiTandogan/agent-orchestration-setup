# Ubuntu 24.04

1. [Download the source ZIP](https://github.com/OrcunSamiTandogan/agent-orchestration-setup/archive/refs/heads/master.zip), extract it, and open a terminal in the extracted folder.
2. After reviewing the packages and approving any administrator prompt, install the GTK/VTE and tmux prerequisites:

   ```bash
   sudo apt update
   sudo apt install python3-gi gir1.2-gtk-3.0 gir1.2-vte-2.91 tmux
   ```

3. Run `bash masaustune-kur.sh`. Open **Agent Orchestration Setup** from your application menu or the desktop shortcut. If your desktop offers **Allow Launching** for this shortcut, verify its source before using it.
4. In the app's **Terminal**, run `node -v` and `npm -v`. Pi needs Node 22.19+; DSH needs 24.9+.

[Open your first session](../README.md#open-your-first-session) · [Troubleshooting](sss.md)
