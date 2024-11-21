import streamlit as st
import pandas as pd

class Project1:
    def __init__(self):
        pass

    def app(self):
        st.title("Проект 1: Анализ данных")
        st.write("Загрузите CSV-файл для анализа.")

        # Форма для загрузки файла
        uploaded_file = st.file_uploader("Выберите CSV-файл", type=["csv"])

        if uploaded_file is not None:
            # Читаем загруженный файл
            data = pd.read_csv(uploaded_file)

            # Отображаем данные
            st.write("Вот первые несколько строк вашего файла:")
            st.dataframe(data.head())

            # Фильтр по колонке
            column = st.selectbox("Выберите колонку для фильтрации", data.columns)
            if column:
                unique_values = data[column].unique()
                selected_value = st.selectbox("Выберите значение для фильтрации", unique_values)

                filtered_data = data[data[column] == selected_value]
                st.write(f"Фильтрованные данные по значению '{selected_value}':")
                st.dataframe(filtered_data)
