import subprocess
import sys

# 🛠️ Install required packages if not already installed
required_packages = [
    "streamlit",
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "plotly",
    "openpyxl"  # Required for Excel file support
]

for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# 📦 Importing Libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from io import StringIO

# 🏠 Set the page's title, layout, and add a fun icon
st.set_page_config(page_title="📊 Data Analyzer Pro", layout="wide", page_icon="📈")
st.title("📊 Data Analyzer Pro")
st.markdown("### 🚀 Upload your CSV or Excel file and explore your data like a pro!")

# 🌗 Add a toggle button to switch between Light and Dark themes
theme = st.radio("Choose a theme:", ['Dark', 'Light'], horizontal=True)

# 🎨 Apply the selected theme using custom CSS
if theme == 'Dark':
    st.markdown("""
    <style>
    .stApp { background-color: #1E1E1E; color: white; }
    .stButton>button, .stSelectbox, .stTextInput, .stFileUploader, .stRadio>div {
        background-color: #333 !important; color: white !important; border-radius: 5px;
    }
    .stMetric-value, .stDataFrame, .stMarkdown, h2, h3, label { color: white !important; }
    .css-1d391kg, .css-1d391kg:hover { background-color: #444 !important; }
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <style>
    .stApp { background-color: #f0f2f6; color: black; }
    .stButton>button, .stSelectbox, .stTextInput, .stFileUploader, .stRadio>div {
        background-color: white !important; color: black !important; border-radius: 5px;
    }
    .stMetric-value, .stDataFrame, .stMarkdown, h2, h3, label { color: black !important; }
    .css-1d391kg, .css-1d391kg:hover { background-color: #f0f2f6 !important; }
    </style>
    """, unsafe_allow_html=True)

# 📂 File uploader for CSV or Excel files
uploaded_file = st.file_uploader("📂 Upload a CSV or Excel file", type=["csv", "xlsx"])

# 🧮 File processing
if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.subheader("📄 Raw Data")
        st.write(df)

        # 🧾 File Summary
        st.subheader("📋 File Summary")
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Rows", df.shape[0])
        col2.metric("Total Columns", df.shape[1])
        col3.metric("Missing Values", df.isnull().sum().sum())

        # 🔍 Data Filtering
        st.subheader("🔍 Filter Data")
        filter_column = st.selectbox("Select a column to filter by", df.columns)
        filter_value = st.text_input(f"Enter a value to filter by in '{filter_column}'")
        if filter_value:
            filtered_df = df[df[filter_column].astype(str).str.contains(filter_value, case=False)]
            st.write(filtered_df)

        # 📊 Basic Statistics
        st.subheader("📊 Basic Statistics")
        st.write(df.describe())

        # ℹ️ Data Information
        st.subheader("ℹ️ Data Information")
        if st.checkbox("Show Data Information"):
            buffer = StringIO()
            df.info(buf=buffer)
            st.text(buffer.getvalue())

        # 🔍 Missing Values
        st.subheader("🔍 Missing Values")
        st.write(df.isnull().sum())

        # 📈 Visualization options
        st.subheader("📈 Data Visualization")
        numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
        categorical_columns = df.select_dtypes(include=['object']).columns.tolist()

        # 📊 Histogram
        if numeric_columns:
            st.write("### 📊 Histogram")
            selected_column = st.selectbox("Select a numeric column for histogram", numeric_columns)
            fig, ax = plt.subplots()
            sns.histplot(df[selected_column], kde=True, ax=ax, color='skyblue')
            st.pyplot(fig)

        # 📊 Bar Plot
        if categorical_columns:
            st.write("### 📊 Bar Plot")
            selected_column = st.selectbox("Select a categorical column for bar plot", categorical_columns)
            fig, ax = plt.subplots()
            sns.countplot(y=df[selected_column], ax=ax, palette='viridis')
            st.pyplot(fig)

        # 📄 Downloadable Report
        st.subheader("📄 Generate Report")
        if st.button("Generate and Download Report"):
            report = f"""
            Data Analyzer Pro Report
            =======================
            File Summary:
            - Total Rows: {df.shape[0]}
            - Total Columns: {df.shape[1]}
            - Missing Values: {df.isnull().sum().sum()}

            Basic Statistics:
            {df.describe()}

            Missing Values:
            {df.isnull().sum()}
            """
            st.download_button("Download Report", report, file_name="data_analyzer_report.txt")

    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.write("👋 Please upload a CSV or Excel file to get started.")

# 🔗 Footer
st.markdown("---")
st.markdown("### 🛠️ Built by Muhammad Khizer")
st.markdown("📧 Contact: [emkhizer007@gmail.com](mailto:emkhizer007@gmail.com)")
