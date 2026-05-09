import streamlit as st

st.title("📈 Audio Visualizer")

st.header("Working of Audio Visualizer")

st.write("""
The Audio Visualizer module is designed to analyze and visualize audio signals graphically.

First, the user uploads an audio file in MP3 or WAV format using the Streamlit interface.

After uploading, the system processes the audio signal using Python libraries such as Librosa, NumPy, and Matplotlib.

The module performs operations like:

• Waveform visualization  
• Spectrogram generation  
• Frequency analysis

Waveform visualization displays the amplitude variation of the audio signal with respect to time.

Spectrogram visualization represents frequency intensity distribution over time using color mapping techniques.

Frequency analysis identifies dominant frequencies present in the audio signal using Fast Fourier Transform (FFT).

These visualizations help users understand audio characteristics, sound patterns, and frequency behavior.

The generated graphs and analysis results are displayed to the user for better audio inspection and visualization.
""")

st.subheader("⚙️ Features")

st.markdown("""
- 📊 Audio Waveform Visualization  
- 📈 Spectrogram Generation  
- 🎚️ Frequency Analysis  
- 🎵 Audio Signal Inspection  
- 🔍 FFT-Based Frequency Detection  
- 📉 Graphical Audio Representation  
""")

st.subheader("📤 Upload Audio File")

audio_file = st.file_uploader(
    "Upload MP3 or WAV File",
    type=["mp3", "wav"]
)

if audio_file is not None:

    st.success("Audio Uploaded Successfully!")

    st.audio(audio_file)
