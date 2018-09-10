# -*- coding: utf-8 -*-
import numpy as np
f=open(r'ex1data1.txt','r')

s=f.read()

s=s.replace(',',' ')
a=0
print len(s)

for i in range(len(s)):
    if s[i]==',':

        a=a+1
f.close()
print a
f=open(r'ex1data1.txt','w')
f.write(s)
f.close()

theta=np.array([0,0])

a=1
b=2
for i in range(5):
    a=theta[0]+1
    b=theta[1]+1
    theta[0]=a
    theta[1]=b

    print theta
