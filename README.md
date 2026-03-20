# IRIS_flower-pridcion_knn_NB_prject

# Project Title


Iris Flower Classification using KNN & Naive Bayes
📌 Project Overview

This project is a Machine Learning application that classifies iris flowers into three species:

Setosa

Versicolor

Virginica

It uses two algorithms:

K-Nearest Neighbors (KNN)

Naive Bayes

The model is integrated with a simple web interface using Flask.

📊 Dataset

The Iris dataset contains:

Sepal Length

Sepal Width

Petal Length

Petal Width

Target:

Flower Species (3 classes)

⚙️ Technologies Used

Python

Flask

NumPy

Pandas

Scikit-learn

HTML, CSS

📁 Project Structure
project/
│
├── app.py
├── knn_mdl.pkl
├── naive_bayes.pkl
│
├── train_results.json
├── test_results.json
├── nb_train_res.json
├── nb_test_results.json
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── images/
│
└── README.md
🚀 Features

User input for flower measurements

Prediction using KNN & Naive Bayes

Displays:

Predicted class

Accuracy

Confusion Matrix

Classification Report

▶️ How to Run
1. Clone Repository
git clone https://github.com/your-username/iris-classification.git
cd iris-classification
2. Install Libraries
pip install flask numpy pandas scikit-learn
3. Run App
python app.py
4. Open Browser
http://127.0.0.1:5000/
🧠 Models Used
🔹 KNN

Distance-based algorithm

Works well for small datasets

🔹 Naive Bayes

Probability-based algorithm

Fast and efficient

📈 Results

KNN Accuracy: ~95%

Naive Bayes Accuracy: ~90%






👩‍💻 Author

Kottamula Priyanka
B.Tech CSE (Data Science)








