from flask import Flask, jsonify
from flask_cors import CORS
from proof.routes import proof_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(proof_bp)   # <<< VERY IMPORTANT
print(app.url_map)


@app.route("/")
def home():
    return jsonify({
        "status": "ZenLancer ProofRank backend running",
        "version": "0.1-mvp"
    })

if __name__ == "__main__":
    app.run(debug=True)
