from flask import Flask, render_template, request
from PIL import Image
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load("savedmodel.pth")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    img = Image.open(request.files["image"]).convert("L")
    img = img.resize((64, 64))
    img = np.array(img) / 255.0
    img = img.reshape(1, -1)
    pred = model.predict(img)[0]

    return render_template("index.html", prediction=pred)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)