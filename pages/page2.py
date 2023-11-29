import streamlit as st
import pandas as pd


st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")

df = pd.read_csv("./datasets/Opros_po_razvitiiu_turizma.csv")

st.dataframe(df)

# Название
st.sidebar.title("что-то")

# Заголовок
st.sidebar.header("муниципальное образование город Алексин")

# Подзаголовок
st.sidebar.subheader("визуализация результатов опроса по развитию туризма")

# Текст
st.sidebar.text("Просто текст")

st.sidebar.success("Успех")
st.sidebar.info("Information")
st.sidebar.warning("Warning")
st.sidebar.error("Error")
# st.snow()
# st.balloons()


# полоска
st.sidebar.divider()

# переключатель пола
gender = st.sidebar.radio("выберите пол респондентов: ", ('муж', 'жен'), horizontal=True)

# слайдер возраста
age = st.sidebar.slider('Укажите возраст респондентов', 0, 100, 35)

# ещё полоска
st.sidebar.divider()


if gender == 'муж':
    st.sidebar.write("вы выбрали респондентов мужчин в возрасте", age)
else:
    st.sidebar.write("вы выбрали респондентов женщин в возрасте", age)
    
# ещё полоска
st.sidebar.divider()

if st.sidebar.button('я кнопка -  Нажми на меня'):
  st.sidebar.write('надпись - результат нажатия на кнопку!')

genre = st.sidebar.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

if genre == ':rainbow[Comedy]':
    st.sidebar.success('You selected comedy.')
else:
    st.sidebar.write("You didn\'t select comedy.")


option = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.sidebar.write('You selected:', option)


# слайдер интервал

values = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.sidebar.write('Values:', values)
