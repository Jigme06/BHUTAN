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


col1,col2,col3 = st.columns(3)
with col1:
    with st.container(border=True):
        st.image("images/con1.png")

with col2:
    with st.container(border=True):
        st.image("images/con2.jpeg")

with col3:
    with st.container(border=True):
        st.image("images/con3.jpg")
        



with st.expander("The Birth of GMC"):
    st.write("Under active Development check back later.")


