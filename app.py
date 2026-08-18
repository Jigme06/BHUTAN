import streamlit as st
from engine import KnowledgeEngine
import json
import base64
import pandas as pd

def get_base64(bin_file):
    with open(bin_file,'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

bin_str = get_base64("images/img1.jpg")

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url("data:image/jpg;base64,{bin_str}");
        background-attachment: fixed;
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
st.title('འབྲུག། : THE KINGDOM OF BHUTAN 🇧🇹')

st.write("Kuzuzangpo La! Welcome to the Digital Interactive Repository of Bhutan")

engine = KnowledgeEngine("data/data.json")
engine.load_data()

st.title('AT A GLANCE:')
pop_val, pop_year = engine.get_stats("SP.POP.TOTL")
gdp_val, gdp_year = engine.get_stats("NY.GDP.MKTP.CD")

col1, col2 = st.columns(2)

with col1:
    if pop_val:
        st.metric(label=f"Population ({pop_year})", value=f"{pop_val:,}")
    else:
        st.error("Could not fetch population data.")

with col2:
    if gdp_val:
        st.metric(label=f"GDP (USD) ({gdp_year})", value=f"${gdp_val / 1e9:.2f} Billion")
    else:
        st.error("Could not fetch GDP data.")

with open('data/about.md',"r", encoding="utf-8") as f:
    about_content = f.read()

with st.expander(" ABOUT DRUKYUL 🇧🇹"):
    st.image("images/img2.jpeg", use_container_width=True)
    st.markdown(about_content)

st.divider()

st.subheader("THE DRUK GYALPOS")
with open('data/crown.md','r') as f:
    crown_hist = f.read()

with st.expander("THE CROWN"):
    st.image("images/crown.jpg", use_container_width=False)
    st.markdown(crown_hist)
    
st.write("LEARN MORE ABOUT THE GLORIOUS RULERS OF BHUTAN")

st.markdown("""
    <style>
    div.stButton > button {
        background-color: #FFC300 !important;
        color: black !important; 
        border: none !important;
    }
    </style>
""", unsafe_allow_html=True)

if st.button("THE ROYALTY: BHUTAN'S GODLY KINGS", type="primary"):
    st.switch_page("pages/01_Royals.py")

    
st.title("The HEART OF BHUTAN")
st.write('Explore culturally resonant sites which have braced the test of time.')
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
            st.markdown(f"""
                    <style>
                    .display {{ background-color: #001F3F;
                        padding: 15px;
                    }}
                    </style>
                    <div class= "display">
                        {wiki_summary}
                    </<div>
                    """,unsafe_allow_html= True)
    
    if st.button('Show on map'):
        with st.spinner("THANK YOU FOR YOUR PATIENCE"):
            try:
                lat,lon = engine.get_coordinates(site_obj.name)
                map_data = pd.DataFrame({'lat':[lat],'lon': [lon]})
                st.map(map_data)

            except Exception as e:
                st.error("Unfortunately we couldn't find the place.")
    
st.divider()

st.title('THE HEARTBEATS OF BHUTAN')
st.write('Explore some of Bhutanese Histories most influential figures.')

with open("data/p_data.json","r") as f:
    personalities_data = json.load(f)

names = [person['name'] for person in personalities_data]
selected_name = st.selectbox("Which figure would you like to explore?",['-- Select a Person -- '] + names)
if selected_name != "-- Select a Person -- ":
    person_obj = next(p for p in personalities_data if p["name"] == selected_name)
    
    st.subheader(f"{person_obj['name']}")
    st.write(f"{person_obj['title']}")
    st.write(f"**Era of Impact:** {person_obj['century']}")

    if st.button(f"Learn more about {person_obj['name']}"):
        with st.spinner("Fetching data from Wikipedia..."):
            wiki_summary = engine.fetch_wikipedia_summary(person_obj['wiki_search_term'])
            st.markdown(f"""
                    <style>
                    .display {{ background-color: #001F3F;
                        padding: 15px;
                    }}
                    </style>
                    <div class= "display">
                        {wiki_summary}
                    </<div>
                    """,unsafe_allow_html= True)

