#!/usr/bin/env python
# coding: utf-8

# In[26]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[27]:


#Reading and preprocessing of data
data = pd.read_csv('All_India_Index_july2019_20Aug2020_dec20_1_2.csv')
data = data.dropna()
data = data.iloc[:,:13]
data = data.set_index('Sector', drop = True)
data = data.loc['Rural+Urban']

#Segregating the data into categories
cereals = np.array(data['Cereals and products'])
meat = data['Meat and fish']
egg = data['Egg']
milk = data['Milk and products']
oils = data['Oils and fats']
fruits = data['Fruits']
veggies = data['Vegetables']
pulses = data['Pulses and products']


# In[28]:


data.columns[2:10]


# In[29]:


#Creating box plots
agri_produce = [cereals, meat, egg, milk, oils, fruits, veggies, pulses]
plt.figure(figsize = (13,5), dpi = 100)
plt.boxplot(agri_produce)
plt.xticks([1,2,3,4,5,6,7,8], data.columns[2:10], rotation = 30)
plt.xlabel("Commodity", weight = 'bold')
plt.ylabel("Consumer price index (CPI)", weight = 'bold')
plt.title("Variation of consumer price index (CPI) for period 2013-2021", weight = 'bold')
plt.grid(which='minor',axis='both',linestyle='--',alpha=0.2)
plt.grid(which='major',axis='y',linestyle='-',alpha=0.5)
plt.minorticks_on()
plt.tick_params(axis='x', which='minor', bottom=False)
plt.savefig("Box_plot_example.jpeg", dpi = 200, bbox_inches = 'tight')
plt.show()


# In[ ]:




