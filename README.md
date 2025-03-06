# 🐦 Twitter Sentiment Analysis

This repository presents a **machine learning-based sentiment analysis** of tweets related to the **2020 US Presidential Election**. The goal is to analyse the sentiment polarity of tweets mentioning **Donald Trump** and **Joe Biden**, providing insights into public opinion trends.

---

## 📌 Table of Contents
1. [Project Overview](#-project-overview)  
2. [Repository Structure](#-repository-structure)  
3. [Data Description](#-data-description)  
4. [Methodology](#-methodology)  
5. [Usage Instructions](#-usage-instructions)  
6. [Requirements](#-requirements)  
7. [Results](#-results)  
8. [Contributing](#-contributing) 

---

## 🔍 Project Overview

- **Goal**: Perform sentiment analysis on tweets related to the 2020 US Presidential Election.  
- **Dataset**: Consists of tweets mentioning **Donald Trump** and **Joe Biden**.  
- **Models Used**: Logistic Regression, Random Forest, Support Vector Machine (SVM).  
- **Evaluation Metrics**: Accuracy, Precision, Recall, F1-score.  
- **Implementation**: Developed using **Apache Spark (PySpark)** for large-scale data processing.  

### 🎯 Key Objectives
1. **Data Collection & Preprocessing**:  
   - Merge and clean datasets.  
   - Tokenization, stopword removal, and feature extraction.  
2. **Sentiment Classification**:  
   - Predict whether a tweet is **positive** or **negative**.  
3. **Visualization & Insights**:  
   - Identify top tweet sources, geographic trends, and sentiment distribution.  

---

## 📂 Repository Structure
```
Twitter_Sentiment_Analysis/
├── notebooks/
│   ├── Data_Preprocessing_and_Model_Building.ipynb  # Jupyter notebook for preprocessing and model training
├── Twitter_Sentiment_Analysis.py                   # PySpark script for large-scale sentiment analysis
├── Report.pdf                                      # Research paper explaining methodology and findings
├── README.md                                       # Project documentation
```

---

## 📊 Data Description

- **Dataset Source**: Twitter API (Election 2020-related tweets).  
- **Feature Categories**:  
  - **Tweet Content**: Textual data of tweets.  
  - **Geographic Information**: Country, state, tweet location.  
  - **Engagement Metrics**: Likes, retweets.  
  - **Device Information**: Twitter Web App, iPhone, Android.  
- **Target Variable**: `sentiment` (positive/negative).  

---

## ⚙️ Methodology

### **Data Preprocessing & Feature Engineering**
- **Text Cleaning** → Removal of URLs, emojis, special characters.  
- **Tokenization** → Breaking tweets into words.  
- **Stopword Removal** → Eliminating unimportant words.  
- **TF-IDF Vectorization** → Convert text to numerical representation.  
- **Categorical Encoding** → Encoding categorical variables for modeling.  

### **Machine Learning Models**
- **Logistic Regression** → Baseline classification model.  
- **Random Forest Classifier** → Ensemble model for better generalization.  
- **Support Vector Machine (SVM)** → Best performing model with **87.48% accuracy**.  

### **Sentiment Analysis Insights**
- **Trump vs Biden Sentiment Distribution**  
  - Trump: **77,336 positive**, **135,927 negative**.  
  - Biden: **75,512 positive**, **105,625 negative**.  
- **Geographic Trends**  
  - **Top 5 countries** with the most election-related tweets: USA, UK, India, France, Germany.  
  - **Top US states** with the highest tweet counts: California, New York, Texas, Florida, Pennsylvania.  
- **Source Analysis**  
  - Most tweets were posted via **Twitter Web App**, followed by **iPhone and Android devices**.  

---

## 🚀 Usage Instructions

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/sanyog-chavhan/Twitter_Sentiment_Analysis.git
cd Twitter_Sentiment_Analysis
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Run Jupyter Notebook**
```bash
jupyter notebook
```
- Open `notebooks/Data_Preprocessing_and_Model_Building.ipynb`.  

### **4️⃣ Run PySpark Script for Large-Scale Data**
```bash
spark-submit Twitter_Sentiment_Analysis.py
```

### **5️⃣ Explore Results**
- The notebook contains model training, evaluation metrics, and visualizations.  
- Refer to the `Report.pdf` for a detailed breakdown.  

---

## 📦 Requirements

Install dependencies via `pip install -r requirements.txt`.  
(Ensure **Apache Spark** is installed if running PySpark scripts).  

---

## 📈 Results

### **Model Performance Comparison**

| Model            | Accuracy  |
|-----------------|----------|
| **Logistic Regression**  | 85.34%  |
| **Random Forest**        | 61.22%  |
| **Support Vector Machine** | **87.48%**  |

### **Best Model**: **Support Vector Machine (SVM)**  
Achieved the highest accuracy of **87.48%**, making it the best sentiment classifier.  

---

## 🤝 Contributing

1. **Fork** this repo.  
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new model or fix bug"
   ```
4. Push to GitHub:
   ```bash
   git push origin feature/your-feature
   ```
5. Open a **Pull Request**.

