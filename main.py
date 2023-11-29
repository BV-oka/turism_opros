# импортируем библиотеку streamlit
import streamlit as st
# импортируем библиотеку pandas
import pandas as pd
import numpy as np


st.markdown("# Туризм муниципальное образование город Алексин")
st.sidebar.markdown("# главная page 🎈")

# Название
st.title("что-то")

# Заголовок
st.header("муниципальное образование город Алексин")

# Подзаголовок
st.subheader("визуализация результатов опроса по развитию туризма")

# Текст
st.sidebar.text("Просто текст")

st.sidebar.success("Успех")
st.info("Information")
st.warning("Warning")
st.error("Error")
# st.snow()
# st.balloons()


# полоска
st.divider()

# переключатель пола
gender = st.sidebar.radio("выберите пол респондентов: ", ('муж', 'жен'), horizontal=True)

# слайдер возраста
age = st.slider('Укажите возраст респондентов', 0, 100, 35)


# ещё полоска
st.divider()


if gender == 'муж':
    st.write("вы выбрали респондентов мужчин в возрасте", age)
else:
    st.write("вы выбрали респондентов женщин в возрасте", age)
    
# ещё полоска
st.divider()

if st.button('я кнопка -  Нажми на меня'):
  st.write('надпись - результат нажатия на кнопку!')

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

if genre == ':rainbow[Comedy]':
    st.success('You selected comedy.')
else:
    st.write("You didn\'t select comedy.")


option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)


# слайдер интервал

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)
