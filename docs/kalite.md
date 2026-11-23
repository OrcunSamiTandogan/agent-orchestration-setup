# Verification and platform status

The upstream Ajan Atölyesi Linux build was tested with an isolated Ubuntu installer, launch and embedded terminal. It also received private live provider smoke tests. Those results are upstream history, not release evidence for the English derivative or an independent model benchmark.

The English edition was checked on Ubuntu 24.04 in a fresh temporary home. The installed desktop entry, both English verification labels, the embedded GTK terminal, and the first-run flow passed. The first-run flow used mock CLI tools and keys. All 49 unit tests passed. The registry installs of Pi 1.6.0 and DSH 0.2.2-rc.5 were separately verified in temporary profiles with version checks. The sample exercise was verified to start with one failing test and pass both after the intended change. No live model response was tested.

| Scope | What to verify |
|---|---|
| Ubuntu 24.04 | Fresh home, actual launcher and UI labels, embedded terminal, and independent Pi and DSH rows. Record observed results, not only checked files. |
| macOS preview | Clean source installation on a real Mac, Finder start, embedded terminal, selected tool. No prebuilt signed release. |
| Windows preview | Real Windows WSL 2/WSLg installer, second launch and embedded terminal. No native Windows build. |
| Providers | Checking a launcher is not a live model test. A live key should be entered by the owner in the masked app input, never by a contributor or into test logs. |

Prefer stub providers and throwaway sessions for routine tests; use no real keys in CI.

## Local skill test

The exact ZIP content was loaded natively in temporary projects using Claude Code 2.1.330 and Codex CLI 0.171.0, without Agensi or app installation. Claude Code recognized the skill and returned a blocked desktop DSH route when EVREN was unavailable; Codex returned a Pi-only terminal route without asking for the desktop app. An earlier run also routed Windows desktop setup to Ubuntu/WSL 2 rather than PowerShell. These are local skill behavior checks on Ubuntu, not platform installations or an Agensi MCP test.

## Improvements to tackle next

1. **Complete the real Agensi journey after approval.** Connect one clean user profile, load the free listing by name, and verify the returned route and next step. Repeat with the other assistant separately. Documentation and local prompt rehearsals are not a live marketplace test.
2. **Run native clean-install tests on macOS and Windows/WSL.** Cover the first launch, Finder/WSLg, dependency visibility in the embedded terminal, and a second launch. Keep both marked as previews until verified.
3. **Add an in-app readiness summary.** Show Node, npm, and tmux availability in the app’s own environment and distinguish “key saved”, “session opened”, and “provider answered”. Keep live tests opt-in because they can consume quota.
4. **Ship versioned tutorial downloads.** Keep a tested source snapshot and its checksum together with the matching guide; the README's master ZIP follows the latest code. Keep Turkish and English runtime changes in sync from their shared upstream.

## Keep the first lesson small

Use one lesson structure on Anladene (Turkish) and Try2Learn (English): choose one route, run one tiny task, verify the outcome. Start with standalone Pi and the two-test exercise; use a one-line response for the DSH text route. Offer the desktop app and multi-session coordination as optional next steps, not prerequisites. Reuse the same exercise and verification checklist, not two separate implementations.
