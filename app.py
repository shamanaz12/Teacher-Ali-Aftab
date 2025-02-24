import streamlit as st

st.set_page_config(page_title="YouTube Video Player", layout="wide")
st.title("🎬 YouTube Video Player")

# YouTube Video URL
video_url = "https://youtu.be/KNZfwxN9tUc?si=GSgxsfrcGuMz_Z-9"

st.video(video_url)

st.success("✅ Video embedded successfully from YouTube!")
