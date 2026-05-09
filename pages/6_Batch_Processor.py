import streamlit as st

st.title("📦 Batch Processor")

st.header("Working of Batch Processor")

st.write("""
The Batch Processor module is designed to process multiple audio or video files simultaneously.

First, the user uploads multiple media files using the Streamlit interface.

After uploading, the system processes all uploaded files automatically using Python processing libraries.

The module performs operations like:

• Batch audio conversion  
• Batch audio trimming  
• Batch volume adjustment  
• Batch video processing  
• Automatic output generation  
• ZIP file creation for processed outputs

Batch processing applies the same selected operation to all uploaded files at once.

This reduces manual work and improves processing efficiency for large numbers of media files.

The processed files are stored in output folders and combined into a downloadable ZIP archive.

The generated ZIP file can be downloaded directly from the application interface.
""")

st.subheader("⚙️ Features")

st.markdown("""
- 📤 Multiple File Upload  
- 🎵 Batch Audio Processing  
- 🎬 Batch Video Processing  
- ✂️ Batch Trimming  
- 🔊 Batch Volume Adjustment  
- 📦 ZIP File Generation  
- 📥 Download Processed Files  
""")

st.subheader("📤 Upload Multiple Files")

uploaded_files = st.file_uploader(
    "Upload Audio or Video Files",
    type=["mp3", "wav", "mp4", "avi", "mov"],
    accept_multiple_files=True
)

if uploaded_files:

    st.success(f"{len(uploaded_files)} Files Uploaded Successfully!")

    for file in uploaded_files:

        st.write("📄", file.name)
