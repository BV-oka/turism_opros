# импортируем библиотеку streamlit
import streamlit as st
# импортируем библиотеку pandas
import pandas as pd
import numpy as np

st.markdown("# Туризм")
st.sidebar.markdown("# главная page 🎈")


# Название
st.sidebar.title("что-то")

# Заголовок
st.header("муниципальное образование город Алексин")

# Подзаголовок
st.subheader("визуализация результатов опроса по развитию туризма")

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
gender = st.sidebar.radio("выберите пол респондентов: ", ('все','муж','жен'), horizontal=True)

# ещё полоска
st.sidebar.divider()

# переключатель возраста
age = st.sidebar.radio("укажите возраст респондентов: ", ('все','до 35', '36-45','46-55', 'старше 55'), horizontal=False)

# ещё полоска
st.sidebar.divider()

# переключатель отношения
att = st.sidebar.radio("укажите отношение к туристам респондентов: ", ('все','положительное', 'отрицательное'), horizontal=False)

# ещё полоска
st.sidebar.divider()

col1, col2, col3 = st.columns(3)
col1.metric(label="Temperature", value="70 °F", delta="1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")



if gender == 'муж':
    st.sidebar.write("вы выбрали респондентов мужчин в возрасте", age)
else:
    st.sidebar.write("вы выбрали респондентов женщин в возрасте", age)
    
# ещё полоска
st.sidebar.divider()

if st.sidebar.button('я кнопка -  Нажми на меня'):
  st.sidebar.write('надпись - результат нажатия на кнопку!')



option = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.sidebar.write('You selected:', option)

# читаем таблицу с опросом
df = pd.read_csv("datasets/Opros_po_razvitiiu_turizma.csv")

# таблица с опросом вывести на экран целиком
# st.dataframe(df)

# таблица с опросом вывести на экран только мероприятия
st.dataframe(df)
