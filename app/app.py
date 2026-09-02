import os
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
st.set_page_config(page_title="Healthcare Claim & EOB Intelligence", layout="wide")
st.title("Healthcare Claim & EOB Intelligence Automation")
st.caption("Gemini-assisted claim and EOB analysis using Python, Pandas and structured prompts.")

sample = pd.DataFrame({
    "claim_id":["CLM1001","CLM1002","CLM1003","CLM1004","CLM1005"],
    "claim_status":["Paid","Denied","Pending","Rejected","Paid"],
    "denial_reason":["None","Authorization required","None","Invalid member ID","None"],
    "payer":["Payer A","Payer B","Payer A","Payer C","Payer B"],
    "payment_amount":[1250,0,500,0,1800]
})
uploaded = st.file_uploader("Upload claim/EOB CSV", type=["csv"])
df = pd.read_csv(uploaded) if uploaded else sample

st.subheader("Claim / EOB Data")
st.dataframe(df, use_container_width=True)

if "claim_status" in df.columns:
    st.subheader("Claim Status Distribution")
    st.bar_chart(df["claim_status"].value_counts())

if st.button("Generate Gemini Claim/EOB Summary"):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        st.error("Set GEMINI_API_KEY in your .env file.")
    else:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(os.getenv("GEMINI_MODEL", "gemini-1.5-flash"))
        prompt = f"Summarize this synthetic healthcare claim/EOB dataset. Mention claim-status patterns, denial reasons, payer/payment observations, and 3 suggested follow-up actions. Do not invent facts. Data:\n{df.to_string(index=False)}"
        try:
            st.write(model.generate_content(prompt).text)
        except Exception as e:
            st.error(f"Gemini error: {e}")

st.info("Portfolio demo. Use synthetic/de-identified healthcare data only. Gemini is used for optional narrative analysis.")
