# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt 
from LinearR import computeCost,gradientDescent


data=np.loadtxt('ex1data1.txt')

#print a,a.shape[0]

X=data[:,0:1]

y=data[:,1]

m=X.shape[0]

X=np.column_stack((np.ones((m,1)),X))

#theta=np.ones((2,1))

theta=np.array([0.0,0.0])

iterations = 1500
alpha = 0.01

J=computeCost(X, y, theta)

theta = gradientDescent(X, y, theta, alpha, iterations)
#pp=np.dot(X,theta)
#print DC(pp,y).sum()

print theta

plt.figure(figsize=(8,6))
plt.scatter(X[:,1],y,color="red",label="Sample Point",linewidth=3) 
x=np.linspace(0,25,100)
y=theta[1]*x+theta[0]
plt.plot(x,y,color="orange",label="Fitting Line",linewidth=2) 
plt.legend()
plt.show()
