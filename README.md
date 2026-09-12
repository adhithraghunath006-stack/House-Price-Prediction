# 🏠 House Price Prediction Model

    ### Machine Learning & AI Internship — SkillNexis

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Machine%20Learning-Linear%20Regression-orange?style=for-the-badge" alt="Machine Learning">
  <img src="https://img.shields.io/badge/Library-Pandas-green?style=for-the-badge&logo=pandas" alt="Pandas">
  <img src="https://img.shields.io/badge/Library-Matplotlib-red?style=for-the-badge" alt="Matplotlib">
  <img src="https://img.shields.io/badge/Library-Scikit--Learn-yellow?style=for-the-badge&logo=scikit-learn" alt="Scikit Learn">
</p>

<p align="center">
  <b>A Machine Learning project that predicts residential house prices using Linear Regression.</b>
</p>

---

## 👨‍💻 Author

**Adhith Raghunathan Nair**

**B.Tech Computer Science & Engineering**  
**Amity University Mumbai**

---

## 🎓 Internship Information

| Field | Details |
|---|---|
| **Internship** | SkillNexis Machine Learning & AI Internship |
| **Project** | Mini Project 2 |
| **Project Title** | House Price Prediction Model |
| **Domain** | Machine Learning |
| **Model Used** | Linear Regression |
| **Dataset** | Kaggle — House Prices Dataset |
| **Programming Language** | Python |

---

## 📌 Project Overview

The **House Price Prediction Model** is a Machine Learning project developed as part of the **SkillNexis Machine Learning & AI Internship**.

The main objective of this project is to build a simple and interpretable **Linear Regression model** capable of predicting residential house prices based on selected property characteristics.

The project follows a complete basic Machine Learning workflow — from loading and exploring the dataset to training the model, generating predictions, evaluating performance, and visualizing the results.

The model uses four selected numerical features:

- 🏠 `GrLivArea` — Above-ground living area
- 🛏️ `BedroomAbvGr` — Number of bedrooms above ground
- 🛁 `FullBath` — Number of full bathrooms
- 📅 `YearBuilt` — Original construction year

The target variable is:

- 💰 `SalePrice` — Final sale price of the house

---

## 🎯 Project Objectives

The project was developed to accomplish the following tasks:

- Load and explore the Kaggle House Prices dataset
- Inspect the structure and dimensions of the dataset
- Identify missing values
- Select relevant numerical features
- Prepare the data for Machine Learning
- Divide the dataset into training and testing sets
- Train a **Linear Regression** model
- Predict house prices using unseen test data
- Evaluate the model using **R² Score**
- Compare actual and predicted house prices visually
- Save prediction results into a CSV file

---

## 📊 Dataset

The project uses the **House Prices — Advanced Regression Techniques** dataset from Kaggle.

The dataset contains information about residential properties along with their corresponding sale prices.

### Dataset Statistics

| Property | Value |
|---|---:|
| **Total Records** | 1,460 |
| **Total Features/Columns** | 81 |
| **Target Variable** | `SalePrice` |
| **Training Samples** | 1,168 |
| **Testing Samples** | 292 |

### Selected Features

| Feature | Description | Type |
|---|---|---|
| `GrLivArea` | Above-ground living area | Numerical |
| `BedroomAbvGr` | Number of bedrooms above ground | Numerical |
| `FullBath` | Number of full bathrooms | Numerical |
| `YearBuilt` | Original construction year | Numerical |

### Target Variable

| Variable | Description |
|---|---|
| `SalePrice` | Final sale price of the residential property |

---

## 🏗️ Project Architecture

The project follows a simple end-to-end Machine Learning pipeline:

```text
                    ┌──────────────────────┐
                    │   Kaggle Dataset     │
                    │      train.csv       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Data Loading       │
                    │      Pandas          │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Data Exploration     │
                    │ Shape / Missing Data │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Feature Selection     │
                    │                      │
                    │ • GrLivArea          │
                    │ • BedroomAbvGr        │
                    │ • FullBath            │
                    │ • YearBuilt           │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Train-Test Split     │
                    │                      │
                    │ 80% Training        │
                    │ 20% Testing         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Linear Regression    │
                    │      Model           │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Price Prediction      │
                    │                      │
                    │ Predicted SalePrice  │
                    └──────────┬───────────┘
                               │
                  ┌────────────┴────────────┐
                  ▼                         ▼
       ┌──────────────────┐       ┌────────────────────┐
       │ R² Score         │       │ Actual vs Predicted│
       │ Evaluation       │       │ Visualization      │
       └────────┬─────────┘       └─────────┬──────────┘
                │                           │
                └────────────┬──────────────┘
                             ▼
                  ┌────────────────────────┐
                  │ prediction_results.csv │
                  └────────────────────────┘


🔄 Machine Learning Workflow

1️⃣ Load the Dataset

The Kaggle train.csv dataset is loaded using Pandas.

import pandas as pd

data = pd.read_csv("train.csv")

The dataset contains 1,460 records and 81 columns.

2️⃣ Explore the Dataset

The dataset was inspected using:

data.head()
data.shape
data.isnull().sum()

This helped understand:

Number of rows and columns
Available features
Target variable
Missing values
Dataset structure
3️⃣ Handle Missing Values

The dataset contains missing values in several columns.

For this mini project, the selected prediction features were numerical and did not require extensive categorical preprocessing.

The dataset was inspected for missing values before model training to ensure the selected inputs were suitable for the regression model.

4️⃣ Feature Selection

Four important features were selected:

features = ["GrLivArea", "BedroomAbvGr", "FullBath", "YearBuilt"]

These features were chosen because they represent meaningful physical characteristics of a house that can influence its selling price.

5️⃣ Define Target Variable

The target variable was:

target = "SalePrice"

The model learns to estimate SalePrice using the selected features.

6️⃣ Train-Test Split

The dataset was divided into training and testing sets.

Training Data → 80%
Testing Data  → 20%

Actual split used:

Dataset	Records
Training	1,168
Testing	292

The training data is used to teach the model, while the testing data evaluates how well the trained model performs on unseen data.

🤖 Linear Regression Model

The project uses Linear Regression, a supervised machine learning algorithm commonly used for predicting continuous numerical values.

The basic idea is to learn a relationship between input features and the target house price.

Conceptually:

House Features
      │
      ├── GrLivArea
      ├── BedroomAbvGr
      ├── FullBath
      └── YearBuilt
             │
             ▼
      Linear Regression
             │
             ▼
       Predicted Price

The model was trained using Scikit-learn:

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
💰 House Price Prediction

After training, the model was used to predict prices for the test dataset.

predictions = model.predict(X_test)

Example predictions generated by the model:

123619.10
318334.96
101720.32
170545.57
240375.41
119211.72
195534.10
178012.94
117291.77
150770.20

These values represent the estimated selling prices for houses in the testing dataset.

📈 Model Evaluation

The model was evaluated using the R² (R-squared) score.

R² Score
0.7062392402008095
⭐ Final R² Score

R² = 0.7062

An R² score of approximately 0.7062 indicates that the selected features and Linear Regression model explain a substantial portion of the variation in house sale prices within the test dataset.

Since this is a compact mini project using only four features, the result provides a useful baseline for further improvement.

📊 Actual vs Predicted Visualization

The project generates an Actual vs Predicted scatter plot to visually compare:

Actual house prices
Model-predicted house prices

The closer the points are to the ideal diagonal relationship, the closer the predictions are to the actual values.

Visualization

📁 Project Structure
House-Price-Prediction/
│
├── 📄 house_price_prediction.py
│   └── Main machine learning implementation
│
├── 📊 train.csv
│   └── Kaggle House Prices dataset
│
├── 📈 actual_vs_predicted.png
│   └── Actual vs Predicted visualization
│
├── 📋 prediction_results.csv
│   └── Actual and predicted house prices
│
└── 📘 README.md
    └── Project documentation
🛠️ Technologies & Libraries
Programming Language

Machine Learning

Data Processing

Visualization

⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/adhithraghunath006-stack/House-Price-Prediction.git

Navigate into the project:

cd House-Price-Prediction
2. Install Required Libraries

Run:

pip install pandas numpy matplotlib scikit-learn
3. Run the Project

Execute:

python house_price_prediction.py

The program will:

✓ Load the dataset
✓ Explore the data
✓ Check missing values
✓ Select features
✓ Split training/testing data
✓ Train Linear Regression
✓ Generate predictions
✓ Calculate R² score
✓ Generate visualization
✓ Save prediction results
📋 Output Files

After successful execution, the project generates:

actual_vs_predicted.png

Contains the visualization comparing actual and predicted house prices.

prediction_results.csv

Contains the prediction results generated by the trained model.

Example structure:

Actual Price	Predicted Price
Actual SalePrice	Model Prediction
208500	Predicted Value
181500	Predicted Value
223500	Predicted Value
📊 Results Summary
Metric	Result
Dataset Size	1,460 × 81
Features Used	4
Training Samples	1,168
Testing Samples	292
Algorithm	Linear Regression
Evaluation Metric	R² Score
R² Score	0.7062
💡 Key Learnings

Through this project, the following machine learning concepts were practiced:

Understanding a real-world dataset
Data exploration using Pandas
Identifying missing values
Feature selection
Separating features and target variables
Train-test splitting
Supervised learning
Linear Regression
Model prediction
R² model evaluation
Data visualization
Exporting machine learning results
Organizing a complete ML project
🚀 Future Improvements

The current project provides a simple Linear Regression baseline. Its performance could potentially be improved by:

Using more relevant house features
Applying advanced feature engineering
Encoding categorical variables
Handling missing values more extensively
Detecting and treating outliers
Applying feature scaling where appropriate
Comparing multiple regression algorithms
Using Random Forest Regression
Using Gradient Boosting / XGBoost
Performing hyperparameter tuning
Applying cross-validation

A more advanced version could therefore provide more accurate and robust house price predictions.

🎓 Internship Context

This project was completed as part of the:

SkillNexis Machine Learning & AI Internship

Mini Project 2

Project: House Price Prediction Model

The project demonstrates the practical implementation of fundamental machine learning concepts, from data preparation to model evaluation and visualization.

🧠 Project Takeaway

This mini project demonstrates how a machine learning model can learn relationships between house characteristics and historical selling prices.

Although the implementation uses a simple Linear Regression model with only four features, it establishes a complete and reproducible machine learning pipeline that can be expanded into a more advanced house price prediction system.

👨‍💻 About Me

Adhith Raghunathan Nair

🎓 B.Tech Computer Science & Engineering
🏫 Amity University Mumbai
💡 AI/ML Enthusiast | Web Development | Computer Science

I am interested in building practical technology solutions using Artificial Intelligence, Machine Learning, Web Development, and emerging technologies.

⭐ Acknowledgements

SkillNexis — Machine Learning & AI Internship
Kaggle — House Prices Dataset
Scikit-learn — Machine Learning implementation
Pandas — Data processing
Matplotlib — Data visualization
📜 License

This project was developed for educational and internship purposes.

⭐ If you found this project useful

Feel free to explore the repository, review the implementation, and use the project as a reference for learning fundamental machine learning workflows.

Built with Python & Machine Learning by Adhith Raghunathan Nair 🚀
