# ReviewShield-AI
AI-based fake product review detection system using NLP and Machine Learning

## Overview

ReviewShield-AI a Fake Product Review Detector is a Machine Learning and Natural Language Processing (NLP) based project that identifies whether a product review is fake or genuine.

The project analyzes review text using TF-IDF feature extraction and Logistic Regression classification to predict review authenticity with approximately 90% accuracy.

This project was developed to solve the real-world problem of fake reviews on e-commerce platforms.

---

# Features

* Detects fake and genuine product reviews
* Uses Machine Learning for prediction
* NLP based text processing
* Interactive Streamlit user interface
* Real-time review prediction
* Data visualization support
* Word cloud and chart analysis

---

# Technologies Used

## Programming Language

* Python

## Libraries and Frameworks

* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Matplotlib
* WordCloud
* NLTK

## Machine Learning Techniques

* TF-IDF Vectorization
* Logistic Regression

---

# Project Workflow

1. Dataset Collection
2. Data Preprocessing
3. Feature Extraction using TF-IDF
4. Model Training using Logistic Regression
5. Model Evaluation
6. Real-time Prediction
7. Visualization and User Interface

---

# Dataset Information

The dataset contains labeled product reviews classified as:

* Fake Reviews (CG)
* Genuine Reviews (OR)

Dataset features include:

* Review Text
* Review Rating
* Product Category
* Label

---

# Model Accuracy

The model achieved approximately:

## Accuracy: 90%

---

# Visualizations Included

* Pie Chart
* Word Cloud

---

# Project Structure

```text
AI-Fake-Product-Review-Detector(ReviewShield-AI)
│
├── app.py
├── fake_review_model.pkl
├── vectorizer.pkl
├── fake_reviews.csv
├── requirements.txt
├── README.md
├── screenshots
│   ├── interface.png
│   ├── prediction.png
│   └── charts.png
└── notebook
    └── fake review detector.ipynb
```

---

# Installation

## Clone Repository

```bash
https://github.com/techjay18/ReviewShield-AI.git
```

## Move into Project Folder

```bash
cd ReviewShield-AI
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run the Application

```bash
streamlit run app.py
```

---

# Screenshots


## Application Interface

![Interface](https://raw.githubusercontent.com/techjay18/ReviewShield-AI/main/screenshots/interface.png)


## Prediction Result

![Prediction](Screenshots/prediction.png)

## Data Visualization

![pie Chart](Screenshots/piechart.png)
![wordcloud](Screenshots/wordcloud.png)

# Future Improvements

* Deep Learning integration
* Sentiment analysis
* Cloud deployment
* Browser extension support
* Advanced NLP models

---

# Real-World Applications

* E-commerce platforms
* Online marketplaces
* Customer feedback analysis
* Review authenticity verification

---

# Author

Jay Desai

---

# Resume Description

Developed an AI-based Fake Product Review Detection System using Natural Language Processing and Machine Learning techniques. Built a Streamlit web interface with approximately 90% accuracy using TF-IDF Vectorization and Logistic Regression.

---

# License

This project is for educational and internship purposes.
