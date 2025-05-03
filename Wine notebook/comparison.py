import streamlit as st
import pandas as pd
import plotly.express as px

def wine_comparison():
    st.title("Wine Comparison - Red vs White")
    
    # Load the data for both red and white wines
    df_red = pd.read_excel("WineData/winequality-red.xlsx", header=1)
    df_white = pd.read_excel("WineData/winequality-white.xlsx", header=1)
    
    # Clean up column names (strip spaces)
    df_red.columns = df_red.columns.str.strip()
    df_white.columns = df_white.columns.str.strip()

    # Show a preview of both datasets
    st.subheader("Red Wine Preview")
    st.write(df_red.head())  # Preview red wine data

    st.subheader("White Wine Preview")
    st.write(df_white.head())  # Preview white wine data

    # Compare Quality Distribution
    st.subheader("Quality Distribution Comparison")
    fig1 = px.histogram(df_red, x="quality", nbins=10, title="Red Wine Quality Distribution", opacity=0.7)
    fig2 = px.histogram(df_white, x="quality", nbins=10, title="White Wine Quality Distribution", opacity=0.7)
    
    # Display both histograms in one plot for easy comparison
    st.plotly_chart(fig1)
    st.plotly_chart(fig2)

    # Compare Alcohol Content
    st.subheader("Alcohol Content Comparison")
    fig3 = px.box(df_red, y="alcohol", title="Red Wine Alcohol Content")
    fig4 = px.box(df_white, y="alcohol", title="White Wine Alcohol Content")
    
    # Display both boxplots side by side
    st.plotly_chart(fig3)
    st.plotly_chart(fig4)

    # Compare Correlations (Example: correlation of alcohol and quality)
    st.subheader("Correlation Comparison (Alcohol vs Quality)")
    
    # Red Wine Correlation
    fig5 = px.scatter(df_red, x="alcohol", y="quality", title="Red Wine Alcohol vs Quality")
    # White Wine Correlation
    fig6 = px.scatter(df_white, x="alcohol", y="quality", title="White Wine Alcohol vs Quality")
    
    st.plotly_chart(fig5)
    st.plotly_chart(fig6)

    # Other possible comparisons can be added like pH, acidity, etc.
