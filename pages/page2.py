import streamlit as st
import pandas as pd


st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")

df = pd.read_csv("main/datasets/Opros_po_razvitiiu_turizma.csv")

st.dataframe(df)
