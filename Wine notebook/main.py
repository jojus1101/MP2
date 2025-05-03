import streamlit as st
import redwine
import whitewine
import comparison

# Sidebar for navigation
st.sidebar.title("Wine Quality Analysis")
page = st.sidebar.radio("Select a page:", ["Wines", "Red Wine", "White Wine", "Wine Comparison"])

# Main Page - Info About Wines
if page == "Wines":
    st.title("Welcome to the Wine Quality Analysis")
    st.header("Introduction to Wines")

    st.subheader("Red Wine")
    st.write("""
        Red wine is made from dark-colored (black) grape varieties. The color of the wine can range from intense violet to brick red, and brown, as the wine ages. 
        Red wine is rich in antioxidants and can vary greatly depending on the region, grape variety, and winemaking techniques. Works well with red meats and hearty dishes.
    """)
    
    st.subheader("White Wine")
    st.write("""
        White wine is made from green or yellowish grapes, and sometimes even from red grapes (the skin is discarded before fermentation). 
        It is typically lighter than red wine, and it can range from very dry to sweet, depending on the type of grape used and fermentation process. Works well with seafood, poultry, and light dishes.
    """)

    st.subheader("Why Analyze Wine Quality?")
    st.write("""
        Analyzing wine quality helps winemakers and consumers understand the key factors that influence the flavor, aroma, and overall quality of the wine. 
        Factors like alcohol content, acidity, residual sugar, and other chemical components play an essential role in defining the wine's characteristics.
    """)

    st.subheader("In This App")
    st.write("""
        This app allows you to explore data on red and white wines, focusing on factors such as alcohol content, acidity, and quality. 
        You can view in-depth analysis for both types of wines and compare them to better understand their similarities and differences.
    """)

# Red Wine Page
elif page == "Red Wine":
    redwine.red_wine_analysis()  # This will call the red wine analysis function

# White Wine Page
elif page == "White Wine":
    whitewine.white_wine_analysis()  # This will call the white wine analysis function

# Wine Comparison Page
elif page == "Wine Comparison":
    comparison.wine_comparison()  # This will call the comparison analysis function
