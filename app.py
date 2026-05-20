import streamlit as st
from engine import KnowledgeEngine
st.title("🇧🇹 Knowledge Engine: Bhutan")
st.write("Kuzuzangpo La! Welcome to the Digital Interactive Repository of Bhutanese Administrative and Cultural Sites.")

engine = KnowledgeEngine("data.json")
engine.load_data()


with open('about.md',"r", encoding="utf-8") as f:
    about_content = f.read()

with st.expander(" ABOUT DRUKYUL 🇧🇹"):
    st.image("img1.jpg", use_container_width=True)
    st.markdown(about_content)

search_option = st.selectbox(
    "What type of site are you looking for today?",
    ["-- Select Category --", "Dzongs", "Monasteries and Other Neys"]
)

if search_option == "Dzongs":
    results = engine.find_sites_by_type("Dzong")
    
    st.subheader("Found Dzongs")
    for site in results:
        st.write(f"🏰 **{site.name}** — Located in *{site.loc}*")

elif search_option == "Monasteries and Other Neys":
    results = engine.find_sites_by_type("Monastery")
    
    st.subheader("Found Monasteries & Sacred Neys")
    for site in results:
        st.write(f"🛕 **{site.name}** — Located in *{site.loc}*")