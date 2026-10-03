import os
import signal
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
processes = []


def stop_processes(*_):
    for process in processes:
        if process.poll() is None:
            process.terminate()
    for process in processes:
        try:
            process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            process.kill()
    raise SystemExit(0)


if __name__ == "__main__":
    os.environ.setdefault("AVATAR_CHAT_HOST", "0.0.0.0")
    os.environ.setdefault("AVATAR_CHAT_PORT", os.getenv("PORT", "8787"))

    processes = [
        subprocess.Popen([sys.executable, str(ROOT / "chat_api.py")], cwd=ROOT),
        subprocess.Popen([sys.executable, str(ROOT / "agent.py"), "start"], cwd=ROOT),
    ]
    signal.signal(signal.SIGINT, stop_processes)
    signal.signal(signal.SIGTERM, stop_processes)

    exit_code = 0
    for process in processes:
        code = process.wait()
        if code:
            exit_code = code
            break
    stop_processes()
    raise SystemExit(exit_code)
