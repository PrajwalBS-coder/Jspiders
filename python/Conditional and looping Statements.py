#!/usr/bin/env python
# coding: utf-8

# In[1]:


var=100
if var:
    print("hell")


# In[3]:


var=100
if not var:
    print("hell")
else:
    print("NOt hell")


# In[6]:


var=100
if not var:
    print("hell")
elif var==100:
    print("Hell")


# In[7]:


a=10
b=29
c=30
if(a>b):
    if(a>c):
        print(f'{a} is greater')
    else:
        print(f'{c} is greater')
else:
    if b>c:
        print(f'{b} is greater')
    else:
        print(f'{c} is greater')


# In[11]:


a=100000
b=229
c=3000
print("Using and in condition")
if(a>b)and(a>c):
        print(f'{a} is greater')
elif b>c:
    print(f'{b} is greater')
else:
        print(f'{c} is greater')


# In[13]:


print("loops only applicable to collection data types")

s='amin is legend'#string
for i in s:
    print(i)


# In[14]:


l=[1,2,3,4,5]
for i in l:
    print(i)


# In[15]:


l=(1,2,3,4,5)
for i in l:
    print(i)


# In[16]:


l={1,2,3,4,5}
for i in l:
    print(i)


# In[19]:


l={1:2,3:4,5:0}
for i in l:
    print(i)


# In[ ]:




