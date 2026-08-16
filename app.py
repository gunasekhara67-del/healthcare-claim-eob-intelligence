import streamlit as st

from src.analyzer import analyze_claim


st.set_page_config(
    page_title="Healthcare Claim EOB Intelligence",
    page_icon="🏥",
    layout="wide",
)

st.title("🏥 Healthcare Claim EOB Intelligence")
st.write(
    "Analyze a healthcare claim and generate a structured claim assessment."
)

claim_text = st.text_area(
    "Enter claim information",
    height=250,
    placeholder="""Payer: ABC Health Plan
Claim Number: CLM-1001
Status: Denied
Denial Reason: Prior authorization required
Billed Amount: $1250.00
Paid Amount: $0.00
Patient Responsibility: $0.00""",
)

if st.button("Analyze Claim", type="primary"):
    if not claim_text.strip():
        st.warning("Please enter claim information.")
    else:
        with st.spinner("Analyzing claim..."):
            try:
                result = analyze_claim(claim_text)

                st.subheader("Claim Analysis")

                col1, col2 = st.columns(2)

                with col1:
                    st.write("**Claim Number:**", result.claim_number)
                    st.write("**Payer:**", result.payer)
                    st.write("**Status:**", result.status)
                    st.write("**Denial Reason:**", result.denial_reason)

                with col2:
                    st.write("**Billed Amount:**", f"${result.billed_amount:,.2f}")
                    st.write("**Paid Amount:**", f"${result.paid_amount:,.2f}")
                    st.write(
                        "**Patient Responsibility:**",
                        f"${result.patient_responsibility:,.2f}",
                    )

                st.subheader("Recommended Action")
                st.info(result.recommended_action)

            except Exception as exc:
                st.error(f"Unable to analyze the claim: {exc}")