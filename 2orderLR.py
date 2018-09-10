# -*- coding: utf-8 -*-

from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt

import numpy as np

model = LinearRegression()


data=np.loadtxt('ex1data1.txt')


X=data[:,0:1]

y=data[:,1]


model.fit(X,y)

X1=np.linspace(0,25,100)
Y1=[]
print model.predict(X1[0]),X1[0]

for i in range(100):
    Y1.append(model.predict(X1[i]))

Y1=np.array(Y1)
print X1
print Y1

plt.figure()

plt.scatter(X,y,color="red",label="Sample Point",linewidth=3)

plt.plot(X1,Y1,color="orange",label="Fitting Line",linewidth=3)
plt.legend()
plt.show()
#print(u'预测价格:%.2f$'%model.predict(12))