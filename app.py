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
    "Advertising", "Aerospace Industry", "Agriculture", "Air Pollution", "Arms Industry",
    "Automotive Industry", "Broadcasting", "Chemical Industry", "Computer Industry",
    "Construction Industry", "Creative", "Cultural Industry", "Culture Industry", 
    "Defense Industry", "Democracy", "Design", "Disasters", "Drink Industry", "Ecology", 
    "Education Industry", "Electric Power Industry", "Electronics Industry", "Energy Industry",
    "Entertainment", "Entertainment Industry", "Fashion", "Film Industry", 
    "Financial Services Industry", "Fishing Industry", "Floral", "Food Industry",
    "Gambling Industry", "Healthcare Industry", "Horticulture Industry", "Hospitality Industry", 
    "Hr", "Industrial Robot Industry", "Industrial Waste", "Information Industry",
    "Insurance Industry", "Internet", "Leisure Industry", "Mass Media", "Meat", "Mineral",
    "Mining", "Music Industry", "News Media", "Occupational Injury", "Oil And Gas", 
    "Oil Shale", "Petroleum Industry", "Pharmaceutical Industry", "Professional Services", 
    "Publishing", "Pulp And Paper Industry", "Radio", "Railway", "Raw Material", 
    "Real Estate Industry", "Retail Industry", "Sales", "Semiconductor Industry",
    "Shipbuilding Industry", "Software Industry", "Sport Industry", "Steel Industry",
    "Technology", "Telecommunications", "Television", "Textile Industry", "Tobacco Industry",
    "Trade Association", "Transport Industry", "Video Game Industry", "Water Industry",
    "Wood Industry"
])

final_theme = theme_input.strip() if theme_input else theme_dropdown

# Color Mapping Dataset
theme_palettes = {
    "Advertising": ["#FF6F61", "#FFC107", "#FF3D00", "#FFEB3B", "#E91E63"],
    "Aerospace Industry": ["#003366", "#0D47A1", "#B0BEC5", "#90A4AE", "#81D4FA"],
    "Agriculture": ["#4CAF50", "#8BC34A", "#689F38", "#CDDC39", "#795548"],
    "Air Pollution": ["#7E7E7E", "#B0B0B0", "#5D4037", "#9E9E9E", "#616161"],
    "Arms Industry": ["#5D4037", "#37474F", "#263238", "#546E7A", "#1B5E20"],
    "Automotive Industry": ["#E53935", "#212121", "#757575", "#F57C00", "#0288D1"],
    "Broadcasting": ["#1E88E5", "#1976D2", "#64B5F6", "#0D47A1", "#BBDEFB"],
    "Chemical Industry": ["#FFEB3B", "#FBC02D", "#FF5722", "#795548", "#B71C1C"],
    "Computer Industry": ["#2196F3", "#0288D1", "#00BCD4", "#4CAF50", "#F44336"],
    "Construction Industry": ["#FF9800", "#F57C00", "#6D4C41", "#212121", "#FFEB3B"],
    "Creative": ["#9C27B0", "#E040FB", "#673AB7", "#FF4081", "#00BCD4"],
    "Cultural Industry": ["#FF5722", "#D84315", "#FF7043", "#6D4C41", "#FBC02D"],
    "Culture Industry": ["#795548", "#6D4C41", "#A1887F", "#3E2723", "#D7CCC8"],
    "Defense Industry": ["#37474F", "#263238", "#455A64", "#546E7A", "#1B5E20"],
    "Democracy": ["#1565C0", "#0D47A1", "#64B5F6", "#4DB6AC", "#81C784"],
    "Design": ["#00BCD4", "#0097A7", "#4CAF50", "#FFC107", "#E91E63"],
    "Disasters": ["#F44336", "#D32F2F", "#FF6F00", "#FFEB3B", "#212121"],
    "Drink Industry": ["#6D4C41", "#FF7043", "#4E342E", "#A1887F", "#8D6E63"],
    "Ecology": ["#388E3C", "#4CAF50", "#81C784", "#2E7D32", "#AED581"],
    "Education Industry": ["#1E88E5", "#64B5F6", "#0D47A1", "#4DB6AC", "#FFC107"],
    "Electric Power Industry": ["#FFA000", "#FF6F00", "#FFD54F", "#FFC107", "#F57C00"],
    "Electronics Industry": ["#2196F3", "#0D47A1", "#4FC3F7", "#1976D2", "#0288D1"],
    "Energy Industry": ["#FF5722", "#E64A19", "#FF7043", "#D84315", "#BF360C"],
    "Entertainment": ["#FF4081", "#E040FB", "#9C27B0", "#FF6E40", "#673AB7"],
    "Entertainment Industry": ["#F06292", "#BA68C8", "#9575CD", "#7986CB", "#64B5F6"],
    "Fashion": ["#E91E63", "#C2185B", "#AD1457", "#880E4F", "#F48FB1"],
    "Film Industry": ["#212121", "#616161", "#757575", "#9E9E9E", "#BDBDBD"],
    "Financial Services Industry": ["#0D47A1", "#1565C0", "#1976D2", "#64B5F6", "#90CAF9"],
    "Fishing Industry": ["#0277BD", "#0288D1", "#03A9F4", "#81D4FA", "#4FC3F7"],
    "Floral": ["#E91E63", "#F48FB1", "#CE93D8", "#BA68C8", "#F06292"],
    "Food Industry": ["#FF7043", "#FF5722", "#D84315", "#BF360C", "#E64A19"],
    "Gambling Industry": ["#FFD700", "#FFA000", "#FFC107", "#FFB300", "#FF6F00"],
    "Healthcare Industry": ["#4CAF50", "#81C784", "#388E3C", "#2E7D32", "#A5D6A7"],
    "Horticulture Industry": ["#689F38", "#7CB342", "#9CCC65", "#8BC34A", "#33691E"],
    "Hospitality Industry": ["#F57C00", "#FF9800", "#FFA726", "#FFB74D", "#FFE0B2"],
    "Hr": ["#009688", "#00796B", "#4DB6AC", "#26A69A", "#80CBC4"],
    "Industrial Robot Industry": ["#455A64", "#546E7A", "#607D8B", "#78909C", "#90A4AE"],
    "Industrial Waste": ["#37474F", "#263238", "#455A64", "#546E7A", "#607D8B"],
    "Information Industry": ["#2196F3", "#1976D2", "#64B5F6", "#42A5F5", "#90CAF9"],
    "Insurance Industry": ["#1565C0", "#0D47A1", "#64B5F6", "#1E88E5", "#1976D2"],
    "Internet": ["#4285F4", "#0F9D58", "#DB4437", "#F4B400", "#0F9D58"],
    "Leisure Industry": ["#FF7043", "#FFA726", "#FFB74D", "#FFCC80", "#FFE0B2"],
    "Mass Media": ["#1E88E5", "#1976D2", "#64B5F6", "#90CAF9", "#BBDEFB"],
    "Meat": ["#6D4C41", "#5D4037", "#4E342E", "#3E2723", "#8D6E63"],
    "Mineral": ["#8D6E63", "#A1887F", "#BCAAA4", "#D7CCC8", "#EFEBE9"],
    "Mining": ["#5D4037", "#6D4C41", "#4E342E", "#3E2723", "#8D6E63"],
    "Music Industry": ["#9C27B0", "#673AB7", "#3F51B5", "#2196F3", "#03A9F4"],
    "News Media": ["#1E88E5", "#1976D2", "#1565C0", "#0D47A1", "#BBDEFB"],
    "Occupational Injury": ["#F44336", "#D32F2F", "#E53935", "#B71C1C", "#FFCDD2"],
    "Oil And Gas": ["#FFA000", "#FF6F00", "#F57C00", "#FFB300", "#FFCC80"],
    "Oil Shale": ["#6D4C41", "#5D4037", "#4E342E", "#3E2723", "#8D6E63"],
    "Petroleum Industry": ["#FF6F00", "#FF9800", "#F57C00", "#FFB300", "#FFA726"],
    "Pharmaceutical Industry": ["#4CAF50", "#81C784", "#388E3C", "#2E7D32", "#A5D6A7"],
    "Professional Services": ["#1976D2", "#1565C0", "#0D47A1", "#64B5F6", "#90CAF9"],
    "Publishing": ["#D84315", "#FF7043", "#FF5722", "#BF360C", "#FFCCBC"],
    "Pulp And Paper Industry": ["#6D4C41", "#A1887F", "#BCAAA4", "#D7CCC8", "#EFEBE9"],
    "Radio": ["#1E88E5", "#1976D2", "#64B5F6", "#90CAF9", "#BBDEFB"],
    "Railway": ["#455A64", "#546E7A", "#607D8B", "#78909C", "#90A4AE"],
    "Raw Material": ["#8D6E63", "#A1887F", "#BCAAA4", "#D7CCC8", "#EFEBE9"],
    "Real Estate Industry": ["#3F51B5", "#303F9F", "#283593", "#1A237E", "#C5CAE9"],
    "Retail Industry": ["#FF7043", "#FF5722", "#D84315", "#FF8A65", "#FFCCBC"],
    "Sales": ["#FF9800", "#F57C00", "#FFB300", "#FFA726", "#FFCC80"],
    "Semiconductor Industry": ["#2196F3", "#0288D1", "#03A9F4", "#4FC3F7", "#81D4FA"],
    "Shipbuilding Industry": ["#0277BD", "#01579B", "#039BE5", "#0288D1", "#4FC3F7"],
    "Software Industry": ["#00BCD4", "#0097A7", "#4DD0E1", "#26C6DA", "#80DEEA"],
    "Sport Industry": ["#D32F2F", "#C2185B", "#1976D2", "#388E3C", "#FBC02D"],
    "Steel Industry": ["#607D8B", "#455A64", "#37474F", "#546E7A", "#90A4AE"],
    "Technology": ["#2196F3", "#1976D2", "#0288D1", "#03A9F4", "#64B5F6"],
    "Telecommunications": ["#1E88E5", "#1976D2", "#0D47A1", "#64B5F6", "#90CAF9"],
    "Television": ["#1E88E5", "#1976D2", "#64B5F6", "#90CAF9", "#BBDEFB"],
    "Textile Industry": ["#FF7043", "#FF5722", "#F4511E", "#E64A19", "#D84315"],
    "Tobacco Industry": ["#5D4037", "#6D4C41", "#4E342E", "#3E2723", "#8D6E63"],
    "Trade Association": ["#1565C0", "#0D47A1", "#1976D2", "#64B5F6", "#90CAF9"],
    "Transport Industry": ["#0277BD", "#01579B", "#039BE5", "#0288D1", "#4FC3F7"],
    "Video Game Industry": ["#9C27B0", "#673AB7", "#3F51B5", "#2196F3", "#03A9F4"],
    "Water Industry": ["#0288D1", "#03A9F4", "#81D4FA", "#4FC3F7", "#81C784"],
    "Wood Industry": ["#6D4C41", "#5D4037", "#4E342E", "#3E2723", "#8D6E63"],
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
