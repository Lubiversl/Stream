import streamlit as st
from PIL import Image

class Project3:
    def __init__(self):
        pass

    def app(self):
        st.title("Проект 3: Работа с изображениями")
        st.write("Загрузите изображение, чтобы отобразить его на странице.")

        # Загрузка изображения
        uploaded_image = st.file_uploader("Выберите изображение", type=["jpg", "png", "jpeg"])

        if uploaded_image is not None:
            # Открываем изображение с помощью PIL
            image = Image.open(uploaded_image)

            # Отображаем изображение
            st.image(image, caption="Загруженное изображение", use_column_width=True)
            st.write("Размер изображения:", image.size)
