#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[13]:


df = pd.read_csv(r"C:\Users\vmsof\Desktop\test.csv")
df


# In[14]:


df.set_index('customer_id')


# In[15]:


group_by_frame = df.groupby('occupation')


# In[89]:


print(plt.style.available)
plt.style.use('fivethirtyeight')


# In[90]:


df.plot(kind='line', title = 'Analyzing Bank Customer Behavior',use_index = True , xlabel='Daily Rating' , ylabel='Scores', figsize = (10,5), grid = True)


# In[50]:


df.plot(kind= 'bar',figsize = (10,7), stacked= True)


# In[52]:


df.plot.barh(stacked=True,figsize = (10,5))


# In[61]:


df.plot.scatter(x='customer_id',y='occupation',figsize = (5,3), s=100, c= 'Blue')


# In[68]:


df.plot.hist(bins=50)


# In[79]:


df.plot.area(figsize=(10,7))


# In[85]:


df.plot.pie(y='vintage', figsize=(10,6))


# In[87]:


print(plt.style.available)
plt.style.use('seaborn-v0_8-deep')


# In[ ]:




