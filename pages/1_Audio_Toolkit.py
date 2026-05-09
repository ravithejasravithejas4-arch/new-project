import streamlit as st

st.title("🎵 Audio Toolkit")

st.header("Working of Audio Toolkit")

st.write("""
The Audio Toolkit module is designed to perform various audio processing operations.

First, the user uploads an audio file in MP3 or WAV format using the Streamlit interface.

After uploading, the system processes the audio using Python libraries such as Pydub and Librosa.

The module performs operations like:

• Audio format conversion  
• Audio trimming  
• Volume increase/decrease  
• Silence detection  
• Waveform visualization  
• Spectrogram generation  
• Frequency analysis

Waveform visualization shows the amplitude variation of the audio signal over time.

Spectrogram visualization displays frequency intensity distribution with respect to time.

Frequency analysis identifies dominant frequencies present in the audio signal.

The processed audio files and generated visualizations are displayed to the user and can also be downloaded.
""")

st.subheader("⚙️ Features")

st.markdown("""
- 🎵 Audio Format Conversion  
- ✂️ Audio Trimming  
- 🔊 Volume Control  
- 🔇 Silence Detection  
- 📊 Waveform Visualization  
- 📈 Spectrogram Analysis  
- 🎚️ Frequency Analysis  
""")

st.subheader("📤 Upload Audio File")

audio_file = st.file_uploader(
    "Upload MP3 or WAV File",
    type=["mp3", "wav"]
)

if audio_file is not None:

    st.success("Audio Uploaded Successfully!")

    st.audio(audio_file)
