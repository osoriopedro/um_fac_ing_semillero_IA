# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 12:00:51 2021

@author: David
"""

import numpy as np
import matplotlib.pyplot as plt 

from sklearn.linear_model import LinearRegression 
def f(x):
    np.random.seed(42)
    y = 0.1*x + 1.25 + 0.2*np.random.randn(x.shape[0])
    return y
x = np.arange(0, 100, 0.5) 
y = f(x) 
plt.scatter(x,y,label='data', color='red')
plt.title('Datos');