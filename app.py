import streamlit as st

# Extended theme-to-palette mapping
theme_palettes = {
    "hospital": ["#0000FF", "#FFFFFF", "#008000", "#00FFFF"],
    "retail": ["#FF0000", "#FFA500", "#FFFF00", "#FFFFFF"],
    "nature": ["#008000", "#A52A2A", "#F5F5DC", "#FFFF00"],
    "technology": ["#0000FF", "#800080", "#008080", "#000000"],
    "marketing": ["#FF0000", "#800080", "#000000", "#FFFFFF"],
    "education": ["#0000FF", "#FFA500", "#FF0000", "#F5F5DC"],
    "finance": ["#00008B", "#FFD700", "#008000", "#FFFFFF"],
    "fashion": ["#000000", "#FFFFFF", "#B76E79", "#FFC0CB"],
    "healthcare": ["#0000FF", "#FFFFFF", "#008000", "#00FFFF"],
    "environment": ["#008000", "#F5F5DC", "#87CEEB", "#FFFFFF"],
    "agriculture": ["#228B22", "#A0522D", "#F5F5DC", "#FFFF00"],
    "fishing": ["#1E90FF", "#00FFFF", "#008080", "#FFFFFF"],
    "horticulture": ["#228B22", "#FFC0CB", "#800080", "#FFFFE0"],
    "tobacco": ["#A52A2A", "#F5F5DC", "#808000", "#800000"],
    "wood": ["#8B4513", "#D2B48C", "#228B22", "#36454F"],
    "mining": ["#000000", "#808080", "#B7410E", "#A0522D"],
    "oil and gas": ["#000000", "#00008B", "#FF8C00", "#708090"],
    "automotive": ["#C0C0C0", "#FF0000", "#000000", "#4682B4"],
    "aerospace": ["#0000FF", "#FFFFFF", "#000080", "#87CEEB"],
    "chemical": ["#800080", "#00FFFF", "#00FF00", "#FFFFFF"],
    "pharmaceutical": ["#0000FF", "#FFFFFF", "#00FFFF", "#90EE90"],
    "construction": ["#FFFF00", "#808080", "#FFA500", "#FFFFFF"],
    "electronics": ["#000000", "#0000FF", "#00FFFF", "#C0C0C0"],
    "textile": ["#FFDAB9", "#E6E6FA", "#FF7F50", "#FFF0F5"],
    "steel": ["#808080", "#C0C0C0", "#B7410E", "#000000"],
    "shipbuilding": ["#000080", "#808080", "#FFFFFF", "#008080"],
    "food": ["#FF0000", "#FFFF00", "#A52A2A", "#008000"],
    "drink": ["#00FFFF", "#FFA500", "#00FF00", "#00008B"],
    "industrial robots": ["#A9A9A9", "#00FFFF", "#000000", "#FFFF00"],
    "financial services": ["#00008B", "#FFD700", "#008000", "#FFFFFF"],
    "insurance": ["#000080", "#D3D3D3", "#228B22"],
    "real estate": ["#008000", "#808080", "#F5F5DC", "#0000FF"],
    "digital marketing": ["#FF7E5F", "#00CED1", "#800080"],
    "hospitality": ["#FFD700", "#800000", "#FFFDD0", "#808000"],
    "e-commerce": ["#0000FF", "#FFFF00", "#00FFFF", "#FFFFFF"],
    "supply chain": ["#A0522D", "#000080", "#808080", "#FFA500"],
    "logistics": ["#0000FF", "#FF0000", "#808080", "#000000"],
    "crimes": ["#00008B", "#000000", "#FF0000", "#FFFFFF"],
    "film": ["#2F4F4F", "#FFD700", "#800000", "#000000"],
    "music": ["#800080", "#00FFFF", "#000000", "#FF1493"],
    "advertising": ["#FF0000", "#FFA500", "#0000FF", "#800080"],
    "software": ["#0000FF", "#800080", "#008080", "#000000"],
    "entertainment": ["#FF00FF", "#00FFFF", "#000000", "#FFFFFF"],
    "gaming": ["#39FF14", "#800080", "#000000", "#FFA500"],
    "diamond": ["#FFFFFF", "#0000FF", "#808080", "#C0C0C0"],
    "gold": ["#FFD700", "#8B4513", "#000000", "#F7E7CE"],
    "petroleum": ["#000000", "#FF8C00", "#708090", "#FF0000"],
    "ngo": ["#008000", "#F5F5DC", "#87CEEB", "#FFFFFF"],
    "government": ["#0000FF", "#808080", "#F5F5DC", "#000080"],
    "cybersecurity": ["#4B0082", "#000080", "#FF0000", "#000000"]
}

# --- UI Layout ---
st.set_page_config(page_title="Theme-Based Color Palette", layout="centered")

st.title("🎨 Theme-Based Color Palette Recommender")
st.markdown("Type a theme (e.g., `hospital`, `retail`, `fashion`) to get a smart color palette.")

# Input box
theme_input = st.text_input("Enter a theme:")

# Normalize input
theme_key = theme_input.lower().strip()

# Display results
if theme_key:
    if theme_key in theme_palettes:
        st.subheader(f"🎨 Suggested Palette for: `{theme_key.capitalize()}`")

        colors = theme_palettes[theme_key]

        # Show colors as colored blocks with hex
        cols = st.columns(len(colors))
        for i, col in enumerate(cols):
            with col:
                st.markdown(
                    f"""
                    <div style=\"background-color: {colors[i]};
                                border-radius: 10px;
                                height: 100px;
                                width: 100%;
                                border: 1px solid #ccc;\"></div>
                    <p style=\"text-align:center; margin-top:10px;\">{colors[i]}</p>
                    """, unsafe_allow_html=True)
    else:
        st.warning("Sorry, theme not found. Try another like `fashion`, `education`, or `nature`.")
