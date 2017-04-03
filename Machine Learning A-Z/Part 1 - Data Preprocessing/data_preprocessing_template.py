#### Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values


# Splitting the dataset into the Training set and Test set
#from sklearn.cross_validation import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

"""
# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
## Fit and transform 
X_train = sc_X.fit_transform(X_train)
## only transform because it's already fit
X_test = sc_X.transform(X_test)
"""

## Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,y)

## Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
## PolyFeatures will transform the linear matrix to another matrix 
## with polymons 
poly_reg = PolynomialFeatures(degree=3) ### You can add degres of freddom to best fit the model
X_poly = poly_reg.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly,y)

## visualising the Linear Regression results
plt.scatter(X,y,color= 'red')
plt.plot(X,lin_reg.predict(X),color= 'blue')
plt.title('Trug of Bluff (Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()


## visualising the Polynomial Regression results
plt.scatter(X,y,color= 'red')
plt.plot(X,lin_reg_2.predict(poly_reg.transform(X)),color= 'blue')
plt.title('Trug of Bluff (Polynomial Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()