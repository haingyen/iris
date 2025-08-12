import os
import pickle
import streamlit as st
import pandas as pd  
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# Load
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target
labels = iris.target_names

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=66)

# Train
clf = RandomForestClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# Eval
report = classification_report(y_test, y_pred, target_names=labels)
conf_matrix = confusion_matrix(y_test, y_pred)
accuracy = clf.score(X_test, y_test)

# Create the 'model' directory if it doesn't exist
os.makedirs("model", exist_ok=True)

# Save the trained model to a file
with open("model/iris_model.pkl", "wb") as f:
    pickle.dump(clf, f)

print("Model trained and saved successfully!")
# Streamlit App
