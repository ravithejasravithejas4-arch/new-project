import streamlit as st

st.title("📊 Media Analyzer")

st.header("Working of Media Analyzer")

st.write("""
The Media Analyzer module is designed to analyze audio and video properties using Python processing libraries.

First, the user uploads an audio or video file through the Streamlit interface.

After uploading, the system analyzes the media file using libraries such as MoviePy, OpenCV, and Pydub.

The module performs operations like:

• Audio duration analysis  
• Audio bitrate calculation  
• Video FPS detection  
• Video resolution detection  
• Frame extraction  
• Scene change detection using threshold-based analysis

Audio duration analysis calculates the total playback time of the uploaded audio file.

Bitrate analysis estimates the quality and data rate of the audio signal.

Video FPS analysis determines the number of frames displayed per second in the video.

Resolution analysis identifies the width and height of the video frames.

Frame extraction captures individual frames from the video at fixed intervals.

Scene change detection compares consecutive frames and detects major visual changes using threshold values.

The analyzed results are displayed to the user for media inspection and processing.
""")

st.subheader("⚙️ Features")

st.markdown("""
- 🎵 Audio Duration Analysis  
- 🎚️ Audio Bitrate Detection  
- 🎬 Video FPS Detection  
- 📺 Video Resolution Analysis  
- 🖼️ Frame Extraction  
- 🎯 Scene Change Detection  
- 📊 Media Information Display  
""")

st.subheader("📤 Upload Media File")

media_file = st.file_uploader(
    "Upload Audio or Video File",
    type=["mp3", "wav", "mp4", "avi", "mov"]
)

if media_file is not None:

    st.success("Media File Uploaded Successfully!")

    if media_file.type.startswith("audio"):

        st.audio(media_file)

    else:

        st.video(media_file)
