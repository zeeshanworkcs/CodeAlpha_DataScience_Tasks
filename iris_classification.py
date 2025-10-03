# Iris Flower Classification - CodeAlpha Internship Task 1

# Step 1: Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Step 2: Load dataset
df = pd.read_csv("Iris.csv")   # Make sure Iris.csv is in your project folder
print("First 5 rows of dataset:\n", df.head())

# Step 3: Data visualization (optional)
sns.pairplot(df.drop("Id", axis=1), hue="Species")
plt.show()

# Step 4: Split data (features & target)
X = df.drop(["Id", "Species"], axis=1)   # input columns
y = df["Species"]                        # target column

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)

# Step 5: Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 6: Predictions
y_pred = model.predict(X_test)

# Step 7: Evaluation
print("\nModel Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
