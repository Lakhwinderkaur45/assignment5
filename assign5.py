#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pandas import DataFrame
import pymysql
from sqlalchemy import create_engine


# In[2]:


#raw_df = pd.read_csv('youtube_dataset.csv', sep=',', encoding='gbk')

with open("youtube_dataset.csv") as f:
    print(f.encoding)


# In[3]:


raw_df_top_1000 = pd.read_csv('youtube_dataset.csv', sep=',', encoding='cp1252')
# raw_df_top_1000.head(1000)
raw_df_top_1000= raw_df_top_1000.iloc[:1000]
raw_df_top_1000


# In[4]:


raw_df_top_1000['channeltype'].unique()


# In[5]:


def channeltype_distribution(df,col42,col2):
    count_col= df.groupby(col42)[col2].count()
    return count_col.sort_values(ascending=False)


# In[6]:


channeltype_count=channeltype_distribution(raw_df_top_1000,'channeltype','name')
channeltype_count


# In[ ]:




