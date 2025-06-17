import streamlit as st
import json
from pathlib import Path
from TTS.api import TTS
import tempfile
import os
import uuid

# Constants
SUMMARY_FILE = Path("output/summaries.json")
VOICE_SAMPLE = "voices/obama.wav"

# Set Streamlit page configuration (must be the first Streamlit command)
st.set_page_config(page_title="NewsBreeze", layout="wide")

# Load summaries
if not SUMMARY_FILE.exists():
    st.error("❌ Summaries not found. Run `rss_summary.py` first.")
    st.stop()

with open(SUMMARY_FILE, "r") as f:
    summaries = json.load(f)

st.title("🗞️ NewsBreeze - Celebrity-Powered Audio News")
st.markdown("Enjoy the latest headlines, summarized and read aloud in a celebrity voice (Barack Obama).")

# Initialize TTS only once (cached for performance)
@st.cache_resource
def load_tts():
    return TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=False)

tts = load_tts()

# Display summaries with Read Aloud buttons
for summary in summaries:
    st.markdown("---")
    st.subheader(f"{summary['id']}. {summary['title']}")
    st.write(f"📝 **Summary:** {summary['summary']}")

    button_key = f"read_{summary['id']}"
    if st.button("🔊 Read Aloud", key=button_key):
        with st.spinner("🎤 Generating voice..."):
            tmp_path = Path(tempfile.gettempdir()) / f"newsbreeze_{uuid.uuid4().hex}.wav"
            try:
                # Generate speech using cloned voice
                tts.tts_to_file(
                    text=summary["summary"],
                    speaker_wav=VOICE_SAMPLE,
                    language="en",
                    file_path=str(tmp_path)
                )
                # Load and play audio
                with open(tmp_path, 'rb') as audio_file:
                    st.audio(audio_file.read(), format='audio/wav')
            finally:
                # Safe cleanup
                if tmp_path.exists():
                    try:
                        os.remove(tmp_path)
                    except PermissionError:
                        pass  # File still in use; skip deletion
