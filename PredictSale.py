#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import pandas as pd
import datetime
import time
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# In[13]:


data = pd.read_excel("\\Sample_data.xlsx")
SelectedData = data[['Date', 'qty']]


# In[14]:


SelectedData


# In[15]:


def findDay(date):
	return datetime.datetime.strptime(date, "%m/%d/%Y").weekday()


# In[16]:


x_axis = SelectedData['Date']
y_axis = SelectedData['qty']
b = []
a = []
c = []
d = []
for k in x_axis:
    c.append(k)
for j in y_axis:
    a.append(j)
print(type(a))
epoch = datetime.datetime.utcfromtimestamp(0)


# In[17]:


def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0
for i in x_axis:
    if findDay(i.strftime("%m/%d/%Y")) != 5 and findDay(i.strftime("%m/%d/%Y")) != 6:
        dt_obj = datetime.datetime.strptime(i.strftime("%m/%d/%Y"), "%m/%d/%Y")
        millisec = dt_obj.timestamp() * 1000
        b.append(millisec)

for m in range(len(c)):
    if findDay(c[m].strftime("%m/%d/%Y")) != 5 and findDay(c[m].strftime("%m/%d/%Y")) != 6:
        d.append(a[m])
x,y = np.asarray(b),np.asarray(d)

x = x.reshape(len(b), -1)
y = y.reshape(len(d), -1)


# In[18]:


# Model initialization
regression_model = LinearRegression()
# Fit the data(train the model)
regression_model.fit(x, y)
# Predict
y_predicted = regression_model.predict(x)

# model evaluation
rmse = mean_squared_error(y, y_predicted)
r2 = r2_score(y, y_predicted)

# printing values
print('Slope:' ,regression_model.coef_)
print('Intercept:', regression_model.intercept_)
print('Root mean squared error: ', rmse)
print('R2 score: ', r2)


# In[19]:


# data points
plt.scatter(x, y, s=10)
plt.xlabel('x')
plt.ylabel('y')
# predicted values
plt.plot(x, y_predicted, color='r')
plt.show()


# In[20]:


predictionDate = '9/1/2022'
dt_obj = datetime.datetime.strptime(predictionDate, "%m/%d/%Y")
predictionMilli = (dt_obj.timestamp() * 1000)
print(predictionMilli)
predictionOrders = (predictionMilli * regression_model.coef_) + regression_model.intercept_ 
print (predictionOrders)


# In[ ]:





# In[ ]:




