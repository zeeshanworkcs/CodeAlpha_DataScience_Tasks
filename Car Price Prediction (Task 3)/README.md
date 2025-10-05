# Task 3: Car Price Prediction with Machine Learning

This project is part of my **CodeAlpha Data Science Internship**.
The objective of this task is to build a regression model that predicts the **selling price of cars** based on features like brand, year, fuel type, kilometers driven, etc.

---

## 📌 Dataset

The dataset contains details of 301 cars with the following columns:

* **Car_Name** – Name of the car
* **Year** – Year of manufacture
* **Selling_Price** – Price at which the car is being sold
* **Present_Price** – Price of the car when it was new
* **Driven_kms** – Kilometers driven
* **Fuel_Type** – Type of fuel (Petrol/Diesel/CNG)
* **Selling_type** – Dealer or Individual
* **Transmission** – Manual or Automatic
* **Owner** – Number of previous owners

---

## 🛠️ Steps Performed

1. Loaded dataset using Pandas.
2. Checked data info and missing values.
3. Converted categorical columns into numeric using one-hot encoding.
4. Split data into **train** and **test sets**.
5. Trained a **Linear Regression model** using scikit-learn.
6. Evaluated performance using **R² Score** and **Mean Squared Error (MSE)**.
7. Visualized Actual vs Predicted Car Prices.

---

## 📊 Results

* **R² Score:** ~0.60
* **MSE:** ~9.22

The model explains around **60% of the variance** in car prices, which is reasonable for a simple regression model.

---

## 📂 Files in this folder

* `Car_Price_Prediction.py` – Python code for prediction
* `README.md` – Project description
* `Link Detaset` - https://www.kaggle.com/datasets/vijayaadithyanvg/car-price-predictionused-cars
