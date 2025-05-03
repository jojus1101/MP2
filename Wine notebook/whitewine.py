import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns

def white_wine_analysis():
    # Load the white wine data with the correct header row (index 1)
    df_white = pd.read_excel("WineData/winequality-white.xlsx", header=1)

    # Clean up column names (strip spaces)
    df_white.columns = df_white.columns.str.strip()

    # Display the first few rows of data to ensure it is correctly loaded
    st.title('White Wine Quality Analysis')
    st.subheader("White Wine Data Preview")
    st.write(df_white.head())

    # Allow sorting the dataframe by columns
    st.subheader("White Wine Data (Sortable)")
    st.dataframe(df_white.sort_values(by="quality"))

    # 2D Plot - Histogram for White Wine Quality
    st.subheader("White Wine - Quality Distribution")
    fig4 = px.histogram(df_white, x="quality", nbins=10, title="White Wine Quality Distribution")
    st.plotly_chart(fig4)

    # 2D Scatter Plot for Alcohol vs Quality
    st.subheader("White Wine - Alcohol vs Quality")
    fig5 = px.scatter(df_white, x="alcohol", y="quality", title="White Wine Alcohol vs Quality")
    st.plotly_chart(fig5)

    # 3D Plot for Alcohol, Volatile Acidity, and Quality
    st.subheader("White Wine - 3D Plot (Alcohol, Volatile Acidity, Quality)")
    fig6 = px.scatter_3d(df_white, x="alcohol", y="volatile acidity", z="quality", color="quality", 
                         title="White Wine 3D Scatter Plot (Alcohol, Volatile Acidity, Quality)")
    st.plotly_chart(fig6)

    # Correlation Matrix
    st.subheader("Correlation Matrix (White Wine)")
    corr_white = df_white.corr()
    st.write(corr_white)

    # Show Pairplot (optional, requires seaborn)
    st.subheader("White Wine Pairplot")
    pairplot_white = sns.pairplot(df_white)
    st.pyplot(pairplot_white)
