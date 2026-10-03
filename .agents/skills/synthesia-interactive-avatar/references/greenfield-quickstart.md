# Greenfield Quickstart — Synthesia Interactive Avatar

Use this when the user has **no existing LiveKit Agent**. Output: a runnable Python agent with the avatar attached, plus a working frontend to see it in.

## Prerequisites — gather before writing code

1. **Synthesia API key** from a workspace with Interactive Avatar access (from the [Synthesia developer console](https://docs.synthesia.io/reference/synthesia-api-quickstart)). Keys without access are rejected — confirm this exists first.
2. **LiveKit credentials**: `LIVEKIT_URL`, `LIVEKIT_API_KEY`, `LIVEKIT_API_SECRET`. Easiest source is a free LiveKit Cloud project; self-hosted works too.
3. **Model provider key(s)**:
   - Default path: an **OpenAI API key** with Realtime access.
   - Pipeline path: keys for whichever STT / LLM / TTS providers the user chose.
4. **Python 3.10+.**

## Project setup

```bash
mkdir avatar-agent && cd avatar-agent
uv init && uv add "livekit-agents[openai,silero]~=1.8" "livekit-plugins-synthesia~=1.8" python-dotenv
```

pip equivalent: `pip install "livekit-agents[openai,silero]~=1.8" "livekit-plugins-synthesia~=1.8" python-dotenv`

`.env` (never commit; load via a secret manager in production):

```bash
LIVEKIT_URL=wss://<project>.livekit.cloud
LIVEKIT_API_KEY=...
LIVEKIT_API_SECRET=...
SYNTHESIA_API_KEY=...
OPENAI_API_KEY=...
```

## Pick the voice to match the avatar

`voice="alloy"` in the templates below is a placeholder. Set the model's speaking voice to one whose perceived persona fits the chosen avatar — don't ship a mismatched default — and confirm the choice with the user. Voice lists: [OpenAI Realtime](https://platform.openai.com/docs/guides/realtime) for Variant A; the TTS provider's docs (e.g. [OpenAI TTS](https://platform.openai.com/docs/guides/text-to-speech)) for Variant B.

## Agent — Variant A: OpenAI Realtime (default)

Fewest moving parts: one model handles VAD, STT, LLM and TTS internally. Use unless the user lacks Realtime access or wants specific providers.

```python
# agent.py
from dotenv import load_dotenv
from livekit.agents import Agent, AgentSession, JobContext, WorkerOptions, cli
from livekit.plugins import openai, synthesia

load_dotenv()


async def entrypoint(ctx: JobContext):
    await ctx.connect()

    session = AgentSession(
        llm=openai.realtime.RealtimeModel(voice="alloy"),
    )

    # Attach the avatar BEFORE session.start() — order matters.
    avatar = synthesia.AvatarSession(
        synthesia.AvatarConfig(avatar_ids=["7572faa9-15da-400d-8227-ef1ab8932523"]),  # Kenji
    )
    await avatar.start(session, room=ctx.room)

    await session.start(
        agent=Agent(
            instructions=(
                "You are a friendly product assistant. Speak English unless the user "
                "speaks to you in another language — then match their language."
            )
        ),
        room=ctx.room,
    )

    await session.generate_reply(instructions="Greet the user briefly, in English.")


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, agent_name="synthesia-avatar-agent"))
```

## Agent — Variant B: Component pipeline

Only if the user wants explicit provider control (or has no Realtime access). Same avatar code — the component intercepts the agent's audio output regardless of providers.

```python
# agent.py
from dotenv import load_dotenv
from livekit.agents import Agent, AgentSession, JobContext, WorkerOptions, cli
from livekit.plugins import openai, silero, synthesia

load_dotenv()


async def entrypoint(ctx: JobContext):
    await ctx.connect()

    session = AgentSession(
        stt=openai.STT(model="gpt-4o-mini-transcribe", language="en"),
        llm=openai.LLM(model="gpt-4o-mini"),
        tts=openai.TTS(voice="alloy"),
        vad=silero.VAD.load(),
    )

    avatar = synthesia.AvatarSession(
        synthesia.AvatarConfig(avatar_ids=["7572faa9-15da-400d-8227-ef1ab8932523"]),  # Kenji
    )
    await avatar.start(session, room=ctx.room)

    await session.start(
        agent=Agent(
            instructions=(
                "You are a friendly product assistant. Speak English unless the user "
                "speaks to you in another language — then match their language."
            )
        ),
        room=ctx.room,
    )

    await session.generate_reply(instructions="Greet the user briefly, in English.")


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, agent_name="synthesia-avatar-agent"))
```

Swap providers freely (Deepgram STT, ElevenLabs TTS, Anthropic LLM, …) — install the matching `livekit-agents` extras. The avatar lines never change.

To switch avatars mid-session, pass up to five ids in `avatar_ids` and call `await avatar.swap_avatar("<other-id>")` (`"default"` returns to the first id) — details in `references/api-and-troubleshooting.md`.

## Frontend

The avatar joins as a **regular LiveKit participant**, so any LiveKit client renders it with zero Synthesia-specific code. Pick the first option that fits:

1. **Zero setup — LiveKit Cloud Agent Console.** In the LiveKit Cloud dashboard, open the same project the agent connects to → **Agents** → **Console**, select the agent from the dropdown by its `agent_name` (`synthesia-avatar-agent` in the boilerplate), and hit **Start session**. This is a real browser room that renders video for avatar agents — Kenji appears here directly. Do **not** suggest `agents-playground.livekit.io`: the hosted playground is deprecated and now redirects to the Agent Console.
2. **User already has a LiveKit frontend** → done. The avatar's video track appears alongside other participants (with `useVoiceAssistant`, it surfaces as the agent's video).
3. **Fastest path to a real product frontend** → clone the [interactive-avatar-quickstarts/minimal](https://github.com/synthesia-ai/interactive-avatar-quickstarts/tree/main/minimal) repo. Crib the frontend and token endpoint (`index.html` + `server.py`, including `sync_streams=True`); its agent is latency-tuned (Cartesia voices, preflight speculation) rather than this guide's minimal template — the avatar lines are identical either way. Its `server.py` dispatches via `RoomAgentDispatch`; keep that agent name in sync with your worker's `agent_name`.
4. **Building their own** → LiveKit's [frontend guide](https://docs.livekit.io/agents/start/frontend/) and the React [`useVoiceAssistant`](https://docs.livekit.io/reference/components/react/hook/usevoiceassistant/) hook. The frontend needs a token endpoint (standard LiveKit access token minted server-side); it must never see `SYNTHESIA_API_KEY`. Mint tokens with `sync_streams=True` in the room config — it keeps the avatar's audio and video in sync in the browser (see `server.py` in the quickstart repo for the pattern).

**Video quality:** the avatar's resolution is set by Synthesia's hosted worker — the plugin has no quality knob — so the only lever is the subscriber. Either create the room with adaptive downscaling off (`new Room({ adaptiveStream: false })` in `livekit-client`) so the client always pulls full resolution, or keep `adaptiveStream` on but render the avatar's video element large and pin its track with `publication.setVideoQuality(VideoQuality.HIGH)` — adaptive streaming otherwise requests a lower layer for small or hidden elements and pauses the track in background tabs.

**Dispatch:** `agent_name=` in `WorkerOptions` makes dispatch **explicit** — the agent only joins rooms it's dispatched into. The Agent Console dispatches for you; a custom frontend (options 2–4) must request the agent in the token's room config or the avatar never joins:

```python
from livekit import api

token = (
    api.AccessToken()
    .with_identity(identity)
    .with_grants(api.VideoGrants(room_join=True, room=room_name))
    .with_room_config(api.RoomConfiguration(
        agents=[api.RoomAgentDispatch(agent_name="synthesia-avatar-agent")],
        sync_streams=True,  # same room config that keeps avatar A/V in sync (option 4)
    ))
    .to_jwt()
)
```

(Server-side alternative: `lkapi.agent_dispatch.create_dispatch(...)`.) Removing `agent_name` restores **automatic dispatch**: the worker joins every new room in the entire LiveKit project, not just your app's — fine in a solo sandbox, wrong in any shared project.

## Run it

```bash
python agent.py dev
```

Then test in the **LiveKit Cloud Agent Console** (or the user's frontend): dashboard → same project → Agents → Console → select `synthesia-avatar-agent` from the agent dropdown → **Start session**. Speak; Kenji should appear and lip-sync the replies.

**Careful with the word "console" — there are two, and they behave oppositely:**

| | What it is | Avatar behaviour |
| --- | --- | --- |
| `python agent.py console` | Terminal run mode, local **mock room** | Silently never appears — do not use for avatar testing |
| LiveKit Cloud **Agent Console** | Browser tool in the dashboard, **real room** | Renders avatar video — the recommended test surface |

Always phrase advice to the user with this distinction; a bare "don't use console mode" reads as a warning against the dashboard tool they should actually be using.

Expected sequence on first run: agent connects → avatar worker is dispatched → avatar joins and publishes video (within `join_timeout`, default 30 s; cold starts can be slow — raise it rather than assuming failure) → speaking to the agent produces a lip-synced reply.

If anything fails, match the error name or symptom in `references/api-and-troubleshooting.md` before changing code.
