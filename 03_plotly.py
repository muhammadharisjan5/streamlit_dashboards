# Import libraries
from turtle import width
import streamlit as st
import plotly.express as px
import pandas as pd
import seaborn as sns


# import dataset
st.title("plotly and streamlit ko mila k app bnana")
df = px.data.election()
st.write(df) 

# summary stat
st.write(df.describe())

# data management
# year_option = df["tip"].unique().tolist()
# year = st.selectbox("which year should we plot?", year_option, 0)
# df = df[df["year"]==year]

# plotting

fig = px.scatter(df, x="Coderre", y="Joly", animation_frame="total", 
    animation_group="total", range_x=[100,10000000], range_y=[25,140000])
fig.update_layout(width=600)
st.write(fig)
