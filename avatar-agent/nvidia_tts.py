import asyncio
import io
import os
import uuid
import wave
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from livekit.agents import APIConnectOptions, APIError, DEFAULT_API_CONNECT_OPTIONS
from livekit.agents.tts import AudioEmitter, ChunkedStream, TTS, TTSCapabilities


class NvidiaMagpieTTS(TTS):
    """LiveKit adapter for NVIDIA's hosted Magpie multilingual TTS model."""

    def __init__(
        self,
        *,
        api_key: str,
        endpoint: str = (
            "https://877104f7-e885-42b9-8de8-f6e4c6303969."
            "invocation.api.nvcf.nvidia.com/v1/audio/synthesize"
        ),
        language: str = "en-US",
        voice: str = "Magpie-Multilingual.EN-US.Aria",
        sample_rate: int = 22050,
    ):
        super().__init__(
            capabilities=TTSCapabilities(streaming=False),
            sample_rate=sample_rate,
            num_channels=1,
        )
        self._api_key = api_key
        self._endpoint = endpoint
        self._language = language
        self._voice = voice

    @property
    def model(self) -> str:
        return "magpie-tts-multilingual"

    @property
    def provider(self) -> str:
        return "nvidia"

    def synthesize(
        self,
        text: str,
        *,
        conn_options: APIConnectOptions = DEFAULT_API_CONNECT_OPTIONS,
    ) -> ChunkedStream:
        return _NvidiaMagpieChunkedStream(
            tts=self,
            input_text=text,
            conn_options=conn_options,
        )

    async def _synthesize(self, text: str) -> bytes:
        body = urlencode(
            {
                "text": text,
                "language": self._language,
                "voice": self._voice,
                "sample_rate_hz": str(self.sample_rate),
                "encoding": "LINEAR_PCM",
            }
        ).encode("utf-8")

        request = Request(
            self._endpoint,
            data=body,
            headers={
                "Authorization": f"Bearer {self._api_key}",
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "audio/wav",
            },
            method="POST",
        )

        try:
            return await asyncio.to_thread(self._request_audio, request)
        except (HTTPError, URLError, TimeoutError) as error:
            raise APIError(f"NVIDIA Magpie TTS request failed: {error}") from error

    @staticmethod
    def _request_audio(request: Request) -> bytes:
        with urlopen(request, timeout=30) as response:
            return response.read()


class _NvidiaMagpieChunkedStream(ChunkedStream):
    async def _run(self, output_emitter: AudioEmitter) -> None:
        tts = self._tts
        if not isinstance(tts, NvidiaMagpieTTS):
            raise APIError("Invalid TTS provider for NVIDIA Magpie stream")

        audio = await tts._synthesize(self._input_text)
        try:
            with wave.open(io.BytesIO(audio), "rb") as wav:
                sample_rate = wav.getframerate()
                channels = wav.getnchannels()
                sample_width = wav.getsampwidth()
                pcm = wav.readframes(wav.getnframes())
        except (wave.Error, EOFError) as error:
            raise APIError("NVIDIA Magpie returned invalid WAV audio") from error

        if sample_width != 2:
            raise APIError("NVIDIA Magpie returned audio that is not 16-bit PCM")
        if sample_rate != tts.sample_rate or channels != tts.num_channels:
            raise APIError(
                "NVIDIA Magpie returned unexpected audio format: "
                f"{sample_rate}Hz/{channels} channel(s)"
            )

        output_emitter.initialize(
            request_id=uuid.uuid4().hex,
            sample_rate=sample_rate,
            num_channels=channels,
            mime_type="audio/pcm",
        )
        bytes_per_frame = sample_width * channels
        chunk_size = int(sample_rate * 0.02) * bytes_per_frame
        for offset in range(0, len(pcm), chunk_size):
            output_emitter.push(pcm[offset : offset + chunk_size])


def create_nvidia_magpie_tts() -> NvidiaMagpieTTS:
    api_key = os.getenv("NVIDIA_API_KEY")
    if not api_key:
        raise RuntimeError("NVIDIA_API_KEY is required for Magpie TTS")

    return NvidiaMagpieTTS(
        api_key=api_key,
        endpoint=os.getenv(
            "NVIDIA_TTS_ENDPOINT",
            (
                "https://877104f7-e885-42b9-8de8-f6e4c6303969."
                "invocation.api.nvcf.nvidia.com/v1/audio/synthesize"
            ),
        ),
        language=os.getenv("NVIDIA_TTS_LANGUAGE", "en-US"),
        voice=os.getenv(
            "NVIDIA_TTS_VOICE",
            "Magpie-Multilingual.EN-US.Aria",
        ),
        sample_rate=int(os.getenv("NVIDIA_TTS_SAMPLE_RATE", "22050")),
    )
