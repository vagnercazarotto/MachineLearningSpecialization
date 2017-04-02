#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 16:45:29 2017

@author: vagnercazarotto
"""

# Data Preprocessing Template
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50-Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# Encoding categorical data
# Encoding the Independent Variable State
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()


## Avoiding the Dummy Variable Trap..
X = X[:, 1:]


# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

## Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)


## Predicting the Test set results
y_pred = regressor.predict(X_test)


## Building the optimal model using Backward Elimination
import statsmodels.formula.api as sm
## in this library we need to add a columns of ones to be able to use Backward Elimination
X = np.append(arr = np.ones((50,1)).astype(int) , values = X , axis = 1)

### Starting Backward Elimination
#1) Create a new matriz of features 
X_optimal = X[:, [0,1,2,3,4]] ## Start with all the independent variables
regressor_OLS = sm.OLS(endog=y , exog=X_optimal).fit() 
## Fit the full model with all possibles predictios
### Condiser the predictor with the highest P-value. If P > SL remove the predictor 
# otherwise finish the model
regressor_OLS.summary()  ## get information about the model

## IF P>|t| is bigger than Sl = 0.05 it should be removed one by one
##

X_optimal = X[:, [0,1,2,4]] ## Start with all the independent variables
regressor_OLS = sm.OLS(endog=y , exog=X_optimal).fit() 
regressor_OLS.summary()  ## get information about the model

X_optimal = X[:, [0,2,4]] ## Start with all the independent variables
regressor_OLS = sm.OLS(endog=y , exog=X_optimal).fit() 
regressor_OLS.summary()  ## get information about the model

X_optimal = X[:, [0,2]] ## Start with all the independent variables
regressor_OLS = sm.OLS(endog=y , exog=X_optimal).fit() 
regressor_OLS.summary()  ## get information about the model