#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=(1,)
a


# In[2]:


type(a)


# In[3]:


a=('hell','hai',[10,20,30],'@!#%^',True,1)
a


# In[4]:


a[2][1]


# In[5]:


a[2][1]=80


# In[6]:


a


# In[7]:


a[2]='uj'


# In[8]:


a[2]


# In[9]:


a[0]


# In[10]:


b=[[200,[45,[True,[1]]]]]
b


# In[11]:


b[0][1][1][1][0]


# In[12]:


b[-1][-1][-1][-1]


# In[13]:


b[-1][-1][-1][-1][-1]


# In[14]:


s=set()
s


# In[15]:


type(s)


# In[21]:


s={5,2.3,True,3+1j}
s


# In[22]:


type(s)


# In[23]:


s.add(10)


# In[24]:


s


# In[25]:


s.add(0)


# In[26]:


s


# In[27]:


s.add(False)


# In[28]:


s


# In[29]:


s.add([1,2,3])#set itself is mutable but it only aloows immutable data


# In[30]:


p={1,2,3,4,56,1,2,3}


# In[33]:


p#set doenot support dupilcate values and the order may be differnt during the output


# In[34]:


a=list((11,2,23,2))
a


# In[ ]:




