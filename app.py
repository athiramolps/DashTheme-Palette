import streamlit as st

# Page config
st.set_page_config(page_title="DashTheme Palette", layout="wide")

# Title and description
st.markdown("""
    <h1 style='text-align: center; color: #4A90E2;'>DashTheme Palette</h1>
    <p style='text-align: center; font-size: 18px;'>An intelligent color recommender app for dashboards and branding based on your selected theme or industry.</p>
""", unsafe_allow_html=True)

# Input area with two columns
st.write("### Enter a Theme or Choose from the Dropdown:")
col1, col2 = st.columns([2, 1])

with col1:
    theme_input = st.text_input("Type a theme like 'Healthcare', 'Retail', etc.")
with col2:
    theme_dropdown = st.selectbox(
        "Or select a theme:",
        options=[
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
        ]
    )

final_theme = theme_input.strip() if theme_input else theme_dropdown

# Theme palettes dictionary (shortened example)
theme_palettes = {
    "Advertising": ["#FF6F61", "#FFC107", "#FF3D00", "#FFEB3B", "#E91E63"],
    "Aerospace Industry": ["#003366", "#0D47A1", "#B0BEC5", "#90A4AE", "#81D4FA"],
    "Agriculture": ["#4CAF50", "#8BC34A", "#689F38", "#CDDC39", "#795548"],
    # ... (include the full dictionary you have) ...
    "Wood Industry": ["#6D4C41", "#5D4037", "#4E342E", "#3E2723", "#8D6E63"],
}

# Display recommended palette if available
if final_theme in theme_palettes:
    st.subheader(f"Recommended Colors for: {final_theme}")
    cols = st.columns(len(theme_palettes[final_theme]))
    for i, color in enumerate(theme_palettes[final_theme]):
        with cols[i]:
            st.markdown(f"""
                <div style='background-color: {color}; width: 100%; height: 100px; border-radius: 8px;'></div>
                <p style='text-align: center; font-size: 16px;'>{color}</p>
            """, unsafe_allow_html=True)
elif final_theme:
    st.warning("Theme not found. Please try another or select from the dropdown.")

# Note section
st.markdown("""
    <p style='margin-top:30px; color:gray;'><strong>NB:</strong> Some services may choose to follow their brand colors instead of the theme-recommended palette.</p>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
    <hr>
    <p style='text-align: center; color:gray;'>Designed by Athiramol PS</p>
""", unsafe_allow_html=True)
