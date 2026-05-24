import streamlit as st
from engine import KnowledgeEngine
import json
import base64

def get_base64(bin_file):
    with open(bin_file,'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

bin_str = get_base64("bg.jpg")

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(0, 0, 0, 0.65), rgba(0, 0, 0, 0.65)), url("data:image/jpg;base64,{bin_str}");
        background-attachment: fixed;
        background-size: cover;
        background-position: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title('འབྲུག། : THE KINGDOM OF BHUTAN 🇧🇹')

st.write("Kuzuzangpo La! Welcome to the Digital Interactive Repository of Bhutan")

engine = KnowledgeEngine("data.json")
engine.load_data()

with open('about.md',"r", encoding="utf-8") as f:
    about_content = f.read()

with st.expander(" ABOUT DRUKYUL 🇧🇹"):
    st.image("img1.jpg", use_container_width=True)
    st.markdown(about_content)

st.title("The HEART OF BHUTAN")
site_names = [site.name for site in engine.sites]
selected_site = st.selectbox("Select a cultural site to learn more:", ["-- Select a Site --"] + site_names)

if selected_site != "-- Select a Site --":
    site_obj = next(s for s in engine.sites if s.name == selected_site)
    
    st.subheader(f"📍 {site_obj.name}")
    st.write(f"**Location:** {site_obj.loc}")
    st.write(f"**Founded:** {site_obj.year}")

    if st.button(f"Learn more about {site_obj.name}"):
        with st.spinner("Fetching data from Wikipedia..."):
            wiki_summary = engine.fetch_wikipedia_summary(site_obj.name)
            st.info(wiki_summary)
    
st.divider()

st.title('THE HEARTBEATS OF BHUTAN')

with open("p_data.json","r") as f:
    personalities_data = json.load(f)


names = [person['name'] for person in personalities_data]
selected_name = st.selectbox("Which figure would you like to explore?",['-- Select a Person -- '] + names)
if selected_name != "-- Select a Person -- ":
    person_obj = next(p for p in personalities_data if p["name"] == selected_name)
    
    st.subheader(f"👤 {person_obj['name']}")
    st.write(f"{person_obj['title']}")
    st.write(f"**Era of Impact:** {person_obj['century']}")

