import streamlit as st

st.set_page_config(
    page_title="Audio Video Utility Studio",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Audio Video Utility Studio")

st.markdown("""
Welcome to the **Audio Video Utility Studio** project.

This application provides multiple media processing modules using Python libraries such as:

- OpenCV
- MoviePy
- Librosa
- Pydub
- Matplotlib

Use the sidebar to navigate through different modules.
""")

st.subheader("📌 Available Modules")

st.markdown("""
### 🎵 Audio Toolkit
- Audio trimming
- Audio conversion
- Volume adjustment
- Silence detection

### 🎬 Video Toolkit
- Video trimming
- Video merging
- Watermarking
- Compression

### 📊 Media Analyzer
- Audio duration
- Bitrate analysis
- FPS detection
- Scene detection

### 🖼️ Frame Processor
- Frame extraction
- Grayscale conversion
- Edge detection

### 📈 Audio Visualizer
- Waveform visualization
- Spectrogram generation
- Frequency analysis

### 📦 Batch Processor
- Multiple file upload
- Batch processing
- ZIP download
""")

st.success("Select a module from the sidebar to continue.")
