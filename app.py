import pandas as pd
import streamlit as st

st.set_page_config(page_title="Excel Dashboard", layout="wide")
st.title("📊 Quick Excel Data Dashboard")

uploaded_file = st.file_uploader("Upload Excel File (.xlsx)", type=["xlsx"])

if uploaded_file is not None:
  df = pd.read_excel(uploaded_file)

  st.subheader("📈 Summary Metrics")
  col1, col2, col3 = st.columns(3)
  col1.metric("Total Rows", df.shape[0])
  col2.metric("Total Columns", df.shape[1])

  numeric_cols = df.select_dtypes(include=["number"]).columns
  if len(numeric_cols) > 0:
    selected_col = st.selectbox("Select metric for summary & chart", numeric_cols)
    col3.metric(
        f"Total {selected_col}", f"{df[selected_col].sum():,.2f}"
    )

    st.subheader("🔍 Dataset Preview")
    st.dataframe(df, use_container_width=True)

    st.subheader("📊 Chart")
    st.bar_chart(df[selected_col])
  else:
    st.subheader("🔍 Dataset Preview")
    st.dataframe(df, use_container_width=True)
    st.warning("⚠️ No numeric columns found in this Excel file.")
else:
  st.warning("⚠️ Please upload your Excel file to view the dashboard.")