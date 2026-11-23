# Verification and platform status

The upstream Ajan Atölyesi Linux build was tested with an isolated Ubuntu installer, launch and embedded terminal. It also received private live provider smoke tests. Those results are upstream history, not release evidence for the English derivative or an independent model benchmark.

The English edition was checked on Ubuntu 24.04 in a fresh temporary home. The installed desktop entry, both English verification labels, the embedded GTK terminal, and the first-run flow passed. The first-run flow used mock CLI tools and keys. All 45 unit tests passed. No live model response was tested.

| Scope | What to verify |
|---|---|
| Ubuntu 24.04 | Fresh home, actual launcher and UI labels, embedded terminal, and independent Pi and DSH rows. Record observed results, not only checked files. |
| macOS preview | Clean source installation on a real Mac, Finder start, embedded terminal, selected tool. No prebuilt signed release. |
| Windows preview | Real Windows WSL 2/WSLg installer, second launch and embedded terminal. No native Windows build. |
| Providers | Checking a launcher is not a live model test. A live key should be entered by the owner in the masked app input, never by a contributor or into test logs. |

Prefer stub providers and throwaway sessions for routine tests; use no real keys in CI.
