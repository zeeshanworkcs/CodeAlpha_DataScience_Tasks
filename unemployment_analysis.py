# Task 2: Unemployment Analysis with Python (CodeAlpha Internship)
# Using both CSV files from Kaggle dataset

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------
# Load File 1: "Unemployment in India.csv"
# ----------------------------
df1 = pd.read_csv("Unemployment in India.csv")

# Clean column names (remove extra spaces)
df1.columns = df1.columns.str.strip()

print("File 1 - Columns:", df1.columns)
print("File 1 - First 5 rows:\n", df1.head())

# Visualization 1: Unemployment Rate Over Time by Region (File 1)
plt.figure(figsize=(12,6))
sns.lineplot(x="Date", y="Estimated Unemployment Rate (%)", data=df1, hue="Region")
plt.xticks(rotation=90)
plt.title("Unemployment Rate Over Time by Region (File 1)")
plt.show()

# Visualization 2: Average unemployment by region (File 1)
region_avg1 = df1.groupby("Region")["Estimated Unemployment Rate (%)"].mean().sort_values()
plt.figure(figsize=(10,6))
region_avg1.plot(kind="bar", color="orange")
plt.title("Average Unemployment Rate by Region (File 1)")
plt.ylabel("Unemployment Rate (%)")
plt.show()


# ----------------------------
# Load File 2: "Unemployment_Rate_upto_11_2020.csv"
# ----------------------------
df2 = pd.read_csv("Unemployment_Rate_upto_11_2020.csv")

# Clean column names
df2.columns = df2.columns.str.strip()

print("File 2 - Columns:", df2.columns)
print("File 2 - First 5 rows:\n", df2.head())

# Visualization 3: Unemployment Rate Trend (File 2)
plt.figure(figsize=(12,6))
sns.lineplot(x="Date", y="Estimated Unemployment Rate (%)", data=df2, hue="Region")
plt.xticks(rotation=90)
plt.title("Unemployment Rate Trend (File 2)")
plt.show()

# Visualization 4: Average unemployment by region (File 2)
region_avg2 = df2.groupby("Region")["Estimated Unemployment Rate (%)"].mean().sort_values()
plt.figure(figsize=(10,6))
region_avg2.plot(kind="bar", color="skyblue")
plt.title("Average Unemployment Rate by Region (File 2)")
plt.ylabel("Unemployment Rate (%)")
plt.show()
