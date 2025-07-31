# meeting-transcriber
# 🎙️ Dexy - AI Meeting Summarizer Agent for Google Meet

Dexy is an intelligent meeting agent that joins Google Meet calls as a virtual participant, listens to conversations in real-time, performs live transcription, identifies speakers, stores memory of past meetings, and delivers accurate meeting summaries via email or dashboard.

> 🔊 "Hey Dexy, summarize the meeting."  
Dexy listens — and delivers.

---

## 🧠 Core Features

| Feature                         | Description                                                                 |
|--------------------------------|-----------------------------------------------------------------------------|
| ✅ Real-time Transcription      | Live captions using Whisper/OpenAI transcription APIs                      |
| ✅ Speaker Identification       | Uses `pyannote.audio` or Whisper timestamps for diarization                |
| ✅ Voice Interaction            | Wake phrase detection: “Hey Dexy...” to trigger summary generation         |
| ✅ Memory Retention             | Stores conversation vectors using FAISS or Pinecone for continuity         |
| ✅ Email Summaries              | Sends automated meeting summaries to registered participants               |
| ✅ Streamlit Dashboard          | Visual log of past meetings, searchable and timestamped                    |
| ✅ Voice Output                 | Uses ElevenLabs API for natural AI-generated voice replies                 |
| ✅ Google Meet Integration      | Uses automation to join Meets (via Puppeteer or Selenium-based wrapper)    |

---

## 🚀 Use Cases

- Remote team meeting summarization  
- Daily stand-up transcription & task logging  
- Speaker-based memory recall  
- Hands-free voice-controlled AI note-taker  
- Lightweight alternative to tools like Otter or Fireflies.ai  

---

## 🏗️ Project Architecture

```bash
dexy/
│
├── agents/
│   └── summarizer_agent.py         # Main agent loop
├── transcriber/
│   ├── whisper_client.py           # Whisper/OpenAI-based live transcription
│   └── diarization.py              # Speaker detection
├── memory/
│   └── vector_store.py             # FAISS or Pinecone memory interface
├── wake_phrase/
│   └── trigger.py                  # Detects “Hey Dexy, summarize the meeting”
├── dashboard/
│   └── app.py                      # Streamlit dashboard
├── utils/
│   └── email_summary.py            # Sends meeting summaries via SMTP
├── run_agent.py                    # Main script to launch Dexy
└── requirements.txt



🧪 Sample Flow

Launch Dexy agent with:
python run_agent.py
Agent joins Google Meet (headless browser).
Real-time transcription begins.
Agent identifies speakers.
On voice command “Hey Dexy, summarize the meeting”:
Summarization is triggered.
Tasks, deadlines, and speakers extracted.
Summary is:
Emailed to participants.
Saved to memory.
Displayed on the dashboard.
🛠️ Installation

git clone https://github.com/your-username/dexy-ai-agent.git
cd dexy-ai-agent

# Set up virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
📦 Key Dependencies

openai – for Whisper & GPT-based summarization
pyannote.audio – for speaker diarization
elevenlabs – for AI-generated voice output
pinecone or faiss-cpu – for vector memory store
selenium or playwright – to automate Google Meet joining
streamlit – for the meeting dashboard
speechrecognition, pyaudio – wake phrase handling
langchain – optional for memory or summarization chains
✅ Example Prompt for Testing

In your Meet, say:

"Okay Dexy, here are the tasks:
Vaibhavi will complete voice integration by Wednesday.
Mayur will deploy speaker diarization by Friday.
The demo is on Monday at 11 AM.
Hey Dexy, summarize the meeting."
Dexy should return a summary like:

📋 Meeting Summary:
- Vaibhavi: Voice API integration (Deadline: Wednesday)
- Mayur: Speaker diarization setup (Deadline: Friday)
- Internal demo scheduled: Monday @ 11:00 AM
🔐 Environment Setup

Create a .env file with:

OPENAI_API_KEY=your_openai_key
ELEVENLABS_API_KEY=your_11labs_key
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your_email@example.com
EMAIL_PASS=your_app_password
🧪 Testing Checklist

 Wake phrase triggers summary
 Live transcription accuracy
 Speaker diarization logs who said what
 Summaries include task + deadlines
 Email delivery working
 Dashboard loads past summaries
📊 Dashboard Preview

Launch dashboard:

streamlit run dashboard/app.py
You’ll see:

Recent meeting logs
Speaker-specific timeline
Keyword filters
Downloadable summaries
📅 Roadmap

 Multi-user diarization improvements
 Google Calendar integration
 Slack/Discord summary delivery
 Native Dexy Desktop App
 Voice-to-action (auto-create Notion/Tasks)
🤝 Contributing

Contributions welcome!
Please submit a PR or open an issue for bugs, features, or enhancements.

📜 License

MIT License © 2025 Mayur Tarate & Team

🔗 Related Projects

OpenAI Whisper
pyannote-audio
ElevenLabs
Langchain
Streamlit
📧 Contact

Mayur Tarate
📫 mtarate2004@gmail.com
🔗 LinkedIn

