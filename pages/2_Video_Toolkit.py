import streamlit as st

st.title("🎬 Video Toolkit")

st.header("Working of Video Toolkit")

st.write("""
The Video Toolkit module is designed to perform various video processing operations.

First, the user uploads a video file in MP4, AVI, or MOV format using the Streamlit interface.

After uploading, the system processes the video using Python libraries such as MoviePy and OpenCV.

The module performs operations like:

• Video trimming  
• Video merging  
• Audio extraction from video  
• Video compression and resizing  
• Text watermark addition  
• Logo watermark addition

Video trimming allows users to cut selected portions from the uploaded video.

Video merging combines multiple video clips into a single output video.

Audio extraction separates the audio track from the video file.

Video compression reduces the file size and resolution for easier storage and sharing.

Watermarking adds custom text or logo overlays on video frames for branding and identification.

The processed video files are displayed to the user and can also be downloaded.
""")

st.subheader("⚙️ Features")

st.markdown("""
- ✂️ Video Trimming  
- 🔗 Video Merging  
- 🎧 Audio Extraction  
- 📉 Video Compression  
- 📝 Text Watermark  
- 🖼️ Logo Watermark  
- 📺 Video Preview  
""")

st.subheader("📤 Upload Video File")

video_file = st.file_uploader(
    "Upload MP4, AVI, or MOV File",
    type=["mp4", "avi", "mov"]
)

if video_file is not None:

    st.success("Video Uploaded Successfully!")

    st.video(video_file)
