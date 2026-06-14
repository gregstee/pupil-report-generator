import streamlit as st
import requests

st.set_page_config(page_title="Pupil Report Generator", page_icon="▪", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');

:root {
  --desktop:    #008080;
  --win-bg:     #c0c0c0;
  --titlebar:   #000080;
  --title-text: #ffffff;
  --text:       #000000;
  --input-bg:   #ffffff;
  --border-lt:  #ffffff;
  --border-dk:  #808080;
  --border-blk: #000000;
  --btn-face:   #c0c0c0;
}

html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
  background-color: var(--desktop) !important;
  font-family: 'VT323', monospace !important;
  color: var(--text) !important;
}

[data-testid="stMain"], [data-testid="block-container"] {
  background: transparent !important;
}

/* Inputs */
input, textarea, select {
  background: var(--input-bg) !important;
  border-top: 2px solid var(--border-dk) !important;
  border-left: 2px solid var(--border-dk) !important;
  border-right: 2px solid var(--border-lt) !important;
  border-bottom: 2px solid var(--border-lt) !important;
  color: var(--text) !important;
  font-family: 'VT323', monospace !important;
  font-size: 1rem !important;
  border-radius: 0 !important;
}

/* Labels */
label, [data-testid="stWidgetLabel"] p {
  font-family: 'VT323', monospace !important;
  font-size: 1.1rem !important;
  color: var(--text) !important;
  letter-spacing: 0px !important;
}

/* Buttons — raised 3D Win3.1 style */
.stButton > button {
  background: var(--btn-face) !important;
  border-top: 2px solid var(--border-lt) !important;
  border-left: 2px solid var(--border-lt) !important;
  border-right: 2px solid var(--border-blk) !important;
  border-bottom: 2px solid var(--border-blk) !important;
  color: var(--text) !important;
  font-family: 'VT323', monospace !important;
  font-size: 1.1rem !important;
  letter-spacing: 1px !important;
  text-transform: uppercase !important;
  border-radius: 0 !important;
  padding: 0.3rem 1.2rem !important;
  box-shadow: none !important;
}
.stButton > button:hover {
  background: #d4d0c8 !important;
}
.stButton > button:active {
  border-top: 2px solid var(--border-blk) !important;
  border-left: 2px solid var(--border-blk) !important;
  border-right: 2px solid var(--border-lt) !important;
  border-bottom: 2px solid var(--border-lt) !important;
}

/* Select dropdown */
[data-baseweb="select"] > div {
  background: var(--input-bg) !important;
  border-top: 2px solid var(--border-dk) !important;
  border-left: 2px solid var(--border-dk) !important;
  border-right: 2px solid var(--border-lt) !important;
  border-bottom: 2px solid var(--border-lt) !important;
  border-radius: 0 !important;
  color: var(--text) !important;
}

/* Output text area */
.stTextArea textarea {
  background: var(--input-bg) !important;
  border-top: 2px solid var(--border-dk) !important;
  border-left: 2px solid var(--border-dk) !important;
  border-right: 2px solid var(--border-lt) !important;
  border-bottom: 2px solid var(--border-lt) !important;
  color: var(--text) !important;
  font-family: 'VT323', monospace !important;
  font-size: 1rem !important;
  line-height: 1.5 !important;
  border-radius: 0 !important;
}

/* Alerts */
[data-testid="stAlert"] {
  background: var(--win-bg) !important;
  border-radius: 0 !important;
  font-family: 'VT323', monospace !important;
  color: var(--text) !important;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
<h1 style="font-family:'VT323',monospace;font-size:2.4rem;color:#ffffff;
  letter-spacing:2px;text-align:center;margin-bottom:2px;text-shadow:1px 1px #000000;">
  Pupil Report Generator
</h1>
<p style="font-family:'VT323',monospace;font-size:1rem;color:#ffffff;
  letter-spacing:1px;text-align:center;margin-bottom:1rem;">
  KS2 Report Writer v1.0
</p>
""", unsafe_allow_html=True)

# Window border — Win3.1 raised panel
st.markdown("""<div style="
  border-top:2px solid #ffffff;border-left:2px solid #ffffff;
  border-right:2px solid #000000;border-bottom:2px solid #000000;
  padding:2px;background:#c0c0c0;margin-bottom:1rem;">
<div style="background:#000080;padding:4px 8px;
  margin-bottom:12px;
  font-family:'VT323',monospace;color:white;font-size:1rem;letter-spacing:1px;
  display:flex;justify-content:space-between;align-items:center;">
  <span>&#x25CF; Report Input</span>
  <span style="display:flex;gap:4px;">
    <span style="border:1px solid #808080;background:#c0c0c0;color:#000;padding:0 5px;font-size:0.8rem;">_</span>
    <span style="border:1px solid #808080;background:#c0c0c0;color:#000;padding:0 4px;font-size:0.8rem;">&#x25A1;</span>
    <span style="border:1px solid #808080;background:#c0c0c0;color:#000;padding:0 4px;font-size:0.8rem;">&#x00D7;</span>
  </span>
</div>
<div style="padding:0 12px 12px 12px;">
""", unsafe_allow_html=True)

name    = st.text_input("▶ PUPIL NAME", placeholder="Enter pupil's name...")
col1, col2 = st.columns(2)
with col1:
    subject = st.selectbox("▶ SUBJECT", ["", "Science", "Maths", "English"])
with col2:
    ability = st.selectbox("▶ ABILITY", ["", "At Target", "Working Towards Target", "Below Target"])
notes   = st.text_area("▶ TEACHER NOTES", placeholder="Enter your observations, achievements, areas for development...", height=120)

col_gen, col_clear = st.columns([2, 1])
with col_gen:
    generate = st.button("► GENERATE REPORT")
with col_clear:
    clear = st.button("◄ CLEAR FORM")

st.markdown("</div></div>", unsafe_allow_html=True)

if clear:
    st.rerun()

if generate:
    errors = []
    if not name:    errors.append("PUPIL NAME REQUIRED")
    if not subject: errors.append("PLEASE SELECT A SUBJECT")
    if not ability: errors.append("PLEASE SELECT ABILITY LEVEL")
    if not notes:   errors.append("TEACHER NOTES REQUIRED")

    if errors:
        for e in errors:
            st.error(f"⛔ ERROR: {e}")
    else:
        api_key = st.secrets["GEMINI_API_KEY"]

        prompt = f"""You are an experienced primary school teacher writing an end-of-year school report for a pupil aged 7-8 years old (Key Stage 2, Year 3/4).

Here are three example reports showing the expected style, tone, and length. The first is for a pupil at target, the second working towards target, and the third below target:

EXAMPLE 1 (At Target):
Child A has a real enthusiasm for English and thoroughly enjoys listening to stories, participating in discussions, and writing for a range of purposes. They are reading at the expected standard, which is supporting the development of their writing skills. Child A listens carefully to instructions and works hard to include the appropriate features and punctuation in their writing. They approach English lessons with a positive attitude and consistently try their best.

EXAMPLE 2 (Working Towards Target):
Child A enjoys taking part in English lessons and particularly likes listening to stories and sharing their ideas during class discussions. They are developing their reading skills and are beginning to use what they have learned from reading to support their writing. Child A listens carefully to instructions and is working hard to include key features and punctuation in their writing. With continued practice and encouragement, they will continue to grow in confidence and make good progress towards the expected standard.

EXAMPLE 3 (Below Target):
Child A enjoys taking part in English lessons and particularly likes listening to stories and sharing their ideas during class discussions. They are currently working below the expected standard in English and find some aspects of reading and writing challenging. Child A is developing their reading skills and is beginning to use what they have learned from reading to support their writing, although they require regular support and guidance to do this successfully. They listen carefully to instructions and are working hard to include key features and punctuation in their writing. With continued practice, targeted support and encouragement, Child A will continue to develop their confidence and make progress in their English learning.

Now write a report in exactly the same style for the following pupil. Replace "Child A" with the pupil's actual name. Write only the report paragraph, with no preamble or labels.

Pupil Name: {name}
Subject: {subject}
Ability Level: {ability}
Teacher Notes: {notes}"""

        with st.spinner("GENERATING REPORT..."):
            res = requests.post(
                f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}",
                json={
                    "contents": [{"parts": [{"text": prompt}]}],
                    "generationConfig": {"temperature": 0.7, "maxOutputTokens": 1024}
                }
            )

        if res.ok:
            data = res.json()
            report = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "").strip()
            if report:
                st.markdown("""<div style="
                  border-top:2px solid #ffffff;border-left:2px solid #ffffff;
                  border-right:2px solid #000000;border-bottom:2px solid #000000;
                  padding:2px;background:#c0c0c0;margin-top:1rem;">
                <div style="background:#000080;padding:4px 8px;margin-bottom:12px;
                  font-family:'VT323',monospace;color:white;font-size:1rem;letter-spacing:1px;
                  display:flex;justify-content:space-between;align-items:center;">
                  <span>&#x25CF; Generated Report</span>
                  <span style="display:flex;gap:4px;">
                    <span style="border:1px solid #808080;background:#c0c0c0;color:#000;padding:0 5px;font-size:0.8rem;">_</span>
                    <span style="border:1px solid #808080;background:#c0c0c0;color:#000;padding:0 4px;font-size:0.8rem;">&#x25A1;</span>
                    <span style="border:1px solid #808080;background:#c0c0c0;color:#000;padding:0 4px;font-size:0.8rem;">&#x00D7;</span>
                  </span>
                </div>
                <div style="padding:0 12px 12px 12px;">
                """, unsafe_allow_html=True)
                st.text_area("", value=report, height=180, key="report_out")
                st.markdown("</div></div>", unsafe_allow_html=True)
            else:
                st.error("⛔ ERROR: NO RESPONSE FROM MODEL")
        else:
            err = res.json().get("error", {}).get("message", f"HTTP {res.status_code}")
            st.error(f"⛔ ERROR: {err.upper()}")
