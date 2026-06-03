from flask import Flask, jsonify

app = Flask(__name__)

import logging

logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    app.logger.info("Home endpoint accessed")
    return "App Running"

@app.route("/health")
def health():
    return {
    "status": "healthy",
    "service": "flask-api",
    "version": "1.0"
}, 200

@app.route("/predict")
def predict():
    return jsonify(prediction="coming soon")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)