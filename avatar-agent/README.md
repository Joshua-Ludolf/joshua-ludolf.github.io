# Synthesia Interactive Avatar Agent

This is a LiveKit Agent with Synthesia Interactive Avatar integration for Joshua Ludolf's portfolio.

## Setup

1. Install dependencies:
```bash
uv sync
# or
pip install -e .
```

2. Configure `.env` with your credentials:
```bash
# Copy .env.example to .env first, then replace the placeholder values.
LIVEKIT_URL=wss://your-project.livekit.cloud
LIVEKIT_API_KEY=your-livekit-api-key
LIVEKIT_API_SECRET=your-livekit-api-secret
SYNTHESIA_API_KEY=your-synthesia-api-key
OPENROUTER_API_KEY=your-openrouter-api-key
NVIDIA_API_KEY=your-nvidia-api-key
```

## Run

```bash
python agent.py dev
```

Then test in the **LiveKit Cloud Agent Console**:
1. Go to LiveKit Cloud dashboard → your project → Agents → Console
2. Select `synthesia-avatar-agent` from the dropdown
3. Click **Start session**
4. Speak to the avatar - it will lip-sync responses about Joshua Ludolf

## Notes

- The avatar uses Synthesia's "Kenji" avatar (ID: `7572faa9-15da-400d-8227-ef1ab8932523`)
- The agent uses OpenRouter (OpenAI-compatible) for response text and NVIDIA
  Magpie Multilingual for speech synthesis. Set `NVIDIA_TTS_LANGUAGE` and
  `NVIDIA_TTS_VOICE` to change the language or voice.
- The avatar joins as a regular LiveKit participant - any LiveKit frontend will render it
- Do NOT use `python agent.py console` for testing - the avatar won't appear in the terminal mock room