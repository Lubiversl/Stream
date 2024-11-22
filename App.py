import streamlit as st
from pages import Home, Project1, Project2, Project3
from PIL import Image
import os

# Устанавливаем параметры страницы
icon_path = os.path.join("img", "game_coin_cash_sack_dollar_bag_bucket_buck_money_icon_262454.png")
st.set_page_config(page_title="My Web App", page_icon=icon_path)

# Настраиваем стили
st.markdown(
    """
    <style>
    .top-menu {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .top-menu button {
        margin: 0 10px;
        padding: 10px 20px;
        background-color: #007BFF;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .top-menu button:hover {
        background-color: #0056b3;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Путь к логотипу
logo_path = os.path.join("img", "game_army_pistol_sword_war_military_gift_weapon_gun_icon_262418.svg")

if os.path.exists(logo_path):
    st.sidebar.image(logo_path, caption="Логотип сайта", use_container_width=True)
else:
    st.sidebar.error("Логотип не найден. Проверьте файл 'game_army_pistol_sword_war_military_gift_weapon_gun_icon_262418.svg'.")

# Создаём верхнее меню с кнопками
selected_page = st.session_state.get("selected_page", "Главная")

st.markdown('<div class="top-menu">', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

if col1.button("Главная"):
    selected_page = "Главная"
    st.session_state["selected_page"] = selected_page
if col2.button("Проект 1"):
    selected_page = "Проект 1"
    st.session_state["selected_page"] = selected_page
if col3.button("Проект 2"):
    selected_page = "Проект 2"
    st.session_state["selected_page"] = selected_page
if col4.button("Проект 3"):
    selected_page = "Проект 3"
    st.session_state["selected_page"] = selected_page
st.markdown('</div>', unsafe_allow_html=True)

# Определяем страницы
pages = {
    "Главная": Home.Home(),
    "Проект 1": Project1.Project1(),
    "Проект 2": Project2.Project2(),
    "Проект 3": Project3.Project3(),
}

# Отображаем выбранную страницу
page = pages[selected_page]
page.app()
