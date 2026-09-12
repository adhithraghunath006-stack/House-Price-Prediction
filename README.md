# 🏠 House Price Prediction Model

### Machine Learning & AI Internship — SkillNexis

A machine learning project developed as part of the **SkillNexis Machine Learning & AI Internship** to predict residential house prices using **Linear Regression**.

The model uses important property-related features such as living area, number of bedrooms, bathrooms, and year built to learn the relationship between property characteristics and their corresponding sale prices.

---

## 👨‍💻 Author

**Adhith Raghunathan Nair**  
B.Tech Computer Science & Engineering  
**Amity University Mumbai**

---

## 📌 Internship Information

| Field | Details |
|---|---|
| **Internship** | SkillNexis Machine Learning & AI Internship |
| **Project** | Mini Project 2 |
| **Project Title** | House Price Prediction Model |
| **Domain** | Machine Learning |
| **Model** | Linear Regression |
| **Dataset** | Kaggle — House Prices Dataset |
| **Programming Language** | Python |

---

## 🎯 Project Objective

The objective of this project is to develop a basic machine learning model capable of predicting house prices based on selected property-related features.

This project demonstrates a complete machine learning workflow, starting from dataset loading and feature selection to model training, prediction, evaluation, and visualization.

### Key Objectives

- Load and explore the House Prices dataset
- Analyze the structure and characteristics of the dataset
- Identify missing values
- Select relevant numerical features
- Prepare data for machine learning
- Split the dataset into training and testing sets
- Train a Linear Regression model
- Predict house prices for unseen test data
- Evaluate model performance using R² Score
- Visualize actual vs predicted house prices
- Save prediction results as a CSV file

---

## 📊 Dataset

The project uses the **House Prices — Advanced Regression Techniques** dataset from Kaggle.

The dataset contains information about residential properties along with their corresponding sale prices.

### Dataset Statistics

- **Total Records:** 1,460
- **Total Columns:** 81
- **Target Variable:** `SalePrice`

### Selected Features

For this mini project, four important numerical features were selected:

| Feature | Description |
|---|---|
| `GrLivArea` | Above-ground living area |
| `BedroomAbvGr` | Number of bedrooms above ground |
| `FullBath` | Number of full bathrooms |
| `YearBuilt` | Original construction year |

### Target Variable

**`SalePrice`**

The target variable represents the final sale price of each residential property.

---

## 🏗️ Project Architecture

```text
                    ┌─────────────────────┐
                    │   Kaggle Dataset    │
                    │      train.csv      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Data Loading &    │
                    │     Exploration     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Missing Value       │
                    │     Analysis        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Feature Selection   │
                    │                     │
                    │ GrLivArea           │
                    │ BedroomAbvGr        │
                    │ FullBath            │
                    │ YearBuilt           │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Train-Test Split    │
                    │                     │
                    │ 80% Training        │
                    │ 20% Testing         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Linear Regression   │
                    │       Model         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Price Prediction    │
                    └──────────┬──────────┘
                               │
                 ┌─────────────┴─────────────┐
                 ▼                           ▼
       ┌───────────────────┐       ┌────────────────────┐
       │   R² Evaluation   │       │ Actual vs Predicted│
       │                   │       │     Visualization  │
       └───────────────────┘       └────────────────────┘
                 │                           │
                 └─────────────┬─────────────┘
                               ▼
                    ┌─────────────────────┐
                    │ Prediction Results  │
                    │      CSV Output     │
                    └─────────────────────┘


🔄 Machine Learning Workflow

The project follows the following workflow:

1. Data Collection

The House Prices dataset was obtained from Kaggle and stored locally as train.csv.

2. Data Loading

The dataset was loaded into Python using Pandas.

import pandas as pd

data = pd.read_csv("train.csv")
3. Data Exploration

The dataset was inspected to understand:

Number of rows and columns
Feature names
Data types
Missing values
Target variable
Basic data structure

The dataset contains:

1460 rows × 81 columns
4. Feature Selection

Four relevant numerical features were selected:

GrLivArea
BedroomAbvGr
FullBath
YearBuilt

These features were selected because they provide meaningful information about the size, capacity, and age of a property.

5. Target Selection

The model predicts:

SalePrice
6. Train-Test Split

The dataset was divided into:

80% Training Data
20% Testing Data

This resulted in:

Training Data: 1168 records
Testing Data: 292 records
7. Model Training

A Linear Regression model from Scikit-learn was trained using the selected features.

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
8. Prediction

After training, the model was used to predict house prices for the testing dataset.

predictions = model.predict(X_test)
9. Model Evaluation

The model performance was evaluated using the R² Score.

from sklearn.metrics import r2_score

r2 = r2_score(y_test, predictions)
10. Visualization

A scatter plot was generated to compare:

Actual House Prices
Predicted House Prices

The closer the points are to the diagonal reference line, the better the predictions match the actual prices.

11. Result Export

The predicted values were saved into:

prediction_results.csv
🤖 Machine Learning Model
Linear Regression

Linear Regression is a supervised machine learning algorithm used to model the relationship between input features and a continuous target variable.

In this project:

Input Features:

GrLivArea
BedroomAbvGr
FullBath
YearBuilt

Output:

Predicted SalePrice

The model attempts to learn a linear relationship between these property characteristics and house prices.

📈 Model Performance

The trained Linear Regression model achieved the following result:

R² Score
0.7062

The R² score indicates that the selected features explain approximately 70.62% of the variation in house sale prices on the test dataset.

Note: This is a basic educational model using only four features. The original dataset contains many additional property characteristics that could be used to improve predictive performance.

📊 Actual vs Predicted Visualization

The project generates a scatter plot comparing actual house prices with the prices predicted by the Linear Regression model.

Visualization

actual_vs_predicted.png

The diagonal reference line represents the ideal situation where:

Actual Price = Predicted Price

Points closer to this line indicate more accurate predictions.

📁 Project Structure
House-Price-Prediction/
│
├── 📄 train.csv
│   └── Kaggle House Prices dataset
│
├── 🐍 house_price_prediction.py
│   └── Complete machine learning implementation
│
├── 📊 actual_vs_predicted.png
│   └── Actual vs Predicted price visualization
│
├── 📄 prediction_results.csv
│   └── Model prediction results
│
└── 📘 README.md
    └── Project documentation
🛠️ Technologies Used
Programming Language
Python
Libraries
Pandas — Data loading and manipulation
NumPy — Numerical operations
Matplotlib — Data visualization
Scikit-learn — Machine learning and model evaluation
Development Environment
Visual Studio Code
Python 3.10
Git & GitHub
Dataset Source
Kaggle — House Prices Dataset
⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/adhithraghunath006-stack/House-Price-Prediction.git
2. Navigate to the Project
cd House-Price-Prediction
3. Install Required Libraries
pip install pandas numpy matplotlib scikit-learn
4. Run the Project
python house_price_prediction.py
📤 Output Files

After running the project, the following outputs are generated:

prediction_results.csv

Contains the actual and predicted house prices for the testing dataset.

actual_vs_predicted.png

Contains the visualization comparing actual house prices with predicted house prices.

🔍 Sample Prediction Output

Example predictions generated by the trained model:

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

These values represent the predicted sale prices for selected houses from the testing dataset.

📌 Key Learning Outcomes

Through this project, the following machine learning concepts were implemented:

Dataset exploration
Feature selection
Target variable identification
Train-test splitting
Supervised learning
Linear Regression
Model prediction
R² model evaluation
Data visualization
CSV result generation
End-to-end machine learning workflow
🚀 Future Improvements

The model can be improved further by:

Using more features from the original dataset
Applying advanced feature engineering
Handling categorical variables
Performing feature scaling where appropriate
Comparing Linear Regression with other regression algorithms
Using Random Forest or Gradient Boosting models
Performing hyperparameter tuning
Applying cross-validation
Using advanced regression techniques such as XGBoost

These improvements could potentially increase the model's predictive accuracy.

🎓 Internship Context

This project was completed as Mini Project 2 during the SkillNexis Machine Learning & AI Internship.

The project focuses on understanding the fundamentals of regression-based machine learning and implementing a complete prediction pipeline using a real-world dataset.

🏁 Conclusion

The House Price Prediction Model successfully demonstrates how machine learning can be used to estimate residential property prices based on selected property characteristics.

A Linear Regression model was trained using GrLivArea, BedroomAbvGr, FullBath, and YearBuilt as input features. The model achieved an R² Score of 0.7062 on the test dataset.

The project provides a simple yet complete implementation of the machine learning lifecycle:

Data
  ↓
Exploration
  ↓
Feature Selection
  ↓
Train-Test Split
  ↓
Model Training
  ↓
Prediction
  ↓
Evaluation
  ↓
Visualization
  ↓
Result Export

This project serves as a practical demonstration of applying Python and Machine Learning techniques to a real-world regression problem.

👨‍💻 Developer

Adhith Raghunathan Nair
B.Tech Computer Science & Engineering
Amity University Mumbai

⭐ If you found this project useful, feel free to explore the repository and the implementation.
