#  VoxGuard
AI-Powered Real-Time Voice Cloning & Impersonation Detection
VoxGuard is a voice security prototype designed to help identify suspicious AI-generated and cloned voices during audio communication.
## 🚀 Project Features
- Real-time microphone audio streaming
- WebSocket-based communication
- Audio signal analysis
- Live audio waveform visualization
- Audio metrics monitoring
- AI voice-cloning detection (planned)
- Risk scoring and security alerts (planned)
## 🛠 Tech Stack
- Python
- FastAPI
- WebSockets
- NumPy
- HTML, CSS, JavaScript
- Web Audio API
## 📁 Project Structure
```text
VoxGuard/
├── backend/
│   ├── main.py
│   ├── audio_engine.py
│   └── requirements.txt
├── frontend/
│   └── index.html
└── README.md
```

## ▶️ Run Locally

Install dependencies:

```bash
pip install -r backend/requirements.txt
```

Start the server:

```bash
cd backend
uvicorn main:app --reload
```

Open in browser:

http://127.0.0.1:8000

## ⚠️ Development Status

Currently, VoxGuard supports microphone audio streaming and basic audio signal analysis.

The trained AI voice-cloning detection model, risk scoring, and intelligent alerts are under development.

## 🎯 Goal

To make voice-based communication safer by helping users recognize possible voice impersonation and AI voice-cloning threats.

**Trust the voice, verify the source.**
