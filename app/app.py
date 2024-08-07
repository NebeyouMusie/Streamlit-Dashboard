import random
import duckdb
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from utils import plot_metric, plot_gauge, plot_top_right, plot_bottom_left, plot_bottom_right

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
bottom_left_column, bottom_right_column = st.columns(2)

with top_left_column:
    column_1, column_2, column_3, column_4 = st.columns(4)
    
    with column_1:
        fig_1 = plot_metric("Receivable Accounts", 6621280, prefix="$", suffix="", show_graph=True, color_graph="rgba(0, 104, 201, 0.2)")
        st.plotly_chart(fig_1, use_container_width=True)