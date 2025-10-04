# Iris Flower Classification — CodeAlpha Internship Task 1

## Project Overview

This project is part of my Data Science Internship at CodeAlpha.
The goal of this task is to build a machine learning model that classifies Iris flowers into three species (Setosa, Versicolor, Virginica) based on their physical features.

---

## Dataset

The dataset used is the Iris dataset, which contains the following features:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width
* Species

Dataset Link: [Iris Dataset (Kaggle)](https://www.kaggle.com/datasets/saurabh00007/iriscsv)

---

## Technologies Used

* Python
* Pandas
* Seaborn and Matplotlib (Data Visualization)
* Scikit-learn (Model Training and Evaluation)

---

## Steps Performed

1. Loaded and explored the dataset.
2. Visualized data distributions and relationships using pairplots.
3. Split the dataset into training and testing sets.
4. Trained a Random Forest Classifier model.
5. Evaluated model performance using accuracy and classification report.

---

## Results

* Model Accuracy: ~95–100% (depending on random split)
* The classification report showed high precision, recall, and F1-score for all species.

Sample Output:

```
Model Accuracy: 0.97

              precision    recall  f1-score   support

      setosa       1.00      1.00      1.00        13
  versicolor       0.93      0.93      0.93        15
   virginica       0.93      0.93      0.93        17
```

---

## Acknowledgement

This project was completed as part of the CodeAlpha Internship Program in the Data Science Domain.
