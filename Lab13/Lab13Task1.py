import pandas as pd
from sklearn import tree
import matplotlib.pyplot as plt

# Step 1: Load dataset from CSV file
data = pd.read_csv("C:/Users/ACG/Downloads/study_dataset.csv")

# Step 2: Separate features and labels
X = data.drop("Pass", axis=1)  # Features: Hours_Studied, Sleep_Hours, Tuition_Attended
Y = data["Pass"]               # Labels: Pass (0/1)

# Step 3: Create and train the Decision Tree model
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

# Step 4: Make a prediction
# Predict for: Studied 3 hours, Slept 7 hours, Attended tuition
sample = [[3, 7, 1]]
prediction = clf.predict(sample)

print("Will the student pass? (1 = Yes, 0 = No):", prediction[0])

# Step 5: Visualize the Decision Tree
plt.figure(figsize=(12, 8))
tree.plot_tree(clf,
               feature_names=["Hours_Studied", "Sleep_Hours", "Tuition_Attended"],
               class_names=["Fail", "Pass"],
               filled=True)
plt.title("Decision Tree - Student Pass Prediction")
plt.show()
