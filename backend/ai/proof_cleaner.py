import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def clean_proof(raw_proof: str):
    prompt = f"""
You are ProofRank AI.

From the proof below, extract:

- service
- industry (if mentioned or inferable)
- result/outcome
- metric (numbers, %, revenue, time, etc)
- rewrite a clean professional proof statement

Return strictly in JSON format:

{{
  "service": "",
  "industry": "",
  "outcome": "",
  "metric": "",
  "clean_proof": ""
}}

Proof:
{raw_proof}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content
