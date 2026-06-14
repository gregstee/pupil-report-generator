import streamlit as st
import requests

st.set_page_config(page_title="Pupil Report Generator", page_icon="▪", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=VT323&family=Share+Tech+Mono&display=swap');

:root {
  --bg:        #1a0a2e;
  --bg2:       #16213e;
  --win-bg:    #0d0d1a;
  --titlebar:  #c800c8;
  --titlebar2: #6400c8;
  --border:    #ff00ff;
  --border2:   #00ffff;
  --text:      #e0e0ff;
  --text-dim:  #a0a0cc;
  --neon-pink: #ff00ff;
  --neon-cyan: #00ffff;
  --neon-yel:  #ffff00;
  --btn-bg:    #2a0a4a;
  --input-bg:  #0a0a20;
}

html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
  background-color: var(--bg) !important;
  background-image:
    linear-gradient(rgba(200,0,200,0.07) 1px, transparent 1px),
    linear-gradient(90deg, rgba(200,0,200,0.07) 1px, transparent 1px);
  background-size: 40px 40px;
  font-family: 'Share Tech Mono', monospace !important;
  color: var(--text) !important;
}

[data-testid="stMain"], [data-testid="block-container"] {
  background: transparent !important;
}

/* Scanlines */
[data-testid="stApp"]::before {
  content: '';
  position: fixed;
  inset: 0;
  background: repeating-linear-gradient(
    0deg, transparent, transparent 2px,
    rgba(0,0,0,0.15) 2px, rgba(0,0,0,0.15) 4px
  );
  pointer-events: none;
  z-index: 9999;
}

/* Inputs */
input, textarea, select {
  background: var(--input-bg) !important;
  border: 1px solid var(--border2) !important;
  color: var(--text) !important;
  font-family: 'Share Tech Mono', monospace !important;
  border-radius: 0 !important;
}
input:focus, textarea:focus {
  border-color: var(--neon-pink) !important;
  box-shadow: 0 0 8px var(--neon-pink) !important;
}

/* Labels */
label, [data-testid="stWidgetLabel"] p {
  font-family: 'VT323', monospace !important;
  font-size: 1rem !important;
  color: var(--neon-cyan) !important;
  text-shadow: 0 0 6px var(--neon-cyan) !important;
  letter-spacing: 1px !important;
}

/* Buttons */
.stButton > button {
  background: var(--btn-bg) !important;
  border: 2px solid var(--neon-pink) !important;
  color: var(--neon-pink) !important;
  font-family: 'VT323', monospace !important;
  font-size: 1.1rem !important;
  letter-spacing: 2px !important;
  text-transform: uppercase !important;
  border-radius: 0 !important;
  text-shadow: 0 0 6px var(--neon-pink) !important;
  padding: 0.3rem 1.2rem !important;
}
.stButton > button:hover {
  background: #4a0a8a !important;
  box-shadow: 0 0 14px var(--neon-pink) !important;
}

/* Select dropdown */
[data-baseweb="select"] > div {
  background: var(--input-bg) !important;
  border: 1px solid var(--border2) !important;
  border-radius: 0 !important;
  color: var(--text) !important;
}

/* Output text area */
.stTextArea textarea {
  background: var(--input-bg) !important;
  border: 1px solid var(--border2) !important;
  color: var(--text) !important;
  font-family: 'Share Tech Mono', monospace !important;
  font-size: 0.88rem !important;
  line-height: 1.7 !important;
  border-radius: 0 !important;
}

/* Alerts */
[data-testid="stAlert"] {
  background: var(--input-bg) !important;
  border-radius: 0 !important;
  font-family: 'Share Tech Mono', monospace !important;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
<h1 style="font-family:'VT323',monospace;font-size:2.8rem;color:#ff00ff;
  text-shadow:0 0 10px #ff00ff,0 0 30px #ff00ff,0 0 60px #c800c8;
  letter-spacing:4px;text-align:center;margin-bottom:4px;">
  &#x25A0; PUPIL REPORT GEN &#x25A0;
</h1>
<p style="font-family:'VT323',monospace;font-size:1.1rem;color:#00ffff;
  text-shadow:0 0 8px #00ffff;letter-spacing:2px;text-align:center;margin-bottom:1.5rem;">
  // KS2 REPORT WRITER v1.0 //
</p>
""", unsafe_allow_html=True)

# Window border
st.markdown("""<div style="border:2px solid #ff00ff;
  box-shadow:0 0 20px #ff00ff66;padding:20px;background:#0d0d1a;margin-bottom:1rem;">
<div style="background:linear-gradient(90deg,#c800c8,#6400c8);padding:5px 10px;
  margin:-20px -20px 16px -20px;border-bottom:1px solid #ff00ff;
  font-family:'VT323',monospace;color:white;letter-spacing:2px;
  display:flex;justify-content:space-between;">
  <span>&#x25CF; REPORT INPUT</span><span>_ &#x25A1; &#x00D7;</span>
</div>
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

st.markdown("</div>", unsafe_allow_html=True)

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

Write a formal, warm, and encouraging written report paragraph for the following pupil. The report should:
- Be written in third person (e.g. "Sam has...")
- Be 3-5 sentences long
- Be appropriate for parents/guardians to read
- Reflect the pupil's ability level honestly but constructively
- Include specific mention of the subject
- Reference the teacher's notes naturally
- End with a forward-looking, encouraging sentence

Pupil Name: {name}
Subject: {subject}
Ability Level: {ability}
Teacher Notes: {notes}

Write only the report paragraph, with no preamble or labels."""

        with st.spinner("GENERATING REPORT..."):
            res = requests.post(
                f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}",
                json={
                    "contents": [{"parts": [{"text": prompt}]}],
                    "generationConfig": {"temperature": 0.7, "maxOutputTokens": 400}
                }
            )

        if res.ok:
            data = res.json()
            report = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "").strip()
            if report:
                st.markdown("""<div style="border:2px solid #ff00ff;
                  box-shadow:0 0 20px #ff00ff66;padding:20px;background:#0d0d1a;margin-top:1rem;">
                <div style="background:linear-gradient(90deg,#c800c8,#6400c8);padding:5px 10px;
                  margin:-20px -20px 16px -20px;border-bottom:1px solid #ff00ff;
                  font-family:'VT323',monospace;color:white;letter-spacing:2px;
                  display:flex;justify-content:space-between;">
                  <span>&#x25CF; GENERATED REPORT</span><span>_ &#x25A1; &#x00D7;</span>
                </div>
                """, unsafe_allow_html=True)
                st.text_area("", value=report, height=180, key="report_out")
                st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.error("⛔ ERROR: NO RESPONSE FROM MODEL")
        else:
            err = res.json().get("error", {}).get("message", f"HTTP {res.status_code}")
            st.error(f"⛔ ERROR: {err.upper()}")
