#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[16]:


#Reading the dataset
data = pd.read_csv('Table_20.6_Y2015_1.csv')
data = data.set_index('Category', drop = True)

#Segregating the dataset into different categories
PVs = data.loc["Passenger Vehicles (PVs)"].to_numpy()     
HCVs = data.loc["Commercial Vehicles (CVs) M & HCVs"].to_numpy()
LCVs = data.loc["LCVs"].to_numpy()
_3Wh = data.loc["Three Wheelers"].to_numpy()
_2Wh = data.loc["Two wheelers"].to_numpy()

#Forming arrays for line plot
PVs_tarr = PVs[-1][1:]
HCVs_tarr = HCVs[-1][1:]
LCVs_tarr = LCVs[-1][1:]
_3Wh_tarr = _3Wh[-1][1:]
_2Wh_tarr = _2Wh[-1][1:]

#Converting into list
array_PVs = [PVs_tarr[i] for i in range(len(PVs_tarr))]
array_HCVs = [HCVs_tarr[i] for i in range(len(HCVs_tarr))]
array_LCVs = [LCVs_tarr[i] for i in range(len(LCVs_tarr))]
array_3Wh = [_3Wh_tarr[i] for i in range(len(_3Wh_tarr))]
array_2Wh = [_2Wh_tarr[i] for i in range(len(_2Wh_tarr))]


# In[17]:


#Plotting code starts from here

xarr = list(data.columns)
xarr = xarr[1:]

plt.figure(figsize = (8,5), dpi = 130)
plt.plot(np.arange(len(xarr)), array_PVs, label = "Passenger Vehicles", marker = "x", linewidth = 0.6)
plt.plot(np.arange(len(xarr)), array_HCVs, label = "Heavy Commercial Vehicles", marker = "x", linewidth = 0.6)
plt.plot(np.arange(len(xarr)), array_LCVs, label = "Light Commercial Vehicles", marker = "x", linewidth = 0.6)
plt.plot(np.arange(len(xarr)), array_3Wh, label = "Three Wheelers", marker = "o")
plt.plot(np.arange(len(xarr)), array_2Wh, label = "Two Wheelers", marker = "o")
plt.legend(loc= 'best')
plt.xlabel("Year")
plt.ylabel("Automobile production")
plt.grid(which='minor',axis='both',linestyle='--',alpha=0.2)
plt.grid(which='major',axis='y',linestyle='-',alpha=0.5)
plt.minorticks_on()
plt.xticks(ticks = np.arange(len(xarr)), labels = xarr, rotation = 90)
plt.title("Category-wise automobile production-all India (2001-2013)", weight = 'bold')
plt.savefig("Line_plot_example.jpeg", dpi = 200, bbox_inches = 'tight')
plt.show()


# In[ ]:




