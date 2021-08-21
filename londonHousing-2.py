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


# In[126]:


properties_T = properties_T.rename(columns = {'Unnamed: 0':'London_Borough', pd.NaT: 'ID'
})


# In[127]:


properties_T.head()


# In[128]:


properties_T.columns


# In[129]:


clean_properties = pd.melt(properties_T, id_vars= ['London_Borough', 'ID'])


# In[130]:


clean_properties.head()


# In[131]:


clean_properties = clean_properties.rename(columns = {0: 'Month', 'value': 'Average_price'})


# In[132]:


clean_properties.head()


# In[133]:


clean_properties.dtypes


# In[134]:


clean_properties['Average_price'] = pd.to_numeric(clean_properties['Average_price'])


# In[135]:


clean_properties.dtypes


# In[136]:


clean_properties.count()


# In[137]:


clean_properties['London_Borough'].unique()


# In[138]:


clean_properties[clean_properties['London_Borough'] == 'Unnamed: 34'].head()


# In[139]:


clean_properties[clean_properties['London_Borough'] == 'Unnamed: 37'].head()


# In[140]:


clean_properties[clean_properties['ID'].isna()]


# In[141]:


NaNFreeDF1 = clean_properties[clean_properties['Average_price'].notna()]
NaNFreeDF1.head(48)


# In[142]:


NaNFreeDF1.count()


# In[143]:


NaNFreeDF2 = clean_properties.dropna()
NaNFreeDF2.head(48)


# In[144]:


NaNFreeDF2.count()


# In[145]:


NaNFreeDF2['London_Borough'].unique()


# In[146]:


print(clean_properties.shape)
print(clean_properties.shape)
print(NaNFreeDF2.shape)


# In[147]:


nonBoroughs = ['Inner London', 'Outer London',
'NORTH EAST', 'NORTH WEST', 'YORKS & THE HUMBER',
'EAST MIDLANDS', 'WEST MIDLANDS',
'EAST OF ENGLAND', 'LONDON', 'SOUTH EAST',
'SOUTH WEST', 'England']


# In[148]:


NaNFreeDF2[NaNFreeDF2.London_Borough.isin(nonBoroughs)]


# In[149]:


NaNFreeDF2[~NaNFreeDF2.London_Borough.isin(nonBoroughs)]


# In[150]:


NaNFreeDF2 = NaNFreeDF2[~NaNFreeDF2.London_Borough.isin(nonBoroughs)]


# In[151]:


NaNFreeDF2.head()


# In[152]:


df= NaNFreeDF2


# In[153]:


df.head()


# In[154]:


df.dtypes


# In[155]:


camden_prices = df[df['London_Borough'] == 'Camden']


# In[156]:


ax = camden_prices.plot(kind ='line', x = 'Month', y='Average_price')
ax.set_ylabel('Price')


# In[157]:


df['Year'] = df['Month'].apply(lambda t: t.year)
df.tail()


# In[158]:


dfg = df.groupby(by=['London_Borough', 'Year']).mean()
dfg.sample(10)


# In[159]:


dfg = dfg.reset_index()
dfg.head()


# In[160]:


def create_price_ratio(d):
    y1998 = float(d['Average_price'][d['Year']==1998])
    y2018 = float(d['Average_price'][d['Year']==2018])
    ratio = [y2018/y1998]
    return ratio


# In[161]:


create_price_ratio(dfg[dfg['London_Borough']=='Barking & Dagenham'])


# In[162]:


final = {}


# In[163]:


for b in dfg['London_Borough'].unique():
    borough = dfg[dfg['London_Borough'] == b]
    final[b] = create_price_ratio(borough)
print(final)


# In[164]:


df_ratios = pd.DataFrame(final)


# In[165]:


df_ratios.head()


# In[166]:


df_ratios_T = df_ratios.T
df_ratios = df_ratios_T.reset_index()
df_ratios.head()


# In[167]:


df_ratios.rename(columns={'index':'London_Borough', 0:'2018'}, inplace=True)
df_ratios.head()


# In[168]:


top15= df_ratios.sort_values(by='2018',ascending=False).head(15)
print(top15)


# In[169]:


ax= top15[['London_Borough','2018']].plot(kind='bar')
ax.set_xticklabels(top15.London_Borough)


# In[ ]:




