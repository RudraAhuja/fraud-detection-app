from flask import Flask, render_template, request, jsonify
from utils.workflow import final_analysis
from utils.logger import log_message

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    message = data.get("message", "")

    if not message:
        return jsonify({"error": "No message provided"}), 400

    result = final_analysis(message)

    # Log message
    log_message(message, result)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)