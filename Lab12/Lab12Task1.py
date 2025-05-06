# Import libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('C:/Users/ACG/Downloads/svm_dataset.csv')
data.columns = [col.strip() for col in data.columns]  # Clean extra spaces

# Use correct column names from your dataset
X = data[['Feature1 (X1)', 'Feature2 (X2)']].values
y = data['Label (Y)'].values

# Split into training and testing data (70% train, 30% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create the SVM model
model = SVC(kernel='linear')
model.fit(X_train, y_train)

# Predict on test set and print accuracy
accuracy = model.score(X_test, y_test)
print("Accuracy:", accuracy)

# Plotting
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm')
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# Create grid to evaluate model
xx = np.linspace(xlim[0], xlim[1])
yy = np.linspace(ylim[0], ylim[1])
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = model.decision_function(xy).reshape(XX.shape)

# Plot decision boundary and margins
ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5,
           linestyles=['--', '-', '--'])
plt.title('SVM Decision Boundary')
plt.xlabel('Feature 1 (X1)')
plt.ylabel('Feature 2 (X2)')
plt.show()
