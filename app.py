import streamlit as st
from PIL import Image

# Title and Description
st.set_page_config(page_title="DashTheme Palette", layout="wide")
st.markdown("""
    <h1 style='text-align: center; color: #4A90E2;'>DashTheme Palette</h1>
    <p style='text-align: center; font-size: 18px;'>An intelligent color recommender app for dashboards and branding based on your selected theme or industry.</p>
""", unsafe_allow_html=True)

# Theme Input
st.write("### Enter a Theme or Choose from the Dropdown:")
col1, col2 = st.columns([2, 1])
with col1:
    theme_input = st.text_input("Type a theme like 'Healthcare', 'Retail', etc.")
with col2:
    theme_dropdown = st.selectbox("Or select a theme:", options=[
        "Agriculture", "Fishing", "Horticulture", "Tobacco", "Wood", "Mining", "Oil & Gas",
        "Automotive", "Aerospace", "Chemical", "Pharmaceutical", "Construction", "Electronics",
        "Textile", "Steel", "Shipbuilding", "Food", "Drink", "Industrial Robots",
        "Healthcare", "Financial Services", "Insurance", "Education", "Retail", "Real Estate",
        "Marketing", "Digital Marketing", "Hospitality", "E-commerce", "Supply Chain",
        "Logistics", "Crimes / Justice", "Fashion", "Film / Cinema", "Music", "Advertising",
        "Software/IT", "Entertainment", "Gaming", "Diamond Industry", "Gold Industry",
        "Petroleum", "Environment / NGO", "Government / Public", "Cybersecurity"])

final_theme = theme_input.strip() if theme_input else theme_dropdown

# Color Mapping Dataset
theme_palettes = {
    "Agriculture": ["#6B8E23", "#A0522D", "#F5F5DC", "#FFFF00"],
    "Fishing": ["#4682B4", "#00FFFF", "#008080", "#FFFFFF"],
    "Horticulture": ["#228B22", "#FFC0CB", "#9370DB", "#FFFFE0"],
    "Tobacco": ["#8B4513", "#F5F5DC", "#808000", "#800000"],
    "Wood": ["#A0522D", "#D2B48C", "#228B22", "#36454F"],
    "Mining": ["#000000", "#808080", "#B7410E", "#A0522D"],
    "Oil & Gas": ["#000000", "#003366", "#FF8C00", "#708090"],
    "Automotive": ["#C0C0C0", "#FF0000", "#000000", "#4682B4"],
    "Aerospace": ["#000080", "#FFFFFF", "#1E90FF", "#B0C4DE"],
    "Chemical": ["#800080", "#00FFFF", "#00FF00", "#FFFFFF"],
    "Pharmaceutical": ["#1E90FF", "#FFFFFF", "#7FFFD4", "#98FB98"],
    "Construction": ["#FFD700", "#808080", "#FFA500", "#FFFFFF"],
    "Electronics": ["#000000", "#0000FF", "#00FFFF", "#C0C0C0"],
    "Textile": ["#FFDAB9", "#E6E6FA", "#FF7F50", "#F5F5F5"],
    "Steel": ["#808080", "#C0C0C0", "#B7410E", "#000000"],
    "Shipbuilding": ["#000080", "#808080", "#FFFFFF", "#008080"],
    "Food": ["#FF0000", "#FFFF00", "#8B4513", "#228B22"],
    "Drink": ["#00FFFF", "#FFA500", "#00FF00", "#00008B"],
    "Industrial Robots": ["#A9A9A9", "#00FFFF", "#000000", "#FFFF00"],
    "Healthcare": ["#1E90FF", "#FFFFFF", "#008000", "#7FFFD4"],
    "Financial Services": ["#00008B", "#FFD700", "#228B22", "#FFFFFF"],
    "Insurance": ["#000080", "#D3D3D3", "#228B22"],
    "Education": ["#0000FF", "#FFA500", "#FF0000", "#F5F5DC"],
    "Retail": ["#FF0000", "#FFA500", "#FFFF00", "#FFFFFF"],
    "Real Estate": ["#228B22", "#808080", "#F5F5DC", "#1E90FF"],
    "Marketing": ["#FF0000", "#800080", "#000000", "#FFFFFF"],
    "Digital Marketing": ["#FF7F50", "#20B2AA", "#9370DB"],
    "Hospitality": ["#FFD700", "#800000", "#FFFDD0", "#808000"],
    "E-commerce": ["#0000FF", "#FFFF00", "#00FFFF", "#FFFFFF"],
    "Supply Chain": ["#A0522D", "#000080", "#808080", "#FFA500"],
    "Logistics": ["#0000FF", "#FF0000", "#808080", "#000000"],
    "Crimes / Justice": ["#00008B", "#000000", "#FF0000", "#FFFFFF"],
    "Fashion": ["#000000", "#FFFFFF", "#B76E79", "#FFB6C1"],
    "Film / Cinema": ["#2F4F4F", "#FFD700", "#800000", "#000000"],
    "Music": ["#800080", "#00FFFF", "#000000", "#39FF14"],
    "Advertising": ["#FF0000", "#FFA500", "#0000FF", "#800080"],
    "Software/IT": ["#0000FF", "#800080", "#008080", "#000000"],
    "Entertainment": ["#FF69B4", "#8A2BE2", "#000000", "#FFFFFF"],
    "Gaming": ["#39FF14", "#800080", "#000000", "#FFA500"],
    "Diamond Industry": ["#FFFFFF", "#1E90FF", "#808080", "#C0C0C0"],
    "Gold Industry": ["#FFD700", "#8B4513", "#000000", "#F7E7CE"],
    "Petroleum": ["#000000", "#FFA500", "#708090", "#FF0000"],
    "Environment / NGO": ["#228B22", "#F5F5DC", "#87CEEB", "#FFFFFF"],
    "Government / Public": ["#1E90FF", "#808080", "#F5F5DC", "#000080"],
    "Cybersecurity": ["#4B0082", "#000080", "#FF0000", "#000000"]
}

# Display Palette
if final_theme in theme_palettes:
    st.subheader(f"Recommended Colors for: {final_theme}")
    cols = st.columns(len(theme_palettes[final_theme]))
    for i, color in enumerate(theme_palettes[final_theme]):
        with cols[i]:
            st.markdown(f"""
                <div style='background-color: {color}; width: 100%; height: 100px; border-radius: 8px;'></div>
                <p style='text-align: center; font-size: 16px;'>{color}</p>
            """, unsafe_allow_html=True)
else:
    if final_theme:
        st.warning("Theme not found. Please try another or select from the dropdown.")

# Note
st.markdown("""
    <p style='margin-top:30px; color:gray;'><strong>NB:</strong> Some services may choose to follow their brand colors instead of the theme-recommended palette.</p>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
    <hr>
    <p style='text-align: center; color:gray;'>Designed by Athiramol PS</p>
""", unsafe_allow_html=True)
