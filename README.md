# 🏠 House Price Prediction Model

### Machine Learning & AI Internship — SkillNexis

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/ML-Linear%20Regression-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=matplotlib&logoColor=white" />
</p>

<p align="center">
  <b>A Machine Learning project that predicts residential house prices using Linear Regression.</b>
</p>

---

## 📌 Project Overview

**House Price Prediction Model** is a Machine Learning project developed as part of the **SkillNexis Machine Learning & AI Internship**.

The project uses the **Kaggle House Prices Dataset** to train a **Linear Regression** model capable of predicting house sale prices based on selected property characteristics.

The project demonstrates a complete beginner-friendly Machine Learning workflow — from loading and exploring raw data to training a model, generating predictions, evaluating performance, and visualizing the results.

---

## 👨‍💻 Author

**Adhith Raghunathan Nair**

🎓 **B.Tech Computer Science & Engineering**  
🏫 **Amity University Mumbai**

**Internship:** SkillNexis — Machine Learning & AI Internship

---

## 🏢 Internship Information

| Category | Details |
|---|---|
| **Internship** | SkillNexis Machine Learning & AI Internship |
| **Project** | Mini Project 2 |
| **Project Title** | House Price Prediction Model |
| **Domain** | Machine Learning |
| **Model** | Linear Regression |
| **Dataset** | Kaggle — House Prices Dataset |
| **Programming Language** | Python |
| **Libraries** | Pandas, NumPy, Matplotlib, Scikit-learn |

---

# 🎯 Project Objective

The main objective of this project is to build a Machine Learning model that can estimate residential house prices using important property-related features.

The project focuses on understanding the fundamental stages of a Machine Learning pipeline:

- 📂 Loading the dataset
- 🔍 Exploring the dataset
- 🧹 Checking missing values
- 🎯 Selecting relevant features
- 📊 Preparing input and target variables
- ✂️ Splitting data into training and testing sets
- 🤖 Training a Linear Regression model
- 🔮 Predicting house prices
- 📈 Evaluating the model using R² Score
- 📉 Visualizing Actual vs Predicted prices
- 💾 Saving prediction results into a CSV file

---

# 📊 Dataset

The project uses the **House Prices — Advanced Regression Techniques** dataset from Kaggle.

The dataset contains information about residential properties along with their corresponding sale prices.

### Dataset Statistics

| Property | Value |
|---|---:|
| **Total Records** | 1,460 |
| **Total Columns** | 81 |
| **Target Variable** | `SalePrice` |
| **Training Samples** | 1,168 |
| **Testing Samples** | 292 |

---

# 🧩 Selected Features

Instead of using all 80+ available input columns, four meaningful numerical features were selected for this mini project.

| Feature | Description |
|---|---|
| `GrLivArea` | Above-ground living area |
| `BedroomAbvGr` | Number of bedrooms above ground |
| `FullBath` | Number of full bathrooms |
| `YearBuilt` | Original construction year |

### 🎯 Target Variable

```text
SalePrice
