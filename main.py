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
att = st.sidebar.radio("укажите отношение респондентов к туристам: ", ('все','положительное', 'отрицательное'), horizontal=False)

# ещё полоска
st.sidebar.divider()

st.success("Вы выбрали следующие параметры респондентов:")

col1, col2, col3 = st.columns(3)
col1.metric(label="пол", value=gender)
col2.metric(label="возраст", value=age)
col3.metric(label="отношение", value=att)


if gender == 'муж':
    st.sidebar.write("вы выбрали респондентов мужчин в возрасте", age)
else:
    st.sidebar.write("вы выбрали респондентов женщин в возрасте", age)
    
# ещё полоска
st.sidebar.divider()



# читаем таблицу с опросом
df = pd.read_csv("datasets/Opros_po_razvitiiu_turizma.csv")



# график
chart_data = pd.DataFrame(df, columns=["пол", "возраст", "отношение"])

st.bar_chart(chart_data)


# график
chart_data = pd.DataFrame(df, columns=["возраст", "отношение"])

st.bar_chart(chart_data)

# график изменить
dfopr=pd.DataFrame([[101, 'ivanov', 'муж', 'да'], [102, 'петров', 'муж', 'нет'], [103, 'сидорова', 'жен', 'да'], [104, 'коровин', 'муж', 'нет'], [105, 'кузнецов', 'муж', 'да'], [106, 'дубова', 'жен', 'нет'], [107, 'зайкина', 'жен', 'да']], columns=['id', 'fio', 'gender', 'otvet'])
dfopr
dfopr1=pd.DataFrame([['Earth', 1], ['Moon', 0.606], ['Mars', 0.107], ['Венера', 0.807]], columns=['name', 'mass'])
st.bar_chart(dfopr1)


# таблица с опросом вывести на экран целиком
# st.dataframe(df)

# таблица с опросом вывести на экран только мероприятия
# st.dataframe(df["Какие событийные мероприятия, по Вашему мнению, будут интересны жителям и гостям города?"])


# фильтр таблицы


# rslt_df = df[(df.пол == 'муж') & (df.возраст == 'до 35 лет') & (df.отношение == 'положительное')] 
rslt_df = df[(df.пол == 'муж') & (df.возраст == age) & (df.отношение == 'положительное')]
st.dataframe(rslt_df)
st.info("ответы респондентов на вопрос: Какие событийные мероприятия, по Вашему мнению, будут интересны жителям и гостям города?")
st.dataframe(rslt_df["ответ"])


# Текст
st.sidebar.text("Просто текст")


st.sidebar.info("Information")
st.sidebar.warning("Warning")
st.sidebar.error("Error")
# st.snow()
# st.balloons()



if st.sidebar.button('я кнопка -  Нажми на меня'):
  st.sidebar.write('надпись - результат нажатия на кнопку!')



option = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.sidebar.write('You selected:', option)
