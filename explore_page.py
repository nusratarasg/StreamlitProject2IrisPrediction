import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

@st.cache
def load_data():
    df = pd.read_csv("iris.csv")
    return df

df = load_data()

def show_explore_page():
    df = pd.read_csv("iris.csv")
    df = df.rename(columns={'Sepal.Length':'Sepal Length','Sepal.Width':'Sepal Width','Petal.Length': 'Petal Length', 'Petal.Width': 'Petal Width'})
    df = df.dropna()
    data = "iris.csv"
    st.write(f"##    Dataset Name:  {data} ")
    st.write('Shape of dataset:', df.shape)
    c = df['Species'].nunique()
    st.write('number of classes:', c)
    s = df['Species'].unique()
    st.write(
        """
     Name of Classes : 
    """
    )
    #st.write('number of classes:', s)

    st.write(f"{s} ")

    d=df.describe()
    st.write(' ### Description of data:', d)
    r = df.head()
    st.write(' ### First five rows of data:')
    st.write(r)





