#!/usr/bin/env python
# coding: utf-8

# In[40]:


import pandas as pd


# In[41]:


df=pd.read_csv("student_info.csv")


# In[42]:


df.head()


# In[43]:


x=df[['study_hours']]


# In[44]:


x


# In[45]:


x.isnull().sum()


# In[46]:


x['study_hours']=x['study_hours'].fillna(x['study_hours'].mean())


# In[47]:


x.isnull().sum()


# In[48]:


y=df[['student_marks']]


# In[49]:


from sklearn.linear_model import LinearRegression


# In[50]:


from sklearn import linear_model


# In[51]:


reg=linear_model.LinearRegression()


# 

# reg.fit(x,y)

# In[52]:


reg.fit(x,y)


# In[53]:


reg.coef_


# In[54]:


reg.intercept_


# In[55]:


import matplotlib.pyplot as plt


# In[56]:


plt.scatter(x,y)
plt.plot(x,x*reg.coef_+reg.intercept_,color='red')
plt.show()


# In[57]:


reg.predict(pd.DataFrame([[6.83]],columns=['study_hours']))


# In[58]:


df['study_hours']=x['study_hours'].fillna(df['study_hours'].mean())


# In[59]:


df.head()


# In[60]:


import numpy as np


# In[61]:


hours=[6,6.5,7,8,10,16,24,7,8,4]


# In[62]:


hours=pd.DataFrame([6, 6.5, 7, 8, 10, 16, 24, 7, 8, 4])


# In[63]:


new_df=pd.DataFrame(reg.predict(hours))


# In[64]:


df.head()


# In[65]:


print(new_df)


# In[66]:


pred=reg.predict(new_df)
pred=min(pred[0],100)


# In[67]:


pred


# In[68]:


new_df=pd.DataFrame(reg.predict(hours),columns=['hours'])


# In[69]:


new_df


# In[70]:


new_df


# In[ ]:


new_df.to_csv('predicted.csv')


# In[ ]:


reg.predict([[10]])


# In[78]:


import pickle


# In[80]:


pickle.dump(reg, open("ml_model.pkl", "wb"))


# In[85]:


def marks_predict(hours):
    return reg.predict([[hours]])


# In[82]:


reg.predict([[10]])


# In[86]:


print(marks_predict(10))


# In[ ]:




