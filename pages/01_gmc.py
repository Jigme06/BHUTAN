import streamlit as st
import base64
from engine import KnowledgeEngine
import streamlit_mermaid as stmd
import pandas as pd
import json


def get_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode("utf-8")


bg = get_base64("images/gmcbg.jpeg")

st.markdown("""
<style>
.stApp {
    background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('data:image/jpeg;base64,{bg}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
</style>
""", unsafe_allow_html=True)


st.caption ("We are actively working on it")

st.header("GELEPHU MINDFULNESS CITY")
st.image("images/gmclogo.png")
with st.container():
   st.write("""
> *"I will never tire, never lose hope, and never hesitate. I am confident in our nation, its people, and our collective ability to succeed."*
> 
> **His Majesty King Jigme Khesar Namgyel Wangchuck**
""")


img1, img2, img3 = get_base64("images/con1.png"), get_base64("images/con2.jpeg"), get_base64("images/con3.jpg")

st.markdown(f"""
<style>
@keyframes slide {{ 0% {{transform: translateX(0);}} 100% {{transform: translateX(-50%);}} }}
.track {{ display: flex; width: 200%; animation: slide 15s linear infinite; }}
.track:hover {{ animation-play-state: paused; }}
.track img {{ width: 33%; height: 220px; object-fit: cover; border-radius: 8px; margin-right: 10px; }}
</style>

<div style="overflow: hidden; border-radius: 10px; border: 1px solid rgba(255,255,255,0.2); padding: 10px;">
  <div class="track">
    <img src="data:image/png;base64,{img1}"><img src="data:image/jpeg;base64,{img2}"><img src="data:image/jpeg;base64,{img3}">
    <img src="data:image/png;base64,{img1}"><img src="data:image/jpeg;base64,{img2}"><img src="data:image/jpeg;base64,{img3}">
  </div>
</div>
""", unsafe_allow_html=True)


with st.expander("What is GMC?"):
    st.write("Under Active Development! Check Back Later.")

with open("data/gmchistory.json","r") as f:
    events = json.load(f)

with st.expander("The Journey"):
    st.write("I'm currently figuring out the mechanics might be awhile.")

    mermaid_code = "timeline\n    title History of Gelephu Mindfulness City\n"
    years_dict = {}
    for item in events:
        year = item["date"].strip().split()[-1]
        event_title = item["event"]

        if year not in years_dict:
            years_dict[year] = []
        years_dict[year].append(event_title)

    for yr, titles in years_dict.items():
        titles_str = " : ".join(titles)
        mermaid_code += f"    {yr} : {titles_str}\n"

    stmd.st_mermaid(mermaid_code)
 
