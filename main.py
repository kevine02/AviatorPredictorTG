
from flask import Flask, render_template, send_file
import pandas as pd
import matplotlib.pyplot as plt
from predictor import predict_next

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict")
def predict():
    data, result = predict_next()
    prediction = "✅ >5" if result else "❌ ≤5"
    return render_template("index.html", prediction=prediction, last_5=data[-5:])

@app.route("/graph")
def graph():
    df = pd.read_csv("data.csv")
    plt.figure(figsize=(6,3))
    df["multiplier"].tail(30).plot(title="Multiplicateurs récents")
    plt.tight_layout()
    plt.savefig("static/graph.png")
    plt.close()
    return send_file("static/graph.png", mimetype="image/png")

@app.route("/history")
def history():
    df = pd.read_csv("data.csv")
    html_table = df.to_html(classes='history', index=False)
    return f"<html><head><link rel='stylesheet' href='/static/style.css'></head><body><div class='container'><h1>📊 Historique</h1>{html_table}</div></body></html>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
