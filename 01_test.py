import streamlit as st
import seaborn as sns

st.header("This video is brought to you by #babaAmmar")
st.text("kia apko maza arha hai sekhny main")

st.header("pata nhi kia likha hai")

df = sns.load_dataset("iris")
st.write(df["sepal_length"].head(10))
st.bar_chart(df["sepal_length"])
st.line_chart(df["sepal_length"])