import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

class Project2:
    def __init__(self):
        pass

    def app(self):
        st.title("Проект 2: Визуализация данных")
        st.write("Загрузите CSV-файл, чтобы построить график.")

        # Форма для загрузки файла
        uploaded_file = st.file_uploader("Выберите CSV-файл", type=["csv"])

        if uploaded_file is not None:
            # Читаем загруженный файл
            data = pd.read_csv(uploaded_file)
            st.write("Вот первые несколько строк вашего файла:")
            st.dataframe(data.head())

            # Выбор колонок для графика
            x_column = st.selectbox("Выберите колонку для оси X", data.columns)
            y_column = st.selectbox("Выберите колонку для оси Y", data.columns)

            if x_column and y_column:
                # Построение графика
                st.write(f"График зависимости {y_column} от {x_column}:")
                fig, ax = plt.subplots()
                ax.plot(data[x_column], data[y_column], marker='o')
                ax.set_xlabel(x_column)
                ax.set_ylabel(y_column)
                ax.set_title(f"{y_column} vs {x_column}")
                st.pyplot(fig)
