import streamlit as st
import cv2
from streamlit_webrtc import webrtc_streamer
from yt_dlp import YoutubeDL
import tempfile

class Project2:
    def __init__(self):
        pass

    def app(self):
        st.title("Проект 2: Работа с видео потоками")

        # Выбор источника видео
        video_source = st.selectbox(
            "Выберите источник видео",
            ["Мобильная камера", "YouTube ссылка", "Локальный файл", "Веб-камера", "RTSP поток"]
        )

        if video_source == "Мобильная камера":
            img_file = st.camera_input("Сделайте фото")
            if img_file:
                st.image(img_file)

        elif video_source == "YouTube ссылка":
            youtube_url = st.text_input("Введите URL YouTube видео:")
            if youtube_url:
                try:
                    with YoutubeDL({"format": "best"}) as ydl:
                        info = ydl.extract_info(youtube_url, download=False)
                        video_url = info["url"]
                        st.video(video_url)
                except Exception as e:
                    st.error(f"Не удалось загрузить видео: {e}")

        elif video_source == "Локальный файл":
            video_file = st.file_uploader("Загрузите видео файл", type=["mp4", "mov", "avi"])
            if video_file:
                with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                    temp_file.write(video_file.read())
                    st.video(temp_file.name)

        elif video_source == "Веб-камера":
            webrtc_streamer(key="example")

        elif video_source == "RTSP поток":
            rtsp_url = st.text_input("Введите RTSP ссылку:")
            if rtsp_url:
                cap = cv2.VideoCapture(rtsp_url)
                frame_placeholder = st.empty()
                stop = st.button("Остановить поток")

                while not stop:
                    ret, frame = cap.read()
                    if not ret:
                        st.error("Не удалось получить RTSP поток.")
                        break
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame_placeholder.image(frame)

                cap.release()

        else:
            st.warning("Выберите источник видео.")
