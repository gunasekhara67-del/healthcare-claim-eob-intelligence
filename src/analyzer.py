import os

from dotenv import load_dotenv
from openai import OpenAI

from .models import ClaimAnalysis
from .prompts import SYSTEM_PROMPT, build_claim_prompt


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

DEFAULT_MODEL = "gpt-4o-mini"


def analyze_claim(claim_text: str) -> ClaimAnalysis:
    completion = client.beta.chat.completions.parse(
        model=DEFAULT_MODEL,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": build_claim_prompt(claim_text),
            },
        ],
        response_format=ClaimAnalysis,
        temperature=0,
    )

    result = completion.choices[0].message.parsed

    if result is None:
        raise ValueError("The model did not return a structured claim analysis.")

    return result