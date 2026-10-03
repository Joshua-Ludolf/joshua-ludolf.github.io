import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.request import Request, urlopen

from dotenv import load_dotenv
from livekit import api

load_dotenv()

MODEL = os.getenv("OPENROUTER_MODEL", "openai/gpt-4o-mini")
PORT = int(os.getenv("AVATAR_CHAT_PORT", "8787"))

SYSTEM_PROMPT = """You are Joshua Ludolf's AI portfolio avatar.
Answer questions using the portfolio facts below. Be concise, warm, and accurate.
Do not invent employers, projects, credentials, or personal details.
Portfolio facts:
- Joshua is an AI and software engineer.
- Bachelor's in Computer Science from Texas A&M University of San Antonio (May 2025).
- Master's degree in Artificial Intelligence from the University of Texas at Austin (May 2026).
- Skills include Python, Java, SQL, HTML, CSS, Django, FastAPI, Flask, PyTorch, TensorFlow, Docker, Git, and full-stack development.
- Interests include AI/ML, data science, open source, software architecture, and cloud computing.
- Contact: joshualudolf@gmail.com.
"""


class ChatHandler(BaseHTTPRequestHandler):
    def _send(self, status, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Access-Control-Allow-Origin", os.getenv("AVATAR_CHAT_ORIGIN", "*"))
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", os.getenv("AVATAR_CHAT_ORIGIN", "*"))
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.end_headers()

    def do_POST(self):
        if self.path == "/api/token":
            self._issue_token()
            return

        if self.path != "/api/avatar/chat":
            self._send(404, {"error": "Not found"})
            return

        try:
            length = int(self.headers.get("Content-Length", "0"))
            payload = json.loads(self.rfile.read(length))
            question = str(payload.get("question", "")).strip()
            if not question or len(question) > 1000:
                self._send(400, {"error": "Question must be between 1 and 1000 characters"})
                return

            request = Request(
                "https://openrouter.ai/api/v1/chat/completions",
                data=json.dumps({
                    "model": MODEL,
                    "messages": [
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": question},
                    ],
                    "temperature": 0.4,
                    "max_tokens": 220,
                }).encode("utf-8"),
                headers={
                    "Authorization": f"Bearer {os.environ['OPENROUTER_API_KEY']}",
                    "Content-Type": "application/json",
                    "HTTP-Referer": os.getenv("AVATAR_CHAT_ORIGIN", ""),
                    "X-Title": "Joshua Ludolf AI Avatar",
                },
                method="POST",
            )
            with urlopen(request, timeout=30) as response:
                result = json.loads(response.read())
            reply = result["choices"][0]["message"]["content"].strip()
            self._send(200, {"reply": reply})
        except Exception as error:
            print(f"Avatar chat error: {error}")
            self._send(502, {"error": "The avatar service is temporarily unavailable"})

    def _issue_token(self):
        try:
            length = int(self.headers.get("Content-Length", "0"))
            payload = json.loads(self.rfile.read(length))
            room = str(payload.get("room", "")).strip()
            identity = str(payload.get("identity", "")).strip()
            if not room or not identity:
                self._send(400, {"error": "Room and identity are required"})
                return

            token = (
                api.AccessToken()
                .with_identity(identity)
                .with_grants(api.VideoGrants(room_join=True, room=room))
                .with_room_config(
                    api.RoomConfiguration(
                        agents=[api.RoomAgentDispatch(agent_name="synthesia-avatar-agent")],
                        sync_streams=True,
                    )
                )
                .to_jwt()
            )
            self._send(200, {"token": token, "url": os.environ["LIVEKIT_URL"]})
        except Exception as error:
            print(f"LiveKit token error: {error}")
            self._send(500, {"error": "Unable to create a LiveKit token"})


if __name__ == "__main__":
    print(f"Avatar chat API listening on http://127.0.0.1:{PORT}/api/avatar/chat")
    ThreadingHTTPServer(("127.0.0.1", PORT), ChatHandler).serve_forever()
