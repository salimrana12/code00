#!/usr/bin/env python
# coding: utf-8

# In[2]:

import pandas as pd
 In[3]:
city = ['texus', 'clafornia', 'hollywood']
df = pd.DataFrame(city)
df
type(city)
# In[4]:
city1 = ['europe', 'astraliya', 'north koria']
# In[5]:
city2 = ['bangladesh', 'singapur', 'london']
# In[6]:
df = pd.DataFrame(city)
# In[7]:
df
# In[9]:
df = pd.DataFrame(zip(city, city1, city2), columns=['city_in_usa', 'city_in_europe', 'city_in_asia'], index=['ci', 'c2', 'c3'])
In[10]:
df
In[ ]:




