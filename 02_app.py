from sklearn.ensemble import RandomForestRegressor
import streamlit as st
from pydoc import describe
from sklearn import datasets
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import streamlit as st
import seaborn as sns
import pandas as pd


# make containers
header = st.container()
data_sets = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title("Kashti ki app")
    st.text("In the project we will work on kashti data")
    
with data_sets:
    st.header("Kashti doob gaye") 
    st.text("We will work with Titanic dataset")
    # Import data 
    df = sns.load_dataset("titanic")
    st.write(df.head())
    df = df.dropna()
    
    st.subheader("Sambha, Are oooh sambha, kitnay aadmi thay?")
    st.bar_chart(df["sex"].value_counts())
    
    # Other plot
    st.subheader("Class k hisab se farq")
    st.bar_chart(df["class"].value_counts())
    
    # barplot
    st.bar_chart(df["age"].sample())  # or .head()
    
with features:
    st.header("These are our app features:")
    st.text("Awen bht saary features add krty hain, asaan hi hay")
    st.markdown("1. **Feature 1:** This will tell us pata nahi")
    st.markdown("1. **Feature 1:** This will tell us pata nahi")
    
with model_training:
    st.header("Kashti walon ka kia bna?-Model training")
    st.text("is main hm apny parameters ko kam ya zyada kryn gy")   
    
    # Making columns
    input, display = st.columns(2)
    
    # pehlay column main ap k selection points hun
    max_depth = input.slider("How many people do you know?", min_value=10, max_value=100, value=20, step=5)
    
# n_estimators
n_estimators = input.selectbox("How many tree should be there in a RF?", options=[50,100,200,300,"No limit"])
 
# adding list of feature
input.write(df.columns)

# input features from user
input_features = input.text_input("which feature we should use?")
    
# Machine learning model
model = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)
    
# yahan per hm aik condition lagayen gy
if n_estimators == "No limit" :
    model = RandomForestRegressor(max_depth=max_depth)
else:
    random_r = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)    
    
# define X and Y
X = df[[input_features]]
y = df[["fare"]]
    
# fit our model
model.fit(X, y)
pred = model.predict(y)  
    
# Display metrices
display.subheader("Mean absolute error of the model is: ")
display.write(mean_absolute_error(y, pred))
display.subheader("Mean squared error of the model is: ")
display.write(mean_squared_error(y, pred))
display.subheader("R squared score of the model is: ")
display.write(r2_score(y, pred))