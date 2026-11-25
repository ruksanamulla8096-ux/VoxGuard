from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from pathlib import Path
import json
from audio_engine import analyse_audio
app = FastAPI(
    title="VoxGuard",
    description="Real-time voice security monitoring prototype",
    version="1.0"
)
FRONTEND_FILE = (
    Path(__file__).resolve().parent.parent
    / "frontend"
    / "index.html"
)
@app.get("/")
async def home():
    return FileResponse(FRONTEND_FILE)
@app.get("/health")
async def health():
    return {
        "application": "VoxGuard",
        "status": "running",
        "audio_processing": "enabled",
        "ai_detection": "not_integrated"
    }
@app.websocket("/ws/audio")
async def audio_stream(websocket: WebSocket):
    await websocket.accept()
    total_bytes = 0
    total_chunks = 0
    try:
        await websocket.send_json({
            "type": "connection",
            "status": "connected",
            "message": "Audio monitoring started"
        })
        while True:
            audio_bytes = await websocket.receive_bytes()
            # Ignore unexpectedly large chunks
            if len(audio_bytes) > 256000:
                await websocket.send_json({
                    "type": "error",
                    "message": "Audio chunk too large"
                })
                continue
            total_bytes += len(audio_bytes)
            total_chunks += 1
            metrics = analyse_audio(audio_bytes)
            if metrics is not None:
                await websocket.send_json({
                    "type": "audio_metrics",
                    "metrics": metrics,
                    "total_bytes": total_bytes,
                    "total_chunks": total_chunks,
                    "detection": {
                        "status": "not_integrated",
                        "message": (
                            "AI voice-cloning model "
                            "has not been connected yet."
                        )
                    }
                })
    except WebSocketDisconnect:
        print("VoxGuard: browser disconnected")
    except Exception as error:
        print("VoxGuard error:", error)

