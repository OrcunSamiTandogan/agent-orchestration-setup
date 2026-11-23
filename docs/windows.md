# Windows preview (WSL 2)

This route runs the Linux GTK app using Ubuntu 24.04, WSL 2, and WSLg. It is not a native Windows executable. Real Windows installation and launch are not yet verified. See [Microsoft’s WSLg guide](https://learn.microsoft.com/windows/wsl/tutorials/gui-apps).

1. In administrator PowerShell, after approving this system change, run `wsl --install -d Ubuntu-24.04`. Reboot if Windows asks. Open Ubuntu once and create its Linux user account. Check with `wsl -l -v`: `Ubuntu-24.04` should be version 2.
2. In the Ubuntu terminal, review and install the prerequisites:

   ```bash
   sudo apt update
   sudo apt install python3-gi gir1.2-gtk-3.0 gir1.2-vte-2.91 tmux
   ```

3. [Download the source ZIP](https://github.com/OrcunSamiTandogan/agent-orchestration-setup/archive/refs/heads/master.zip), extract it into a local Windows folder, and open `kur-windows.cmd`. It attempts to start the GUI after installation.
4. On future launches, use `ac-windows.cmd` in the extracted folder. Start menu integration is not required. Install any chosen CLI tools inside Ubuntu, not Windows.

[Open your first session](../README.md#open-your-first-session)
