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

def sidebar_input_features():
    gender = st.sidebar.multiselect("выберите пол респондентов: ", ["мужской","женский"], placeholder="пол респондентов")
    age = st.sidebar.multiselect("укажите возраст респондентов: ", ["до 35 лет", "36-45 лет","46-55 лет", "старше 55 лет"], placeholder="возраст респондентов")
    att = st.sidebar.multiselect("укажите отношение респондентов к туристам: ", ["положительное", "отрицательное"], placeholder="выбор отношение")


if __name__=="__main__":
    process_main_page()

