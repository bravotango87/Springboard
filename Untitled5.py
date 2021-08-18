#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


import matplotlib.pyplot as plt


# In[5]:


url_LondonHousePrices = "https://data.london.gov.uk/download/uk-house-price-index/70ac0766-8902-4eb5-aab5-01951aaed773/UK%20House%20price%20index.xls"

properties = pd.read_excel(url_LondonHousePrices, sheet_name='Average price', index_col=None)


# In[6]:


properties.shape


# In[7]:


properties.head()


# In[8]:


properties_T = properties.T


# In[9]:


print(properties.head())


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


# In[15]:


properties_T.columns = properties_T.iloc[0]


# In[16]:


properties_T.columns = properties_T.iloc[0]


# In[17]:


properties_T.head()


# In[18]:


properties_T = properties_T.drop(0)


# In[19]:


properties_T.head()


# In[20]:


properties_T = properties_T.rename(columns = {'Unnamed: 0':'London_Borough', pd.NaT: 'ID'})


# In[21]:


properties_T.head()


# In[22]:


properties_T.columns


# In[23]:


clean_properties = pd.melt(properties_T, id_vars= ['London_Borough', 'ID'])


# In[24]:


clean_properties.head()


# In[25]:


clean_properties = clean_properties.rename(columns = {0: 'Month', 'value': 'Average_price'})


# In[26]:


clean_properties.head()


# In[27]:


clean_properties['Average_price'] = pd.to_numeric(clean_properties['Average_price'])


# In[28]:


clean_properties.dtypes


# In[29]:


clean_properties.count()


# In[30]:


clean_properties['London_Borough'].unique()


# In[31]:


clean_properties[clean_properties['London_Borough'] == 'Unnamed: 34'].head()


# In[32]:


clean_properties[clean_properties['ID'].isna()]


# In[33]:


NaNFreeDF1 = clean_properties[clean_properties['Average_price'].notna()]
NaNFreeDF1.head(48)


# In[34]:


NaNFreeDF1.dropna()


# In[35]:


NaNFreeDF2 = clean_properties.dropna()
NaNFreeDF2.head(48)


# In[36]:


NaNFreeDF2.count()


# In[37]:


NaNFreeDF2['London_Borough'].unique()


# In[38]:


print(clean_properties.shape)
print(clean_properties.shape)
print(NaNFreeDF2.shape)


# In[39]:


nonBoroughs = ['Inner London', 'Outer London',
'NORTH EAST', 'NORTH WEST', 'YORKS & THE HUMBER',
'EAST MIDLANDS', 'WEST MIDLANDS',
'EAST OF ENGLAND', 'LONDON', 'SOUTH EAST',
'SOUTH WEST', 'England']


# In[40]:


NaNFreeDF2[NaNFreeDF2.London_Borough.isin(nonBoroughs)]


# In[41]:


NaNFreeDF2[~NaNFreeDF2.London_Borough.isin(nonBoroughs)]


# In[42]:


NaNFreeDF2 = NaNFreeDF2[~NaNFreeDF2.London_Borough.isin(nonBoroughs)]


# In[43]:


NaNFreeDF2.head()


# In[44]:


df = NaNFreeDF2


# In[45]:


df.head()


# In[46]:


df.dtypes


# In[47]:


camden_prices = df[df['London_Borough'] == 'Camden']


# In[48]:


ax = camden_prices.plot(kind ='line', x = 'Month', y='Average_price')
ax.set_ylabel('Price')


# In[49]:


df['Year'] = df['Month'].apply(lambda t: t.year)
df.tail()


# In[50]:


dfg = df.groupby(by=['London_Borough', 'Year']).mean()
dfg.sample(10)


# In[51]:


dfg = dfg.reset_index()
dfg.head()


# In[52]:


def create_price_ratio(d):
    y1998 = float(d['Average_price'][d['Year']==1998])
    y2018 = float(d['Average_price'][d['Year']==2018])
    ratio = [y2018/y1998]
    return ratio


# In[53]:


create_price_ratio(dfg[dfg['London_Borough']=='Barking & Dagenham'])


# In[54]:


final = {}


# In[55]:


for b in dfg['London_Borough'].unique():
    borough = dfg[dfg['London_Borough'] == b]
    final[b] = create_price_ratio(borough)
print(final)
    


# In[56]:


df_ratios = pd.DataFrame(final)


# In[57]:


df_ratios.head()


# In[58]:


df_ratios_T = df.T
df_ratios = df_ratios_T.reset_index()
df_ratios.head()


# In[59]:


df_ratios.rename(columns={'index':'Borough', 0:'2018'}, inplace=True)
df_ratios.head()


# In[79]:


top15 = df_ratios.sort_values(by='2018',ascending=False).head(15)
print(top15)


# In[82]:


top15.sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')
print(top15)


# In[83]:


data.reset_index().sort_values(['Column','Index']).set_index('Index')


# In[84]:


properties_T = properties_T.reset_index()


# In[89]:


top15 = df_ratios.sort_values(by=['2018'],ascending=False).head(15)
print(top15)


# In[88]:


ip = get_ipython()


# In[91]:


top15 = df_ratios.sort_values(by=['2018'],ascending=False).head(15)
print(top15)


# In[ ]:


ax = top15[['Borough','2018']].plot(kind='bar')
ax.set_xticklabels(top15.Borough)

