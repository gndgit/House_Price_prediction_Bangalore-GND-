# 🏠 House Price Prediction at Bangalore

A Machine Learning-based project that predicts the price of houses in Bangalore using key parameters like **Location**, **Square Feet**, **BHK**, and **Number of Bathrooms**. The model provides accurate estimates based on historical housing data and delivers real-time predictions through an interactive web application.

---

## 🎯 Project Objective

The main goal of this project is to help users estimate the market price of a house in Bangalore based on specific input features. By analyzing a dataset of past property sales and listings, we trained a machine learning model that can generalize to new, unseen property data with an accuracy of **82%**.

This can be especially helpful for:

- Homebuyers wanting to check if a price is fair
- Real estate agents estimating property value
- Investors analyzing the housing market

---

## 🧰 Tech Stack

- **Python** (Core Programming Language)
- **Pandas**, **NumPy** (Data Handling & Processing)
- **Scikit-Learn** (Modeling & Evaluation)
- **Streamlit** (Web App Deployment)

---

## 📊 Dataset Information

The project uses two versions of the dataset:

- `Bangalore_House_Data.csv` → Raw dataset containing original entries including missing values, inconsistent formats, and outliers.
- `Bangalore_House_Data_Cleaned.csv` → Cleaned dataset after applying preprocessing techniques.

---

## 📋 Column Descriptions

| Column Name    | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `area_type`    | Type of property area (e.g., Super built-up Area, Plot Area, Carpet Area)  |
| `availability` | Availability status of the property (e.g., Ready to Move, Launch Date)      |
| `location`     | Location/area of the property in Bangalore                                  |
| `size`         | Number of bedrooms (BHK) as a string (e.g., "2 BHK", "4 Bedroom")           |
| `society`      | Name of the housing society (may contain missing values)                    |
| `total_sqft`   | Total area of the property in square feet (can be a range or single value)  |
| `bath`         | Number of bathrooms                                                         |
| `balcony`      | Number of balconies (may have missing values)                               |
| `price`        | Price of the property in lakhs (target variable)                            |

---

## 🔧 Data Preprocessing

Before model training, the following preprocessing steps were applied:

- 🔹 Removed unnecessary columns such as `society`, `availability`, and `balcony` due to missing or irrelevant data
- 🔹 Extracted numeric values from `size` to get number of BHKs
- 🔹 Converted `total_sqft` to a consistent numeric format (handling ranges and non-standard entries)
- 🔹 Removed outliers based on business logic and statistical thresholds
- 🔹 One-hot encoded categorical variables like `location` and `area_type`
- 🔹 Cleaned and scaled the data for better model performance

---

## 🤖 Model Training & Evaluation

Several models were tested, and the one with the best performance (based on cross-validation accuracy) was selected. Key metrics include:

- ✔️ Model Accuracy: **82%**
- ✔️ Tested using multiple validation techniques
- ✔️ Optimized using hyperparameter tuning

---

## 🌐 Streamlit Web Application

The project is deployed using **Streamlit**, which offers a lightweight, interactive UI to input house details and get instant predictions.

### ▶️ How to Run the App Locally:

```bash
streamlit run app.py

## 👨‍💻 Author & Contribution

Developed and maintained by: **Gyanendranath Dash**  
GitHub: [@gndgit](https://github.com/gndgit)