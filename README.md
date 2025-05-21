#  Kenya Road Accidents - Nairobi Chapter

## 🧠 Predicting Road Accident Severity in Kenya Using Machine Learning

### 📌 Problem Statement

Road accidents are a significant public safety concern in Kenya, leading to loss of lives, injuries, and economic costs. These have an effect on society when the sole breadwinner loses their life or is unable to work due to injuries, leaving the family vulnerable to hunger and poverty. 

Understanding the factors contributing to accidents, identifying accident-prone areas (hotspots), and predicting accident severity can play a crucial role in improving road safety measures and preventing economic impacts on society.

---

### 🎯 Project Goals

This project aims to leverage machine learning (ML) techniques to:

- Analyze and understand the patterns and contributing factors of accidents on Kenyan roads using historical accident data.
- Identify accident-prone areas (hotspots) by analyzing accidents' spatial and temporal patterns.
- Develop a machine learning model to predict the severity of accidents based on various factors such as road conditions, weather, time of day, and vehicle types.

---

### 🤝 Contribution Guidelines

- **Understand the folder structure** before making changes.
- If you're **creating a task**, go to the `tasks/` folder and create a new folder using this naming convention:

---

### 📁 Project Structure

```plaintext
├── data/                 # Dataset
│   └── RTA_Dataset.csv   # Main dataset
│
├── notebooks/            # Jupyter notebooks (exploratory/training)
│   └── accident_analysis.ipynb
│
├── src/                  # Python scripts
│   └── preprocessing.py
│
├── models/               # Trained models
│   └── RT_model.pkl
│
├── outputs/              # Visual outputs
│   └── severity_distribution.png
│
├── .gitignore
├── .gitattributes
├── requirements.txt
├── README.md
└── LICENSE               # (Optional) License info