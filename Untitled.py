#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os


# In[2]:


df= pd.read_excel(r'Compiled posts data JAN-AUG 2020.xlsx')


# In[3]:


df


# In[4]:


import matplotlib.pyplot as pt


# In[5]:


data= df.iloc[:, 7:] 


# In[6]:


data


# In[7]:


pt.pcolor(data)
pt.show()


# In[8]:


corr= data.corr()
corr.style.background_gradient(cmap='coolwarm')


# In[9]:


df.describe()


# In[10]:


import pandas_profiling


# In[11]:


df.profile_report()


# In[12]:


df['Posted']


# In[13]:


new_df = pd.read_excel(r'Compiled posts data JAN-AUG 2020.xlsx','Lifetime Talking About This(...')


# In[14]:


new_df


# In[15]:


#bb= new_df['Posted'][0]


# In[16]:


#bb.minute


# In[17]:


# from datetime import datetime

# def time_chamge(aa):
    
#     datetime_object = datetime.strptime(aa, "%m-%d-%Y:%M%p")
#     return datetime_object


# In[18]:


# c =6


# In[19]:


minute=[]
hour=[]
month=[]
year=[]
quater=[]
for i in new_df['Posted']:
    c= i.hour
    minute.append(i.minute)
    hour.append(c)
    month.append(i.month)
    year.append(i.year)
    if 0 <= c <= 6:
        quater.append('1')
    elif 7<= c <= 12:
        quater.append('2')
    elif 12 <= c <= 18:
        quater.append('3')
    else:
        quater.append('4')
    


# In[20]:


new_df['Month']= month
new_df['Year'] = year
new_df['min']= minute
new_df['hour']=hour
new_df['Quater'] = quater


# In[21]:


quater_1= new_df.groupby(['Month','Year','Quater'])['like'].agg(lambda x : x.sum()).reset_index()


# In[22]:


new_column=[]
for i,j in zip(quater_1['Month'],quater_1['Quater']):
    c= str(i)+'_'+str(j)
    new_column.append(c)
    


# In[23]:


quater_1['Month_quater'] = new_column


# In[24]:


import matplotlib.pyplot as plt  
  
fig = plt.figure(figsize = (10, 5)) 
  
# creating the bar plot 
plt.bar(quater_1['Month_quater'], quater_1['like'], color ='maroon',  
        width = 0.4) 
  


# In[25]:


plt.pie(quater_1['like'], labels=quater_1['Month_quater'])
plt.show() 


# In[26]:


aa = new_df[(new_df['Quater'] == '1')]


# In[27]:


count_like =[]
for i in aa['like'].values:
    if i>=1.0:
        count_like.append(int(i))
    


# In[28]:


sum(count_like)


# In[29]:


from sklearn.feature_extraction.text import TfidfVectorizer


# In[30]:


#vect = TfidfVectorizer(sublinear_tf=True, max_df=0.5, analyzer='word',stop_words='english', vocabulary=vocabulary)
iff_lst =[]
for i in df['Post Message']:
    i = str(i)
    vocabulary = i.lower().split()
    vect = TfidfVectorizer(sublinear_tf=True, max_df=0.5, analyzer='word',stop_words='english', vocabulary=vocabulary)
    iff_lst.append(vect)
    
    


# In[31]:


cv= TfidfVectorizer(stop_words ='english')


# In[32]:


ff = new_df['Post Message'].dropna()


# In[33]:


len(ff)


# In[34]:


cv.fit(ff)


# In[35]:


cv.get_params()


# In[36]:


cv.get_feature_names()


# In[126]:


new_df['like']= new_df['like'].fillna(new_df['like'].mean())


# In[ ]:


new_df[]

