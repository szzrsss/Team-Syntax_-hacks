
import streamlit as st

st.set_page_config(
    page_title="Restyle | Aurene",
    page_icon="✨",
    layout="wide"
)
from navigation import apply_theme, show_navigation

apply_theme()
show_navigation()

st.title("RESTYLE")
st.subheader("Your wardrobe. A world of possibilities.")

st.write(
    "Upload pictures of clothes you already own and "
    "discover new ways to style them."
)

st.divider()

st.header("Build your digital wardrobe")

uploaded_files = st.file_uploader(
    "Upload photos of your clothing",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

if uploaded_files:
    st.success(f"{len(uploaded_files)} clothing image(s) uploaded!")

st.divider()

st.header("What are you dressing for?")

occasion = st.selectbox(
    "Choose an occasion",
    ["Casual day out", "College / School", "Party",
     "Formal event", "Vacation", "Other"]
)

style = st.selectbox(
    "Choose your preferred style",
    ["Minimalist", "Streetwear", "Casual",
     "Elegant", "Bohemian", "Surprise me"]
)

if st.button("CREATE MY OUTFITS"):
    st.info("Your AI outfit stylist will be connected here soon.")
