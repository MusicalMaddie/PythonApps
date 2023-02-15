#Sure, here's an example Python script that uses Scipy and Numpy libraries to complete a simple machine learning task using the Iris dataset, which is a free and open source dataset.
#First, let's import the required libraries and load the Iris dataset:
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np

iris = load_iris()
X = iris.data
y = iris.target

#Next, we split the dataset into training and testing sets using the train_test_split() function:
# Maddie : removed random_state=42 from train_test_split to see what randomized returns looked like
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#Now, let's create a K-Nearest Neighbors (KNN) model and fit it to the training data:
k = 3
knn_model = KNeighborsClassifier(n_neighbors=k)
knn_model.fit(X_train, y_train)


#After fitting the model, we can use it to predict the classes of the test data and calculate the accuracy of the model using the accuracy_score() function:
y_pred = knn_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

#Finally, we can print out the confusion matrix to see how many samples were correctly and incorrectly classified:
from sklearn.metrics import confusion_matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", conf_matrix)
