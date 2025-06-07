import streamlit as st

st.set_page_config(page_title="DashTheme Palette", layout="wide")

st.markdown("""
    <h1 style='text-align: center; color: #4A90E2;'>DashTheme Palette</h1>
    <p style='text-align: center; font-size: 18px;'>An intelligent color recommender app for dashboards and branding based on your selected theme or industry.</p>
""", unsafe_allow_html=True)

# Full list of themes (make sure this matches keys in the dictionary exactly)
themes = [
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

theme_input = st.text_input("Type a theme like 'Healthcare', 'Retail', etc.")
theme_dropdown = st.selectbox("Or select a theme:", options=themes)

# Normalize user input
def normalize(s):
    return s.strip().lower()

final_theme_input = normalize(theme_input) if theme_input else ""
final_theme_dropdown = normalize(theme_dropdown) if theme_dropdown else ""

# Your color palette dictionary keys should match the themes list exactly
theme_palettes = {
    "Advertising": ["#FF6F61", "#FFC107", "#FF3D00", "#FFEB3B", "#E91E63"],
    "Aerospace Industry": ["#003366", "#0D47A1", "#B0BEC5", "#90A4AE", "#81D4FA"],
    "Agriculture": ["#4CAF50", "#8BC34A", "#689F38", "#CDDC39", "#795548"],
    # ... add the full dictionary here matching all themes ...
    "Wood Industry": ["#6D4C41", "#5D4037", "#4E342E", "#3E2723", "#8D6E63"],
}

# Create a lookup mapping from normalized theme to original key
normalized_to_key = {normalize(k): k for k in theme_palettes.keys()}

# Determine which theme to use
selected_theme_norm = final_theme_input or final_theme_dropdown

if selected_theme_norm in normalized_to_key:
    selected_theme_key = normalized_to_key[selected_theme_norm]
    st.subheader(f"Recommended Colors for: {selected_theme_key}")
    colors = theme_palettes[selected_theme_key]
    cols = st.columns(len(colors))
    for i, color in enumerate(colors):
        with cols[i]:
            st.markdown(f"""
                <div style='background-color: {color}; width: 100%; height: 100px; border-radius: 8px;'></div>
                <p style='text-align: center; font-size: 16px;'>{color}</p>
            """, unsafe_allow_html=True)
elif theme_input or theme_dropdown:
    st.warning("Theme not found. Please check spelling or select from the dropdown.")

st.markdown("""
    <p style='margin-top:30px; color:gray;'><strong>NB:</strong> Some services may choose to follow their brand colors instead of the theme-recommended palette.</p>
""", unsafe_allow_html=True)

st.markdown("""
    <hr>
    <p style='text-align: center; color:gray;'>Designed by Athiramol PS</p>
""", unsafe_allow_html=True)
