import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns

def red_wine_analysis():
    # Load the red wine data with the correct header row (index 1)
    df_red = pd.read_excel("WineData/winequality-red.xlsx", header=1)

    # Clean up column names (strip spaces)
    df_red.columns = df_red.columns.str.strip()

    # Display the first few rows of data to ensure it is correctly loaded
    st.title('Red Wine Quality Analysis')
    st.subheader("Red Wine Data Preview")
    st.write(df_red.head())

    # Allow sorting the dataframe by columns
    st.subheader("Red Wine Data (Sortable)")
    st.dataframe(df_red.sort_values(by="quality"))

    # 2D Plot - Histogram for Red Wine Quality
    st.subheader("Red Wine - Quality Distribution")
    fig1 = px.histogram(df_red, x="quality", nbins=10, title="Red Wine Quality Distribution")
    st.plotly_chart(fig1)

    # 2D Scatter Plot for Alcohol vs Quality
    st.subheader("Red Wine - Alcohol vs Quality")
    fig2 = px.scatter(df_red, x="alcohol", y="quality", title="Red Wine Alcohol vs Quality")
    st.plotly_chart(fig2)

    # 3D Plot for Alcohol, Volatile Acidity, and Quality
    st.subheader("Red Wine - 3D Plot (Alcohol, Volatile Acidity, Quality)")
    fig3 = px.scatter_3d(df_red, x="alcohol", y="volatile acidity", z="quality", color="quality", 
                         title="Red Wine 3D Scatter Plot (Alcohol, Volatile Acidity, Quality)")
    st.plotly_chart(fig3)

    # Correlation Matrix
    st.subheader("Correlation Matrix (Red Wine)")
    corr_red = df_red.corr()
    st.write(corr_red)

    # Show Pairplot (optional, requires seaborn)
    st.subheader("Red Wine Pairplot")
    pairplot_red = sns.pairplot(df_red)
    st.pyplot(pairplot_red)
