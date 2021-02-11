# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 12:26:07 2021

@author: David
"""

import numpy as np 
import matplotlib.pyplot as plt 

from sklearn.linear_model import LinearRegression 
def f(x):
    np.random.seed(42) 
    y = 0.1*x + 1.25 + 0.2*np.random.randn(x.shape[0])
    return y
x = np.arange(0, 20, 0.5) 
y = f(x)
plt.scatter(x,y,label='data', color='green')
plt.title('Datos Ingresados');


from sklearn.linear_model import LinearRegression 
regresion_lineal = LinearRegression() 

regresion_lineal.fit(x.reshape(-1,1), y) 

print('w = ' + str(regresion_lineal.coef_) + ', b = ' + str(regresion_lineal.intercept_))