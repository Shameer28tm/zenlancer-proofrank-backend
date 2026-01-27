from flask import Flask, request, jsonify
from flask_cors import CORS
from proof.routes import proof_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(proof_bp)

@app.route("/")
def home():
    return jsonify({
        "status": "ZenLancer ProofRank backend running",
        "version": "0.1-mvp"
    })

if __name__ == "__main__":
    app.run(debug=True)
