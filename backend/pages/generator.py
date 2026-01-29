from jinja2 import Environment, FileSystemLoader
import os
import json
from datetime import datetime

print("✅ generator.py FILE LOADED")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))

def generate_proof_page(proof_data: dict):
    print("🔥 PAGE GENERATOR TRIGGERED")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    test_path = os.path.join(OUTPUT_DIR, "test.html")
    with open(test_path, "w", encoding="utf-8") as f:
        f.write("<h1>ZenLancer Proof Page Test</h1>")

    print("✅ test.html file written at:", test_path)

    return "test.html"
