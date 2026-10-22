FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8787

WORKDIR /app

COPY pyproject.toml README.md ./
COPY agent.py chat_api.py nvidia_tts.py production.py ./

RUN pip install --no-cache-dir .

EXPOSE 8787

HEALTHCHECK --interval=30s --timeout=5s --start-period=30s --retries=3 \
    CMD ["python", "-c", "import os, urllib.request; urllib.request.urlopen('http://127.0.0.1:' + os.getenv('PORT', '8787') + '/health', timeout=3)"]

CMD ["python", "production.py"]
