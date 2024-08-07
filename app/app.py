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
        fig_1 =  plot_metric(
            "Total Accounts Receivable",
            6621280,
            prefix="$",
            suffix="",
            show_graph=True,
            color_graph="rgba(0, 104, 201, 0.2)",
        )
        st.plotly_chart(fig_1, use_container_width=True)
        fig_2 = plot_gauge(1.86, "#0068C9", "%", "Current Ratio", 3)
        st.plotly_chart(fig_2, use_container_width=True)
    
    with column_2:
        fig_1 =  plot_metric(
            "Total Accounts Payable",
            1630270,
            prefix="$",
            suffix="",
            show_graph=True,
            color_graph="rgba(255, 43, 43, 0.2)",
        )
        st.plotly_chart(fig_1, use_container_width=True)
        fig_2 = plot_gauge(10, "#FF8700", " days", "In Stock", 31)
        st.plotly_chart(fig_2, use_container_width=True)
        
    with column_3:
        fig_1 = plot_metric("Equity Ratio", 75.38, prefix="", suffix=" %", show_graph=False)
        st.plotly_chart(fig_1, use_container_width=True)
        fig_2 = plot_gauge(7, "#FF2B2B", " days", "Out Stock", 31)
        st.plotly_chart(fig_2, use_container_width=True)
        
    with column_4:
        fig_1 = plot_metric("Debt Equity", 1.10, prefix="", suffix=" %", show_graph=False)
        st.plotly_chart(fig_1, use_container_width=True)
        fig_2 = plot_gauge(28, "#29B09D", " days", "Delay", 31)
        st.plotly_chart(fig_2, use_container_width=True)

with top_right_column:
    fig = plot_top_right(df, all_months)
    st.plotly_chart(fig, use_container_width=True)

with bottom_left_column:
    fig = plot_bottom_left(df, all_months)
    st.plotly_chart(fig, use_container_width=True)

with bottom_right_column:
    fig = plot_bottom_right(df, all_months)
    st.plotly_chart(fig, use_container_width=True)        
