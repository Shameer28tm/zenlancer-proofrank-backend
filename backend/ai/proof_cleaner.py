import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"

def clean_proof(raw_proof: str):
    prompt = f"""
You are ProofRank AI.

From the proof below, extract:

- service
- industry (if mentioned or inferable)
- outcome
- metric (numbers, %, revenue, time, etc)
- rewrite a clean professional proof statement

Return ONLY valid JSON in this format:

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

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=120)
    result = response.json()

    try:
        return json.loads(result["response"])
    except:
        return {
            "error": "AI response parse failed",
            "raw": result.get("response")
        }
