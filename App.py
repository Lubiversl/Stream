import streamlit as st
from pages import Home, Project1, Project2, Project3

# Настраиваем стили
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

pages = {
    "Главная": Home.Home(),
    "Проект 1": Project1.Project1(),
    "Проект 2": Project2.Project2(),
    "Проект 3": Project3.Project3(),
}

# Настраиваем выбор страницы через боковую панель
st.sidebar.title("Навигация")
selected_page = st.sidebar.radio("Выберите страницу", list(pages.keys()))

# Отображаем выбранную страницу
page = pages[selected_page]
page.app()
