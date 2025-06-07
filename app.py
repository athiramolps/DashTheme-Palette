import streamlit as st

# Title and Description with 🎨 icon
st.set_page_config(page_title="DashTheme Palette", layout="wide")
st.markdown("""
    <h1 style='text-align: center; color: #4A90E2;'>🎨 DashTheme Palette</h1>
    <p style='text-align: center; font-size: 18px;'>An intelligent color recommender app for dashboards and branding based on your selected theme or industry.</p>
""", unsafe_allow_html=True)

# Theme Input
st.write("### Enter a Theme or Choose from the Dropdown:")
col1, col2 = st.columns([2, 1])
with col1:
    theme_input = st.text_input("Type a theme like 'Healthcare', 'Retail', etc.").strip().lower()
with col2:
    theme_dropdown = st.selectbox("Or select a theme:", options=[
        "Advertising", "Aerospace Industry", "Agriculture", "Air Pollution", "Arms Industry",
        "Automotive Industry", "Broadcasting", "Chemical Industry", "Computer Industry",
        "Construction Industry", "Creative", "Cultural Industry", "Culture Industry", 
        "Defense Industry", "Democracy", "Design", "Disasters", "Drink Industry", "Ecology", 
        "Education Industry", "Electric Power Industry", "Electronics Industry", "Energy Industry",
        "Entertainment", "Fashion", "Film Industry", 
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
    theme_dropdown = theme_dropdown.strip().lower()

# Decide final theme in lowercase to normalize matching
final_theme = theme_input if theme_input else theme_dropdown

# Color Mapping Dataset with lowercase keys
theme_palettes = {
    "advertising": ["#FF6F61", "#FFC107", "#FF3D00", "#FFEB3B", "#E91E63"],
    "aerospace industry": ["#003366", "#0D47A1", "#B0BEC5", "#90A4AE", "#81D4FA"],
    "agriculture": ["#4CAF50", "#8BC34A", "#689F38", "#CDDC39", "#795548"],
    "air pollution": ["#7E7E7E", "#B0B0B0", "#5D4037", "#9E9E9E", "#616161"],
    "arms industry": ["#5D4037", "#37474F", "#263238", "#546E7A", "#1B5E20"],
    "automotive industry": ["#E53935", "#212121", "#757575", "#F57C00", "#0288D1"],
    "broadcasting": ["#1E88E5", "#1976D2", "#64B5F6", "#0D47A1", "#BBDEFB"],
    "chemical industry": ["#FFEB3B", "#FBC02D", "#FF5722", "#795548", "#B71C1C"],
    "computer industry": ["#2196F3", "#0288D1", "#00BCD4", "#4CAF50", "#F44336"],
    "construction industry": ["#FF9800", "#F57C00", "#6D4C41", "#212121", "#FFEB3B"],
    "creative": ["#9C27B0", "#E040FB", "#673AB7", "#FF4081", "#00BCD4"],
    "cultural industry": ["#FF5722", "#D84315", "#FF7043", "#6D4C41", "#FBC02D"],
    "culture industry": ["#795548", "#6D4C41", "#A1887F", "#3E2723", "#D7CCC8"],
    "defense industry": ["#37474F", "#263238", "#455A64", "#546E7A", "#1B5E20"],
    "democracy": ["#1565C0", "#0D47A1", "#64B5F6", "#4DB6AC", "#81C784"],
    "design": ["#00BCD4", "#0097A7", "#4CAF50", "#FFC107", "#E91E63"],
    "disasters": ["#F44336", "#D32F2F", "#FF6F00", "#FFEB3B", "#212121"],
    "drink industry": ["#6D4C41", "#FF7043", "#4E342E", "#A1887F", "#8D6E63"],
    "ecology": ["#388E3C", "#4CAF50", "#81C784", "#2E7D32", "#AED581"],
    "education industry": ["#1E88E5", "#64B5F6", "#0D47A1", "#4DB6AC", "#FFC107"],
    "electric power industry": ["#FFA000", "#FF6F00", "#FFD54F", "#FFC107", "#F57C00"],
    "electronics industry": ["#2196F3", "#0D47A1", "#4FC3F7", "#1976D2", "#0288D1"],
    "energy industry": ["#FF5722", "#E64A19", "#FF7043", "#D84315", "#BF360C"],
    "entertainment": ["#FF4081", "#E040FB", "#9C27B0", "#FF6E40", "#673AB7"],
    "fashion": ["#E91E63", "#C2185B", "#AD1457", "#880E4F", "#F48FB1"],
    "film industry": ["#212121", "#616161", "#757575", "#9E9E9E", "#BDBDBD"],
    "financial services industry": ["#0D47A1", "#1565C0", "#1976D2", "#64B5F6", "#90CAF9"],
    "fishing industry": ["#0277BD", "#0288D1", "#03A9F4", "#81D4FA", "#4FC3F7"],
    "floral": ["#E91E63", "#F48FB1", "#CE93D8", "#BA68C8", "#F06292"],
    "food industry": ["#FF7043", "#FF5722", "#D84315", "#BF360C", "#E64A19"],
    "gambling industry": ["#FFD700", "#FFA000", "#FFC107", "#FFB300", "#FF6F00"],
    "healthcare industry": ["#4CAF50", "#81C784", "#388E3C", "#2E7D32", "#A5D6A7"],
    "horticulture industry": ["#689F38", "#7CB342", "#9CCC65", "#8BC34A", "#33691E"],
    "hospitality industry": ["#F57C00", "#FF9800", "#FFA726", "#FFB74D", "#FFE0B2"],
    "hr": ["#009688", "#00796B", "#4DB6AC", "#26A69A", "#80CBC4"],
    "industrial robot industry": ["#455A64", "#546E7A", "#607D8B", "#78909C", "#90A4AE"],
    "industrial waste": ["#37474F", "#263238", "#455A64", "#546E7A", "#607D8B"],
    "information industry": ["#2196F3", "#1976D2", "#64B5F6", "#42A5F5", "#90CAF9"],
    "insurance industry": ["#1565C0", "#0D47A1", "#64B5F6", "#1E88E5", "#1976D2"],
    "internet": ["#4285F4", "#0F9D58", "#DB4437", "#F4B400", "#0F9D58"],
    "leisure industry": ["#FF7043", "#FFA726", "#FFB74D", "#FFCC80", "#FFE0B2"],
    "mass media": ["#1E88E5", "#1976D2", "#64B5F6", "#90CAF9", "#BBDEFB"],
    "meat": ["#6D4C41", "#5D4037", "#4E342E", "#3E2723", "#8D6E63"],
    "mineral": ["#8D6E63", "#A1887F", "#BCAAA4", "#D7CCC8", "#EFEBE9"],
    "mining": ["#5D4037", "#6D4C41", "#4E342E", "#3E2723", "#8D6E63"],
    "music industry": ["#9C27B0", "#673AB7", "#3F51B5", "#2196F3", "#03A9F4"],
    "news media": ["#1E88E5", "#1976D2", "#1565C0", "#0D47A1", "#BBDEFB"],
    "occupational injury": ["#F44336", "#D32F2F", "#E53935", "#B71C1C", "#FFCDD2"],
    "oil and gas": ["#FFA000", "#FF6F00", "#F57C00", "#FFB300", "#FFCC80"],
    "oil shale": ["#6D4C41", "#5D4037", "#4E342E", "#3E2723", "#8D6E63"],
    "petroleum industry": ["#FF6F00", "#FF9800", "#F57C00", "#FFB300", "#FFA726"],
    "pharmaceutical industry": ["#4CAF50", "#81C784", "#388E3C", "#2E7D32", "#A5D6A7"],
    "professional services": ["#1976D2", "#1565C0", "#0D47A1", "#64B5F6", "#90CAF9"],
    "publishing": ["#D84315", "#FF7043", "#FF5722", "#BF360C", "#FFCCBC"],
    "pulp and paper industry": ["#6D4C41", "#A1887F", "#BCAAA4", "#D7CCC8", "#EFEBE9"],
    "radio": ["#1E88E5", "#1976D2", "#64B5F6", "#90CAF9", "#BBDEFB"],
    "railway": ["#455A64", "#546E7A", "#607D8B", "#78909C", "#90A4AE"],
    "raw material": ["#8D6E63", "#A1887F", "#BCAAA4", "#D7CCC8", "#EFEBE9"],
    "real estate industry": ["#3F51B5", "#303F9F", "#283593", "#1A237E", "#C5CAE9"],
    "retail industry": ["#FF7043", "#FF5722", "#D84315", "#FF8A65", "#FFCCBC"],
    "sales": ["#FF9800", "#F57C00", "#FFB300", "#FFA726", "#FFCC80"],
    "semiconductor industry": ["#2196F3", "#0288D1", "#03A9F4", "#4FC3F7", "#81D4FA"],
    "shipbuilding industry": ["#0277BD", "#01579B", "#039BE5", "#0288D1", "#4FC3F7"],
    "software industry": ["#00BCD4", "#0097A7", "#4DD0E1", "#26C6DA", "#80DEEA"],
    "sport industry": ["#D32F2F", "#C2185B", "#1976D2", "#388E3C", "#FBC02D"],
    "steel industry": ["#607D8B", "#455A64", "#37474F", "#546E7A", "#90A4AE"],
    "technology": ["#2196F3", "#1976D2", "#0288D1", "#03A9F4", "#64B5F6"],
    "telecommunications": ["#1E88E5", "#1976D2", "#0D47A1", "#64B5F6", "#90CAF9"],
    "television": ["#1E88E5", "#1976D2", "#64B5F6", "#90CAF9", "#BBDEFB"],
    "textile industry": ["#FF7043", "#FF5722", "#F4511E", "#E64A19", "#D84315"],
    "tobacco industry": ["#5D4037", "#6D4C41", "#4E342E", "#3E2723", "#8D6E63"],
    "trade association": ["#1565C0", "#0D47A1", "#1976D2", "#64B5F6", "#90CAF9"],
    "transport industry": ["#0277BD", "#01579B", "#039BE5", "#0288D1", "#4FC3F7"],
    "video game industry": ["#9C27B0", "#673AB7", "#3F51B5", "#2196F3", "#03A9F4"],
    "water industry": ["#0288D1", "#03A9F4", "#81D4FA", "#4FC3F7", "#81C784"],
    "wood industry": ["#6D4C41", "#5D4037", "#4E342E", "#3E2723", "#8D6E63"],
}

# Display Palette
if final_theme in theme_palettes:
    colors = theme_palettes[final_theme]
    st.subheader(f"Recommended Colors for: {final_theme.title()}")
    cols = st.columns(len(colors))
    for i, color in enumerate(colors):
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
