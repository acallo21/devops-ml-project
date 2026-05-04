from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "DevOps + MLOps Project is Running!"

@app.route("/health")
def health():
    return jsonify(status="healthy")

@app.route("/predict")
def predict():
    return jsonify(prediction="coming soon")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)