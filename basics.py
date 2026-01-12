#####Numpy refresh

import numpy as np

#Create arrays

x = np.array([1,2,3,4,5])
y= np.random.randn(1000) #1000 random values from normal distribution

#Basic operation

x*2
x+10
x.mean()
x.std

#Vectorised math
returns = np.random.randn(1000)*0.01
prices = 100*np.exp(np.cumsum(returns))



