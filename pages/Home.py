import streamlit as st

class Home:
    def __init__(self):
        pass

    def app(self):
        st.title("Добро пожаловать на главную страницу!")
        st.write("Этот проект демонстрирует, как работать со Streamlit.")
        st.markdown("""
            ### Возможности:
            - Переключение между страницами
            - Работа с интерактивными элементами
            - Визуализация данных
        """)
        st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=300)
