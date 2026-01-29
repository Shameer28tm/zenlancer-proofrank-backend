from flask import Blueprint, request, jsonify
from ai.proof_cleaner import clean_proof
from pages.generator import generate_proof_page

proof_bp = Blueprint("proof", __name__)

@proof_bp.route("/proof/upload", methods=["POST"])
def upload_proof():
    data = request.get_json()
    proof_text = data.get("proof")

    if not proof_text:
        return jsonify({"error": "Proof text required"}), 400

    ai_result = clean_proof(proof_text)

    page_file = generate_proof_page(ai_result)

    return jsonify({
        "message": "Proof processed successfully",
        "ai_output": ai_result,
        "generated_page": page_file
    })
