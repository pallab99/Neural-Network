# -*- coding: utf-8 -*-
"""Gradient descent.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P5MUAHCWzpZ0eSN_nKQhu_yWloBcFsE8
"""

import numpy as np
import matplotlib.pyplot as plt

def mean_squared_error(y_true, y_predicted):
     
    # Calculating the loss or cost
    cost = np.sum((y_true-y_predicted)**2) / len(y_true)
    return cost

def gradient_descent(x,y):
  m=1  #initial value of m
  b=0  #initial value of b
  lr=0.001  #Learning Rate 
  itr=2000 #number of iterations
  costs = []
  weights = []
  for i in range(itr):
    current_cost = mean_squared_error(y, m*x+b)
    costs.append(current_cost)
    weights.append(m)
    derivative_b=(-2)*sum(y-m*x-b) #d/db(L) slope of b
    derivative_m=(-2)*sum(x*(y-m*x-b)) #d/db(m) slope of m
    b-=lr*derivative_b #Updating the value of b
    m-=lr*derivative_m #Updating the value of m
    
    print("Step: {} -> b = {} & m = {} ".format(i,round(b, 3),round(m, 3)))

  plt.figure(figsize = (8,6))
  plt.plot(weights, costs)
  plt.scatter(weights, costs, marker='o', color='red')
  plt.title("Cost vs Weights")
  plt.ylabel("Cost")
  plt.xlabel("Weight")
  plt.show()
    
  return m,b

x=np.array([1,3])  #Values of x
y=np.array([2,4])  #values of y
estimated_m, estimated_b = gradient_descent(x, y)
print("Estimated Weight: {}\nEstimated Bias: {}".format(estimated_m,estimated_b))
Y_pred = estimated_m*x + estimated_b
plt.figure(figsize = (8,6))
plt.scatter(x, y, marker='o', color='red')
plt.plot([min(x), max(x)], [min(Y_pred), max(Y_pred)], color='blue',markerfacecolor='red',markersize=10,linestyle='dashed')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()