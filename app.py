import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Title 
st.title("📊Simple Correlation Analysis Dashboard")

# File uploader 
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # display the first few rows of the dataframe
    st.subheader("Data Preview:")
    st.write(df)

    # display the  number of Rows and Column from the selected data
    st.write('Number of Rows:', df.shape[0])
    st.write('Number of Columns:', df.shape[1])

    # print the null values if those are > 0
    if df.isnull().sum().sum() > 0:
        st.write('Null Values:', df.isnull().sum().sort_values(ascending=False))
    else:
        st.write('No Null Values')

    # display the summary statistics of the selected data
    st.subheader("Summary Statistics:")
    st.write(df.describe())

    # check for numeric columns in dataframe
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    if len(numeric_cols) > 1:
    # Compute correlation matrix
        correlation_matrix = df[numeric_cols].corr()

        # Render the heatmap
        st.subheader("Heatmap:")
        plt.figure(figsize=(10,8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', square=True)
        st.pyplot(plt)

        # Scatter plot input dropdowns
        st.subheader("Scatter Plot:")
        var1 = st.selectbox("Select Variable 1", numeric_cols)
        var2 = st.selectbox("Select Variable 2", numeric_cols)

        # Plot the Scatter plot
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df, x=var1, y=var2)
        plt.title(f'Scatter Plot of {var1} vs {var2}')
        st.pyplot(plt)
    else:
        st.error("The dataset must contain at least two numeric columns.")

# Adding a button
if st.sidebar.button('Greeting'):
    st.sidebar.write('Hi, hello there')

st.markdown("---")
st.caption("Made with ❤️ using Streamlit")

