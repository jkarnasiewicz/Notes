# -*- coding: utf-8 -*-

# Fluent python
# check import order in metaprograming chapter
# 717 python jargon
# raise from lambda !

# ML/25
# JS/31

# Machine Learning

# quandl / http://archive.ics.uci.edu/ml/datasets.html
# Linear Regression(Regresja liniowa)(best fitting line)/Coefficient of determination(Współczynnik determinacji)
# Classification k-Nearest Neighbors(not scaling well)/Accuracy(dokładność/trafność)
# Classification Support Vector Machine(SVM)/Best separated hyperplane/Convex optimization problem



# Scikit-learn
# X - features, y - labels(possible outputs called classes)
# The individual items are called samples in machine learning, and their properties are called features
# The shape of the data array is the number of samples multiplied by the number of features
# dataset['data'].shape
import numpy as np
from sklearn.datasets import load_iris
iris_dataset = load_iris()
print(iris_dataset.keys(), iris_dataset['feature_names'], iris_dataset['target_names'], iris_dataset['data'].shape)



# training data and test data
# One part of the data is used to build our machine learning model, and is called the training data or training set
# The rest of the data will be used to assess how well the model works, this is called the test data
# We cannot use the data we used to build the model to evaluate it. This is because our model can always
# simply remember the whole training set

# train_test_split (shuffles the dataset and splits it)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)



# k-Nearest Neighbors
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)

# build the model using training set
knn.fit(X_train, y_train)

# making predictions
X_new = np.array([[5, 2.9, 1, 0.2]])
prediction = knn.predict(X_new)

print("Predicted target name: {}".format(iris_dataset['target_names'][prediction]))



# model evaluation(oszacowanie)/compute the test set accuracy
# we can measure how well the model works by computing the accuracy(dokładność, trafność) on test_data(X_test)
accuracy = knn.score(X_test, y_test)
print("Test set score: {:.2f}".format(accuracy))
