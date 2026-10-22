# agent.py
import asyncio
import json
import os

from dotenv import load_dotenv
from livekit.agents import Agent, AgentSession, JobContext, WorkerOptions, cli
from livekit.plugins import openai, synthesia
from nvidia_tts import create_nvidia_magpie_tts

load_dotenv()

REQUIRED_ENVIRONMENT = (
    "LIVEKIT_URL",
    "LIVEKIT_API_KEY",
    "LIVEKIT_API_SECRET",
    "SYNTHESIA_API_KEY",
    "OPENROUTER_API_KEY",
    "NVIDIA_API_KEY",
)


async def entrypoint(ctx: JobContext):
    missing = [name for name in REQUIRED_ENVIRONMENT if not os.getenv(name)]
    if missing:
        raise RuntimeError(
            "Missing required avatar-agent environment variables: "
            + ", ".join(missing)
            + ". Copy avatar-agent/.env.example to avatar-agent/.env and fill in the values."
        )

    await ctx.connect()

    # Use OpenRouter's chat-completions API. OpenRouter does not expose the
    # OpenAI Realtime WebSocket endpoint used by the realtime model.
    session = AgentSession(
        llm=openai.LLM.with_openrouter(
            model=os.getenv("OPENROUTER_MODEL", "openai/gpt-4o-mini"),
            api_key=os.environ["OPENROUTER_API_KEY"],
        ),
        # NVIDIA Magpie provides the speech audio that Synthesia lip-syncs.
        tts=create_nvidia_magpie_tts(),
    )

    # Attach the avatar BEFORE session.start() — order matters.
    avatar = synthesia.AvatarSession(
        synthesia.AvatarConfig(avatar_ids=["7572faa9-15da-400d-8227-ef1ab8932523"]),  # Kenji
    )
    await avatar.start(session, room=ctx.room)

    await session.start(
        agent=Agent(
            instructions=(
                "You are Joshua Ludolf's AI avatar assistant. You can answer questions about Joshua's "
                "background, skills, education, experience, and contact information. "
                "Joshua Ludolf is a Computer Science student and aspiring AI professional. "
                "He has a Bachelor of Science in Computer Science from Texas A&M University of San Antonio (May 2025) "
                "and a Master's degree in Artificial Intelligence from University of Texas at Austin (May 2026). "
                "His technical skills include Python, Java, SQL, HTML, CSS, Markdown, Maven, "
                "Django, FastAPI, Flask, JavaFX, PyTorch, TensorFlow, Docker, Git, GitHub Copilot, "
                "IntelliJ IDEA, Jupyter Notebook, VS Code. "
                "He has experience developing backend services using Flask, creating databases from SQL to Firebase, "
                "processing data for Machine Learning applications, and implementing full-stack web applications. "
                "Contact: joshualudolf@gmail.com, +1 (830) 331-0424. "
                "LinkedIn: linkedin.com/in/joshua-ludolf, GitHub: github.com/joshua-ludolf, Devpost: devpost.com/joshua-ludolf. "
                "Interests: AI/ML, full-stack web development, data science, open source, software architecture, cloud computing. "
                "Speak English unless the user speaks to you in another language — then match their language. "
                "Be friendly, professional, and helpful."
            )
        ),
        room=ctx.room,
    )

    def handle_data(data_packet):
        if data_packet.topic != "avatar.question":
            return
        asyncio.create_task(handle_question(data_packet))

    async def handle_question(data_packet):
        try:
            payload = json.loads(data_packet.data.decode("utf-8"))
            question = str(payload.get("question", "")).strip()
            if question:
                await session.generate_reply(user_input=question, input_modality="text")
        except (UnicodeDecodeError, json.JSONDecodeError, TypeError, ValueError) as error:
            print(f"Invalid avatar question: {error}")

    ctx.room.on("data_received", handle_data)
    await session.generate_reply(instructions="Greet the user briefly as Joshua's AI avatar assistant.")


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, agent_name="synthesia-avatar-agent"))