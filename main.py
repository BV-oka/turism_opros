# импортируем библиотеку streamlit
import streamlit as st
# импортируем библиотеку pandas
import pandas as pd

if st.button('Нажми на меня'):
  st.write('Привет, мир!')


# Название
st.title("Песочница")

# Заголовок
st.header("Это заголовок")

# Подзаголовок
st.subheader("Это подзаголовок")

# Подзаголовок
st.subheader("Это подзаголовок")

# Текст
st.text("Просто текст")

# полоски
st.divider()
st.divider()

st.success("Success")
st.info("Information")
st.warning("Warning")
st.error("Error")
# st.snow()
# st.balloons()




# переключатели

gender = st.radio("выберите пол респондентов: ", ('муж', 'жен'), horizontal=True)

if (gender == 'муж'):
    st.success("муж")
else:
    st.success("жен")
   



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


# слайдеры

# age = st.slider('How old are you?', 0, 130, 25)
# st.write("I'm ", age, 'years old')



values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

