
# -*- coding: utf-8 -*-
import numpy as np

def computeCost(X,y,theta):  
    '''''computes cost given predicted and actual values'''  
    m = X.shape[0]#number of training examples  

    J=0
    J=np.dot(X,theta)-y
    J=J*J

    J=J.sum()/(2*m)
    
    return J

def gradientDescent(X, y, theta, alpha, iterations):  
    '''''compute gradient'''  
    m=X.shape[0]
    
    for _ in range(iterations):

        J=np.dot(X,theta)-y
    

        t1=theta[0]-(J*X[:,0]).sum()/m*alpha
        t2=theta[1]-(J*X[:,1]).sum()/m*alpha
        
        
        theta[0]=t1
        theta[1]=t2
    
    return theta