import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

def getFx(x,fx):
    i=0
    ans=0
    while i<len(fx):
        ans+=np.power(x,i)*fx[i]
        i+=1
    return ans

def getPolyPoints(a,b,fx):
    x=np.linspace(a,b,100)
    y=np.zeros_like(x)
    for i,elem in enumerate(x):
        y[i]=getFx(elem,fx)
    return x,y

data=pd.read_csv("data.csv")
data_array=data.values
data_x=data_array[:,0]
data_y=data_array[:,1]

data_x=np.reshape(data_x,(-1,1))
data_y=np.reshape(data_y,(-1,1))

data_x=np.hstack((data_x,data_x[:,0:1]**2))
data_x=np.hstack((data_x,data_x[:,0:1]**3))
data_x=np.hstack((data_x,data_x[:,0:1]**4))
data_x=np.hstack((data_x,data_x[:,0:1]**5))

print(data_x)
reg=LinearRegression().fit(data_x,data_y)

coef=reg.coef_
intercept=reg.intercept_

intercept=np.reshape(intercept,(1,1))
data_all=np.vstack((intercept,coef.T))

draw_x,draw_y=getPolyPoints(0.3,0.9,data_all)

plt.scatter(data_x[:,0:1],data_y)
plt.plot(draw_x,draw_y)
plt.show()
