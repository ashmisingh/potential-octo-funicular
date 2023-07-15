# -*- coding: utf-8 -*-
"""Copy of Project: Heart Disease Prediction

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16dtWE1tUSKSdbBBEjdVjJQAaadP5DTrq

Importing the Dependencies
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Data Collection and Processing

"""

heart_data = pd.read_csv('heart_disease_data.csv')

# print first 5 rows of the dataset
heart_data.head()

# number of rows and columns in the dataset
heart_data.shape

# checking for missing values
heart_data.isnull().sum()

heart_data.describe()

# checking the distribution of Target Variable
heart_data['target'].value_counts()

"""1 --> Defective Heart

0 --> Healthy Heart
"""

#splitting the features and target
X = heart_data.drop(columns = 'target', axis = 1)
Y = heart_data['target']

print(X)

print (Y)

#Splitting the Data into Training data & Test Data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.1, stratify=Y, random_state = 4)

print (X.shape, X_train.shape, X_test.shape)

# training the LogisticRegression model with Training data
model = LogisticRegression()

model.fit(X_train, Y_train)

# accuracy on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

# accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print("Accuracy on training data : ", training_data_accuracy)

print("Accuracy on test data : ", test_data_accuracy)

"""Building a Predictive System"""

input_data = 	(58,	1,	0,	128,	216,	0,	0,	141,	0,	1.2,	2,	3,	4)
input_data_as_numpy_array= np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
prediction = model.predict(input_data_reshaped)
print(prediction)
if (prediction[0]== 0):
  print('The Person is not suffering with any Heart Disease')
else:
  print('The Person has Heart Disease')

