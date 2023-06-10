#!/usr/bin/env python
# coding: utf-8

# In[2]:


#add all csv files into dataframes
import pandas as pd
df1 = pd.read_csv('Top_100_NCAA_100m_men.csv')
df2 = pd.read_csv('Top_100_NCAA_200m.csv')
df3 = pd.read_csv('Top_100_NCAA_400m.csv')
df4 = pd.read_csv('Top_100_NCAA_800m.csv')
df5 = pd.read_csv('Top_100_NCAA_1500m.csv')
df6 = pd.read_csv('Top_100_NCAA_3000S.csv')
df7 = pd.read_csv('Top_100_NCAA_5000m.csv')
df8 = pd.read_csv('Top_100_NCAA_10000m.csv')
df9 = pd.read_csv('Top_100_NCAA_110H.csv')
df10 = pd.read_csv('Top_100_NCAA_400H.csv')
df11 = pd.read_csv('Top_100_NCAA_4X100m.csv')
df12 = pd.read_csv('Top_100_NCAA_4X400m.csv')
df13 = pd.read_csv('Top_100_NCAA_Highjump.csv')
df14 = pd.read_csv('Top_100_NCAA_PoleVault.csv')
df15 = pd.read_csv('Top_100_NCAA_Longjump.csv')
df16 = pd.read_csv('Top_100_NCAA_Triplejump.csv')
df17 = pd.read_csv('Top_100_NCAA_ShotPut.csv')
df18 = pd.read_csv('Top_100_NCAA_Discus.csv')
df19 = pd.read_csv('Top_100_NCAA_Hammer.csv')
df20 = pd.read_csv('Top_100_NCAA_Javelin.csv')
df21 = pd.read_csv('Top_100_NCAA_Decathlon.csv')


# In[44]:


#top 8 finishers/first-team all americans for each event- 100m

df1.head(8)


# In[45]:


#top 8 finishers/first-team all americans for each event- 200m

df2.head(8)


# In[46]:


#top 8 finishers/first-team all americans for each event- 400m
df3.head(8)


# In[47]:


#top 8 finishers/first-team all americans for each event- 800m
df4.head(8)


# In[48]:


#top 8 finishers/first-team all americans for each event- 1500m
df5.head(8)


# In[49]:


#top 8 finishers/first-team all americans for each event- 3000 Steeplechase
df6.head(8)


# In[50]:


#top 8 finishers/first-team all americans for each event- 5000m
df7.head(8)


# In[51]:


#top 8 finishers/first-team all americans for each event- 10,000m
df8.head(8)


# In[52]:


#top 8 finishers/first-team all americans for each event- 110H
df9.head(8)


# In[53]:


#top 8 finishers/first-team all americans for each event- 400H
df10.head(8)


# In[54]:


#top 8 finishers/first-team all americans for each event-4X100 
df11.head(8)


# In[55]:


#top 8 finishers/first-team all americans for each event- 4X400m
df12.head(8)


# In[56]:


#top 8 finishers/first-team all americans for each event- High Jump
df13.head(8)


# In[57]:


#top 8 finishers/first-team all americans for each event- Pole vault
df14.head(8)


# In[58]:


#top 8 finishers/first-team all americans for each event- Long Jump
df15.head(8)


# In[59]:


#top 8 finishers/first-team all americans for each event- Triple Jump
df16.head(8)


# In[60]:


#top 8 finishers/first-team all americans for each event- Shot Put
df17.head(8)


# In[61]:


#top 8 finishers/first-team all americans for each event- Discus
df18.head(8)


# In[62]:


#top 8 finishers/first-team all americans for each event- Hammer Throw
df19.head(8)


# In[63]:


#top 8 finishers/first-team all americans for each event- Javelin
df20.head(8)


# In[43]:


#top 8 finishers/first-team all americans for each event- Decathlon
df21.head(8)


# In[3]:


#Points rewarded to top 8 finishers in each event
points = [10,8,6,5,4,3,2,1]


# In[4]:


#adds points column to each dataframe
for df_name in ['df1', 'df2', 'df3','df4','df5','df6','df7','df8','df9','df10','df11','df12','df13','df14','df15','df16','df17','df18','df19','df20','df21']:
    df = globals()[df_name]  # Get the DataFrame by its name
    df.loc[0:7, 'points'] = points


# In[5]:


#creating csv files for top 8 finisishers - 100m
top_8_100m = df1.head(8)
top_8_100m.to_csv(r'C:\Users\marit\Downloads\Top_8_100m', index=False, header=True)


# In[6]:


#creating csv files for top 8 finisishers - 200m
top_8_200m = df2.head(8)
top_8_200m.to_csv(r'C:\Users\marit\Downloads\Top_8_200m', index=False, header=True)


# In[7]:


#creating csv files for top 8 finisishers - 400m
top_8_400m = df3.head(8)
top_8_400m.to_csv(r'C:\Users\marit\Downloads\Top_8_400m', index=False, header=True)


# In[8]:


#creating csv files for top 8 finisishers - 100m
top_8_800m = df4.head(8)
top_8_800m.to_csv(r'C:\Users\marit\Downloads\Top_8_800m', index=False, header=True)


# In[9]:


#creating csv files for top 8 finisishers - 1500m
top_8_1500m = df5.head(8)
top_8_1500m.to_csv(r'C:\Users\marit\Downloads\Top_8_1500m', index=False, header=True)


# In[10]:


#creating csv files for top 8 finisishers - 100m
top_8_3000S = df6.head(8)
top_8_3000S.to_csv(r'C:\Users\marit\Downloads\Top_8_3000S', index=False, header=True)


# In[11]:


#creating csv files for top 8 finisishers - 5000m
top_8_5000m = df7.head(8)
top_8_5000m.to_csv(r'C:\Users\marit\Downloads\Top_8_5000m', index=False, header=True)


# In[12]:


#creating csv files for top 8 finisishers - 10000m
top_8_10000m = df8.head(8)
top_8_10000m.to_csv(r'C:\Users\marit\Downloads\Top_8_10000m', index=False, header=True)


# In[13]:


#creating csv files for top 8 finisishers - 110H
top_8_110H = df9.head(8)
top_8_110H.to_csv(r'C:\Users\marit\Downloads\Top_8_110H', index=False, header=True)


# In[14]:


#creating csv files for top 8 finisishers - 400H
top_8_400H = df10.head(8)
top_8_400H.to_csv(r'C:\Users\marit\Downloads\Top_8_400H', index=False, header=True)


# In[15]:


#creating csv files for top 8 finisishers - 4x100
top_8_4x100 = df11.head(8)
top_8_4x100.to_csv(r'C:\Users\marit\Downloads\Top_8_4x100', index=False, header=True)


# In[16]:


#creating csv files for top 8 finisishers - 4x400
top_8_4x400 = df12.head(8)
top_8_4x400.to_csv(r'C:\Users\marit\Downloads\Top_8_4x400', index=False, header=True)


# In[17]:


#creating csv files for top 8 finisishers - High Jump
top_8_Highjump = df13.head(8)
top_8_Highjump.to_csv(r'C:\Users\marit\Downloads\Top_8_Highjump', index=False, header=True)


# In[18]:


#creating csv files for top 8 finisishers - Pole Vault
top_8_Polevault = df14.head(8)
top_8_Polevault.to_csv(r'C:\Users\marit\Downloads\Top_8_polevault', index=False, header=True)


# In[19]:


#creating csv files for top 8 finisishers - Long Jump
top_8_Longjump = df15.head(8)
top_8_Longjump.to_csv(r'C:\Users\marit\Downloads\Top_8_Longjump', index=False, header=True)


# In[20]:


#creating csv files for top 8 finisishers - Triple Jump
top_8_Triplejump = df16.head(8)
top_8_Triplejump.to_csv(r'C:\Users\marit\Downloads\Top_8_Triplejump', index=False, header=True)


# In[21]:


#creating csv files for top 8 finisishers - Shot put
top_8_Shotput = df17.head(8)
top_8_Shotput.to_csv(r'C:\Users\marit\Downloads\Top_8_Shotput', index=False, header=True)


# In[22]:


#creating csv files for top 8 finisishers - Discus
top_8_Discus = df18.head(8)
top_8_Discus.to_csv(r'C:\Users\marit\Downloads\Top_8_Discus', index=False, header=True)


# In[23]:


#creating csv files for top 8 finisishers - Hammer Throw
top_8_Hammer = df19.head(8)
top_8_Hammer.to_csv(r'C:\Users\marit\Downloads\Top_8_Hammer', index=False, header=True)


# In[24]:


#creating csv files for top 8 finisishers - Javelin
top_8_Javelin = df20.head(8)
top_8_Javelin.to_csv(r'C:\Users\marit\Downloads\Top_8_Javelin', index=False, header=True)


# In[25]:


#creating csv files for top 8 finisishers - Decathlon
top_8_Decathlon = df21.head(8)
top_8_Decathlon.to_csv(r'C:\Users\marit\Downloads\Top_8_Decathlon', index=False, header=True)


# In[ ]:




