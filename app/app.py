import pandas as pd
import streamlit as st

st.set_page_config(page_title="Healthcare Claim & EOB Intelligence", layout="wide")
st.title("Healthcare Claim & EOB Intelligence Automation")
st.caption("LLM-assisted claim and EOB analysis using Python, Pandas and structured prompts.")

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

st.info("Portfolio demo. Use synthetic/de-identified healthcare data only.")
