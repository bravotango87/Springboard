#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

import matplotlib.pyplot as plt


# In[2]:


url_LondonHousePrices= "https://data.london.gov.uk/download/uk-house-price-index/70ac0766-8902-4eb5-aab5-01951aaed773/UK%20House%20price%20index.xls"


# In[5]:


properties = pd.read_excel(url_LondonHousePrices, sheet_name='Average price', index_col=
None)


# In[6]:


properties.shape


# In[7]:


properties.head()


# In[8]:


properties_T = properties.T


# In[9]:


print(properties_T)


# In[10]:


properties_T.index


# In[11]:


properties_T = properties_T.reset_index()


# In[12]:


properties_T.index


# In[13]:


properties_T.head()


# In[14]:


properties_T.columns


# In[16]:


properties_T.columns = properties_T.iloc[[0]]


# In[17]:


properties_T.columns = properties_T.iloc[0]


# In[18]:


properties_T.head()


# In[19]:


properties_T = properties_T.drop(0)


# In[20]:


properties_T.head()


# In[21]:


properties_T = properties_T.rename(columns = {'Unnamed: 0':'London_Borough', pd.NaT: 'ID'
})


# In[22]:


properties_T.head()


# In[23]:


properties_T.columns


# In[24]:


clean_properties = pd.melt(properties_T, id_vars= ['London_Borough', 'ID'])


# In[25]:


clean_properties.head()


# In[40]:


clean_properties = clean_properties.rename(columns = {0: 'Month', 'value': 'Average_price'})


# In[41]:


clean_properties.head()


# In[42]:


clean_properties.dtypes


# In[43]:


clean_properties['Average_price'] = pd.to_numeric(clean_properties['Average_price'])


# In[44]:


clean_properties.dtypes


# In[45]:


clean_properties.count()


# In[46]:


clean_properties['London_Borough'].unique()


# In[47]:


clean_properties[clean_properties['London_Borough'] == 'Unnamed: 34'].head()


# In[48]:


clean_properties[clean_properties['London_Borough'] == 'Unnamed: 37'].head()


# In[49]:


clean_properties[clean_properties['ID'].isna()]


# In[50]:


NaNFreeDF1 = clean_properties[clean_properties['Average_price'].notna()]
NaNFreeDF1.head(48)


# In[51]:


NaNFreeDF1.count()


# In[52]:


NaNFreeDF2 = clean_properties.dropna()
NaNFreeDF2.head(48)


# In[53]:


NaNFreeDF2.count()


# In[54]:


NaNFreeDF2['London_Borough'].unique()


# In[55]:


print(clean_properties.shape)
print(clean_properties.shape)
print(NaNFreeDF2.shape)


# In[56]:


nonBoroughs = ['Inner London', 'Outer London',
'NORTH EAST', 'NORTH WEST', 'YORKS & THE HUMBER',
'EAST MIDLANDS', 'WEST MIDLANDS',
'EAST OF ENGLAND', 'LONDON', 'SOUTH EAST',
'SOUTH WEST', 'England']


# In[57]:


NaNFreeDF2[NaNFreeDF2.London_Borough.isin(nonBoroughs)]


# In[58]:


NaNFreeDF2[~NaNFreeDF2.London_Borough.isin(nonBoroughs)]


# In[59]:


NaNFreeDF2 = NaNFreeDF2[~NaNFreeDF2.London_Borough.isin(nonBoroughs)]


# In[60]:


NaNFreeDF2.head()


# In[61]:


df= NaNFreeDF2


# In[62]:


df.head()


# In[63]:


df.dtypes


# In[ ]:




