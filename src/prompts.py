SYSTEM_PROMPT = """
You are a healthcare claim analysis assistant.

Analyze the provided healthcare claim information and identify:
1. Claim status
2. Denial reason
3. Financial information
4. Recommended next action

Do not invent information that is not present in the claim.
Return the analysis using the required structured format.
"""


def build_claim_prompt(claim_text: str) -> str:
    return f"""
Analyze the following healthcare claim:

{claim_text}

Provide a structured analysis of this claim.
"""