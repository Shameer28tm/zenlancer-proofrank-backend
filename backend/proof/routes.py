from flask import Blueprint, request, jsonify

proof_bp = Blueprint("proof", __name__)

@proof_bp.route("/proof/upload", methods=["POST"])
def upload_proof():
    data = request.get_json()
    proof_text = data.get("proof")

    if not proof_text:
        return jsonify({"error": "Proof text required"}), 400

    return jsonify({
        "message": "Proof received successfully",
        "raw_proof": proof_text
    })
