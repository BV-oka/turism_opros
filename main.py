# импортируем библиотеку streamlit
import streamlit as st
# импортируем библиотеку pandas
import pandas as pd
import numpy as np


def process_main_page():
    show_main_page()
    process_side_bar_inputs()

def show_main_page():
    st.set_page_config(
    page_title="Туризм Алексин",
    page_icon="🎈",
    layout="wide"
)
    st.markdown("# Туризм")

    # подзаголовок
    st.subheader("муниципальное образование город Алексин")

    # заголовок
    st.header("визуализация результатов опроса по развитию туризма")

    write_user_data()

def write_user_data(df):
    st.success("Вы выбрали следующие параметры респондентов:")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### пол")
        st.write("gender")
    
    with col2:
        st.markdown("### возраст")
        st.write("age")
    
    with col3:
        st.markdown("### отношение")

def process_side_bar_inputs():
    # пояснения для ввода пользовательских настроек 
    st.sidebar.markdown("### Для анализа результатов опроса выберите параметры респондентов")
    user_input_df = sidebar_input_features()

def sidebar_input_features():
    
    gender = st.sidebar.multiselect("выберите пол респондентов: ", ["мужской","женский"], placeholder="пол респондентов")
    # разделительная полоска
    st.sidebar.divider()

    age = st.sidebar.multiselect("укажите возраст респондентов: ", ["до 35 лет", "36-45 лет","46-55 лет", "старше 55 лет"], placeholder="возраст респондентов")
    # разделительная полоска
    st.sidebar.divider()

    att = st.sidebar.multiselect("укажите отношение респондентов к туристам: ", ["положительное", "отрицательное"], placeholder="выбор отношение")
    st.write(gender)
    
    # data = {
    #     "Gender": gender,
    #     "Age": age,
    #     "Att": att,
    # }

    df = pd.DataFrame(data, index=[0])
    return df

process_main_page()
