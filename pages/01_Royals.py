import streamlit as st
import streamlit.components.v1 as components
import json
import base64


def get_base64(file):
    with open(file,'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

bg = get_base64('images/bflag.jpg')

st.markdown(f"""
<style>

    .stApp {{ background-image: linear-gradient(rgba(0.0,0,0.4),rgba(0,0,0,0.4)),url('data:image/jpeg;base64,{bg}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
             }}

   
</style>
""", unsafe_allow_html=True)


with open("data/timeline.json", "r") as f:
    events = json.load(f)

html= """
<style>
    @import url('https://fonts.googleapis.com/css2?family=IM+Fell+English:ital@0;1&display=swap');
    body { margin:0; background:#f5e6c8; color:#2c1810; font-family: 'IM Fell English', serif;}
    h1 { font-family: 'Cinzel', serif; color:#800000; text-align: center;}
    h5 { font-family: 'Cinzel', serif; color:#800000; text-align: center;}
    .page {display: none; padding: 40px;}
    .page.active {display: block;}
    .nav { display: flex; justify-content: space-between; margin-top: 20px; padding: 0 20px; }
</style>
"""

for i,event in enumerate(events):
    img_data = get_base64(f"{event['image']}")
    prev_btn = f'<button onclick="goTo({i-1})">PREV</button>' if i>0 else '<button style="visibility:hidden"> PREV </button>' 
    next_btn = f'<button onclick="goTo({i+1})"> NEXT</button>' if i<(len(events)-1) else '<button style="visibility:hidden"> NEXT </button>'
    html += f"""
<div class="page" id="page-{i}">
    <h1>{event['year']}: {event['title']}</h1>
    <img src="data:image/jpeg;base64,{img_data}" style="width:100%;">
    <h5>{event['imd']}</h5>
    <div class="nav">
        {prev_btn}
        {next_btn}
    </div>
    <h4>{event['description']}</h4>
    
</div>
"""
html += """
<script>
    goTo(0)
    document.getElementById('page-0').classList.add('active')

    function goTo(n){
        document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
        document.getElementById('page-' + n).classList.add('active');

        window.frameElement.scrollIntoView({ behavior: 'instant', block: 'start' });
    }
</script>
"""


components.html(html, height=1000, scrolling=True)