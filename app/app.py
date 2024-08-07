import random
import duckdb
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

st.title("Dashboard")
# st.markdown("_Prototype v0.4.1_")

with st.sidebar:
    st.header("Configuration")
    uploaded_file = st.file_uploader("Choose a file")
    
if uploaded_file is None:
    st.info("Upload a csv file through config", icon="ℹ️")
    st.stop()
    
    
# Data Loading    
@st.cache_data
def load_data(path: str):
    df = pd.read_excel(path)
    return df


df = load_data(uploaded_file)
all_months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]


with st.expander("Data Preview"):
    st.dataframe(df, column_config={"Year": st.column_config.NumberColumn(format="%d")})
    

# Streamlit Layout

top_left_column, top_right_column = st.columns((2, 1))