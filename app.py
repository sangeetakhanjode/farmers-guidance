from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""
    if request.method == "POST":
        question = request.form["question"]

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "phi",
                "prompt": question,
                "stream": False
            }
        )

        result = response.json()
        answer = result["response"]
        answer = answer.replace(". ",".<br><br>")

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)