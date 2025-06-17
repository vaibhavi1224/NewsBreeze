# 📄 `README.md`

# NewsBreeze 🗞️🎤

**Celebrity-Powered Audio News Reader**

## Features
- Fetches latest RSS headlines (NYT).
- Summarizes headlines using Hugging Face model: `Falconsai/text_summarization`.
- Converts summary into audio using XTTS v2 (`TTS` library).
- Celebrity voice used: Barack Obama (`RaysDipesh/obama-voice-samples`).

# Sample Output

![image](https://github.com/user-attachments/assets/73fd272c-6e05-4759-9cc4-ab3e7437aac9)


### ✅ Project Structure

```
NewsBreeze/
│
├── rss_summary.py               # Fetch + summarize news and save to file
├── streamlit_app.py             # UI: display summaries, select celebrity, play audio
├── samples/
│   └── obama.wav                # Voice sample for XTTS
├── output/
│   └── summaries.json           # Generated summaries
├── README.md                    # Setup steps + models used
└── requirements.txt             # Dependencies
```

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/vaibhavi1224/NewsBreeze.git
cd NewsBreeze
````

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # or .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the summarizer

```bash
python news_summary.py
```

### 5. Launch Streamlit app

```bash
streamlit run app.py
```

## Models Used

* **Summarization:** [`Falconsai/text_summarization`](https://huggingface.co/Falconsai/text_summarization)
* **TTS (Voice):** [`TTS/XTTS v2`](https://github.com/coqui-ai/TTS)
* **Voice sample:** [`RaysDipesh/obama-voice-samples`](https://huggingface.co/datasets/RaysDipesh/obama-voice-samples)

