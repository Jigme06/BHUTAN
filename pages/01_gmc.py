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
    background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('data:image/jpeg;base64,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");
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
 
