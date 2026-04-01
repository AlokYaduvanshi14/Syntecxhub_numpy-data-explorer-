import streamlit as st
import pandas as pd

st.title("Data Explorer")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write("### Data preview")
    st.write(df)

    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

    if len(numeric_cols) == 0:
        st.warning("No numeric columns found in the uploaded CSV.")
    else:
        col = st.selectbox("Select column for analysis", numeric_cols)

        st.write("### Statistics")
        st.write(df[col].describe())

        min_data = float(df[col].min())
        max_data = float(df[col].max())
        min_value, max_value = st.slider(
            "Select value range",
            min_value=min_data,
            max_value=max_data,
            value=(min_data, max_data),
        )

        filtered_df = df[(df[col] >= min_value) & (df[col] <= max_value)]

        st.write("### Filtered data")
        st.write(filtered_df)