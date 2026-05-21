import streamlit as st
from engine import KnowledgeEngine
import base64
st.title("The HEART OF BHUTAN 🇧🇹")
st.write("Kuzuzangpo La! Welcome to the Digital Interactive Repository of Bhutanese Cultural Sites.")

engine = KnowledgeEngine("data.json")
engine.load_data()

with open('about.md',"r", encoding="utf-8") as f:
    about_content = f.read()

with st.expander(" ABOUT DRUKYUL 🇧🇹"):
    st.image("img1.jpg", use_container_width=True)
    st.markdown(about_content)

site_names = [site.name for site in engine.sites]
selected_site = st.selectbox("Select a cultural site to learn more:", ["-- Select a Site --"] + site_names)

if selected_site != "-- Select a Site --":
    site_obj = next(s for s in engine.sites if s.name == selected_site)
    
    st.subheader(f"📍 {site_obj.name}")
    st.write(f"**Location:** {site_obj.loc}")
    st.write(f"**Founded:** {site_obj.year}")
    

st.divider()
st.write("Explore Bhutan's heritage one site at a time.")
