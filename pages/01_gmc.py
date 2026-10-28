import streamlit as st
from engine import KnowledgeEngine
from engine import get_base64


st.caption ("We are actively working on it")

st.header("GELEPHU MINDFULLNESS CITY")


st.markdown("""

> *"Because of this, I will never tire, never lose hope, and never hesitate. I am confident in our nation, its people, and our collective ability to succeed."*
> 
> — **His Majesty King Jigme Khesar Namgyel Wangchuck**
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


with st.expander("The Birth of GMC"):
    st.write("Under Active Development check back later.")


