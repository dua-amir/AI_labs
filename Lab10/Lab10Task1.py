import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from collections import Counter
from sklearn.metrics import classification_report

# Step 1: Load the Iris dataset
iris = load_iris()
X = iris.data        # Features
y = iris.target      # Labels

# Step 2: Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Euclidean distance function
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

# Step 4: KNN Classifier
class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = np.array(X)
        self.y_train = np.array(y)

    def predict(self, X):
        return [self._predict(x) for x in X]

    def _predict(self, x):
        # Compute all distances
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
        # Find k nearest samples
        k_indices = np.argsort(distances)[:self.k]
        k_labels = [self.y_train[i] for i in k_indices]
        # Return the most common label
        return Counter(k_labels).most_common(1)[0][0]

# Step 5: Train the Model
model = KNN(k=3)
model.fit(X_train, y_train)

# Step 6: Predict for the entire test set
predictions = model.predict(X_test)

# Step 7: Predict and show a single test point
single_point = X_test[0]
predicted_label = model._predict(single_point)
true_label = y_test[0]

print("Single data point:", single_point)
print("Predicted label for single point:", predicted_label)
print("True label for single point:", true_label)

# Step 8: Accuracy
accuracy = np.mean(predictions == y_test)
print("\nAccuracy on test set:", accuracy)

# Step 9: Classification Report
print("\nClassification Report:")
print(classification_report(y_test, predictions))

