import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


dataset = pd.read_csv(r"/Users/bannusagi/Documents/Investment.csv")

X = dataset.iloc[:,:-1]
y = dataset.iloc[:,4]

# dummes categorizes the data
X = pd.get_dummies(X, dtype=int)

# split the dataset for train and test
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2,train_size=0.8,random_state=0)

# Train the model
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

#mlr model

m = regressor.coef_
print(m)

c = regressor.intercept_
print(c)

X = np.append(arr = np.ones((50,1)).astype(int),values = X, axis = 1)

import statsmodels.api as sm

X_opt = X[:,[0,1,2,3,4,5]]

#Ordinary Leat Squares
# what is rfe Recursive feature elemination
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
print(regressor_OLS.summary())

X_opt = X[:,[0,1,2,3,5]]

#Ordinary Leat Squares
# what is rfe Recursive feature elemination
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
print(regressor_OLS.summary())

X_opt = X[:,[0,1,2,3]]

#Ordinary Leat Squares
# what is rfe Recursive feature elemination
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
print(regressor_OLS.summary())

X_opt = X[:,[0,1,3]]

#Ordinary Leat Squares
# what is rfe Recursive feature elemination
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
print(regressor_OLS.summary())

X_opt = X[:,[0,1]]

#Ordinary Leat Squares
# what is rfe Recursive feature elemination
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
print(regressor_OLS.summary())

bias = regressor.score(X_train, y_train)
bias

variance = regressor.score(X_test, y_test)
variance