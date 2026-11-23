# DeepSeek Harness (DSH)

Both entry points use the official [DeepSeek Harness package](https://github.com/deepseek-ai/deepseek-harness/tree/master/apps/cli) and send model requests through EVREN to DeepSeek V4.1 Flash. DSH needs Node.js 24.9+ and npm. CLI also uses tmux. Save your EVREN key in the app's masked **EVREN API key** field. No NVIDIA key is required.

## Who can use this route?

The [EVREN](https://evren.ssyz.org.tr/) service is open to Turkish citizens and uses Türkiye’s e-Devlet identity verification ([university announcement](https://www.ktu.edu.tr/ofyazilim/duyuru/evren-platformu)). If you do not have EVREN access, choose **Pi only** and use NVIDIA instead. An EVREN API key is still needed for DSH.

## DSH CLI

Choose a trusted folder and open **DSH CLI**. The app starts the official `sdk-minimal` process in tmux session `aa-evren-cli` and shows its own **DSH >** prompt, not DeepSeek’s native TUI. Enter plain text there. `/new` starts a new DSH conversation, `/id` displays its ID, and `/exit` closes it. The DSH conversation ID is not the tmux target or a recovery code.

## DSH Web

Open **DSH Web** for the official browser interface. If needed, open a new session in **Default workspace**. The browser interface is local; do not share its session URL. It does not create a tmux session.

Both profiles in this project are text-only; they do not edit project files or provide web tools. Chat text goes to EVREN. Cache counters are provider-reported, not a guarantee of a hit or durable memory. A 401/403 usually calls for checking key/model access in your EVREN account; a 429 calls for checking your rate or quota before retrying.

A raw DeepSeek provider key is not an EVREN key. Do not put an EVREN key in `DEEPSEEK_API_KEY`.
