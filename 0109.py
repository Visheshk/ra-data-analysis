#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from plotly.offline import iplot
import plotly.graph_objs as go
import numpy as np
import plotly.io as pio
import pandas as pd
import json


# In[2]:


df=pd.read_json("aug23.json",orient='index')


# In[3]:


# len(df) ==33668
# list(df.columns)
print(df["eventKey"].unique())


# In[4]:


flagDf=df[df["eventKey"]=="FlagMoved"]
print(list(flagDf.columns))
# flagDf['activeCreatureCount']
flagDf.head()


# In[5]:


print(flagDf['flags'][0])
print(flagDf['flags'][1])
print(flagDf['flags'][2])
print ("//////////////////")
# print(flagDf['flags'][35])


# In[13]:


## find the max len of flagmoved event ##
lst=[]
for dic in flagDf['flags'][:]:
    length=len(dic)
    lst.append(length)
maxLen=max(lst)
minLen=min(lst)
print (maxLen)
print (minLen)


# In[22]:


## coordLst contains lists of pairs of coords (it's list of lists)

coordLst=[]

for dic in flagDf['flags'][:38]:
    lst=[]
    for k in dic: # k ==0,1,2,3
        val=dic[k] # val is also dictionary
        for v in val:
            x=val["x"]
            y=val["y"]
        tup=(x,y)
        lst.append(tup)
    coordLst.append(lst)
print(coordLst)
print(len(coordLst))


# In[50]:


## Add fake coordinates to make every flag length == 6
fullst=[]
for idx, lst in enumerate (coordLst[:38]):
#     print(len(lst))
    length=len(lst)
    while length <6:
        adcoord=[(0,0)]
        lst.extend(adcoord)
        length +=1
#     print(lst)
    fullst.append(lst)
print(fullst)


# In[51]:


# [(1, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]

def compare(lst1, lst2):
    count = 0
    for i in range(len(lst1)):
        if lst1[i]!= lst2[i]:
            count +=1
    if count ==1:
        return (1)
    else:
        return (2)
compare(fullst[37], fullst[0])


# In[52]:


from pandas import Series, DataFrame
from numpy import array, zeros

# input an array, get matrix
def get_pairmatrix(somearray):
    ResultArray = array(somearray)

    N = ResultArray.shape[0]
    matrix = zeros((N, N)) # N==38
    for i in range(N): # outlst == outer side, compare again,after the inner loop over
        outlst=fullst[i]  # [(1, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]

        for j in range(N):  
            innerlst=fullst[j] # 
#             compare(outlst, innerlst)
            matrix[i, j] = compare(outlst, innerlst)
            matrix[j, i] = matrix[i, j]
    return (matrix)

b=get_pairmatrix(fullst)
small_df = pd.DataFrame(b)
small_df.replace(1, "True", inplace=True)

print(small_df)


# In[32]:


# opt 1: enumerate
for idx, jarr in enumerate(coordLst[:36]): # jarr is current arr, idx+1 == next arr
    count =0
    for j in range(len(jarr)):
        if idx + 1 == len (coordLst):
            break
        if jarr[j] != coordLst[idx+1][j]:
            count +=1
    if count ==1:
        print("True:", idx, idx+1)
    if count !=1:
        print("False:", idx, idx+1)
#     print(coordLst[idx+1] - j )


# In[9]:


for arr in coordLst[:3]: # arr is list of 3 elements : [(1, 0), (0, 0), (0, 0)]
    print(arr)        


# In[10]:


# check the lens of each flagDf['flags'][i]
i=0
for dic in flagDf['flags'][:]:
    count=len(dic.keys())
    i+=1
    if count != 3:
        print(i)
        break


# In[11]:


df.head()


# In[12]:


import math
import numpy as np
df['flags'][0] #dict
retdic={}
for dic in df['flags'][:]:
#     print(dic)
#     print(isinstance(dic, dict))
    if dic is not np.nan and dic !="null":
        for k in dic:
#             print(k)
            val=dic[k] # each val is a dictionary
            for v in val:
                if v =='creatureType':
                    retkey=val[v]
                    if retkey not in retdic:
                        retdic[retkey]=0
                    else:
                        retdic[retkey] +=1
retdic


# In[13]:


df['flags'][3239]


# In[14]:


df['flags'][3240]


# In[15]:


import math
import numpy as np
df['flags'][0] #dict
retdic={}
for dic in df['flags'][:]:
#     print(dic)
#     print(isinstance(dic, dict))
    if isinstance(dic, dict):
        for k in dic:
#             print(k)
            val=dic[k] # each val is a dictionary
            for v in val:
                if v =='creatureType':
                    retkey=val[v]
                    if retkey not in retdic:
                        retdic[retkey]=0
                    else:
                        retdic[retkey] +=1
retdic


# In[ ]:




