import streamlit as st
import pandas as pd

class Project1:
    def __init__(self):
        pass

    def app(self):
        st.title("Проект 1: Анализ данных")
        st.write("На этой странице вы можете загрузить и исследовать данные.")

        # Загрузка файла
        uploaded_file = st.file_uploader("Загрузите CSV-файл", type=["csv"])

        if uploaded_file is not None:
            # Чтение файла
            data = pd.read_csv(uploaded_file)
            st.write("Первые строки загруженного файла:")
            st.dataframe(data.head())

            # Фильтрация данных
            column = st.selectbox("Выберите колонку для фильтрации", data.columns)
            if column:
                unique_values = data[column].unique()
                selected_values = st.multiselect(f"Выберите значения для фильтрации по {column}", unique_values)
                
                if selected_values:
                    filtered_data = data[data[column].isin(selected_values)]
                    st.write(f"Отфильтрованные данные по значениям: {selected_values}")
                    st.dataframe(filtered_data)

        else:
            st.warning("Пожалуйста, загрузите CSV-файл.")
