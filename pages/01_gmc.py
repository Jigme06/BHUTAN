import streamlit as st
import base64
from engine import KnowledgeEngine
import streamlit_mermaid as stmd
import pandas as pd
import json
from datetime import datetime


def get_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode("utf-8")


bg = get_base64("images/gmcbg.jpeg")

st.markdown(f"""
<style>
.stApp {{
    background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('data:image/jpeg;base64,{bg}');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}
</style>
""", unsafe_allow_html=True)


st.caption ("We are actively working on it")

st.markdown("<h2 style='text-align: center; font-weight: bold;'> GELEPHU MINDFULNESS CITY</h2>",unsafe_allow_html=True)

gmclogo = get_base64("images/gmclogo.png")
st.markdown(
    f"""
<div style="display:flex; justify-content: center; align-items:center;">
<img src= "data:image/png;base64,{gmclogo}" width="500">
</div>""",unsafe_allow_html = True
)

st.markdown(f"""
<div style="
    background: rgba(45, 38, 28, 0.55); 
    backdrop-filter: blur(12px); 
    -webkit-backdrop-filter: blur(12px); 
    border: 1px solid rgba(255, 255, 255, 0.15); 
    border-radius: 16px; 
    padding: 40px; 
    max-width: 900px; 
    margin: 20px auto; 
    box-shadow: 0 20px 40px rgba(0,0,0,0.4);
    text-align: center;
    ">
<h7 style='text-align:center;font-style:italic;'>
"I will never tire, never lose hope, and never hesitate. I am confident in our nation, its people, and our collective ability to succeed."
</h7>
<p style='text-align:center;font-style:italic;'>
            -His Majesty King Jigme Khesar Namgyel Wangchuck
</p>
</div>
""",unsafe_allow_html=True)



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

    def parse_event_date(item):
        date_str = item["date"].strip()
        for fmt in ("%B %d, %Y", "%B %Y"):
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                pass
        return datetime.min

    sorted_events = sorted(events, key=parse_event_date)

    mermaid_code = "timeline\n    title History of Gelephu Mindfulness City\n"
    date_dict = {}


    for item in sorted_events:
        date_str = item["date"].strip()
        event_title = item["event"]

        if date_str not in date_dict:
            date_dict[date_str] = []
        date_dict[date_str].append(event_title)

    for dt, titles in date_dict.items():
        titles_str = " : ".join(titles)
        mermaid_code += f"    {dt} : {titles_str}\n"
    

    stmd.st_mermaid(mermaid_code)
 
