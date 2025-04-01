import streamlit as st
import os


st.title("Music Player")

UPLOAD_FOLDER = "uploaded_songs"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


st.sidebar.header("Upload a Song")
uploaded_file = st.sidebar.file_uploader("Choose an MP3 file", type=["mp3"])

if uploaded_file:
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.sidebar.success(f"Uploaded {uploaded_file.name}!")


songs = [f for f in os.listdir(UPLOAD_FOLDER) if f.endswith(".mp3")]


if songs:
    st.subheader("Select a Song")
    selected_song = st.selectbox("Choose a song", songs)

    # Play selected song
    song_path = os.path.join(UPLOAD_FOLDER, selected_song)
    st.audio(song_path, format="audio/mp3")
else:
    st.warning("No songs uploaded yet. Please upload an MP3 file.")
