from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle
import json

app = Flask(__name__)

# Load models
knn_model = pickle.load(open("knn_mdl.pkl", "rb"))
nb_model = pickle.load(open("naive_bayes.pkl", "rb"))

# Load JSON result files
knn_train = json.load(open("train_results.json"))
knn_test = json.load(open("test_results.json"))
nb_train = json.load(open("nb_train_res.json"))
nb_test = json.load(open("nb_test_results.json"))

# Class mapping
flower_names = {
    0: "Setosa",
    1: "Versicolor",
    2: "Virginica"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    model = data.get("model")

    X = np.array([[
        float(data["sl"]),
        float(data["sw"]),
        float(data["pl"]),
        float(data["pw"])
    ]])

    if model == "knn":
        pred_num = int(knn_model.predict(X)[0])
        train = knn_train
        test = knn_test

    elif model == "nb":
        pred_num = int(nb_model.predict(X)[0])
        train = nb_train
        test = nb_test

    else:
        return jsonify({"error": "Model not selected"}), 400

    return jsonify({
        "prediction_number": pred_num,
        "prediction_name": flower_names[pred_num],
        "train_accuracy": train["train_accuracy"],
        "test_accuracy": test["test_accuracy"],
        "train_cm": train["train_confusion_matrix"],
        "test_cm": test["test_confusion_matrix"],
        "train_report": train["train_classification_report"],
        "test_report": test["test_classification_report"]
    })

if __name__ == "__main__":
    app.run(debug=True)
