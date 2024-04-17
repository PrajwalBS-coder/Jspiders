#!/usr/bin/env python
# coding: utf-8

# In[5]:


l=[4,2,9]
for n in l:
    print(n)
    for n in l:
        print(n)
    else:
        print("Inner for loop")
else:
    print("1st loop")


# In[ ]:


n=10
while n!=21:
    print(n)
    n+=1


# In[6]:


n=0
while(n!=3):
    print(n)
    n1=7
    while(n1!=10):
        print(n1)
        n1=n1+1
    else:
        print("Inner while loop")
    n+=1
    print("##############")
else:
    print("1st while loop")


# In[8]:


s='Hello World'
for c in s:
    if(c==" "):
        break
    else:
        print(c)


# In[9]:


s='Hello World'
for c in s:
    if(c==" "):
        continue
    else:
        print(c)


# In[10]:


s='Hello World'
for c in s:
    if(c==" "):
        pass
    else:
        print(c)


# In[11]:


s='Hello World'
for c in s:
    pass
    

print(c)


# In[13]:


s='Hello World'
for c in s:
    if(c=="W"):
        pass
        
    else:
        print(c)


# In[16]:


print("DIFFERENT COPY OPERATIONS")


l=[2,678,-2,98]
a=l
print(a is l)
print(a,l)
a[1]=100
print(a,l)
print(a[0] is l[0])


# In[25]:


print("Shallow copy")
print("Using Slicing")


# In[24]:


import copy
l=[2,44,66,788]
s=l[::]
print(s,l)
print(s is l)
print(s[0] is l[0])
s[0]=10
print(s,l)
print(s[0] is l[0])


# In[26]:


print("Using Inbuilt Copy Method")


# In[27]:


l=[2,44,66,788]
s=l.copy()
print(s,l)
print(s is l)
print(s[0] is l[0])
s[0]=10
print(s,l)
print(s[0] is l[0])


# In[29]:


print("Using COPY MOULE'S COPY METHOD")


# In[30]:


import copy
l=[2,44,66,788]
s=copy.copy(l)
print(s,l)
print(s is l)
print(s[0] is l[0])
s[0]=10
print(s,l)
print(s[0] is l[0])


# In[32]:


print("DEEP COPY")


# In[35]:


from copy import deepcopy
l=[2,44,66,788]
s=deepcopy(l)
print(s,l)
print(s is l)
print(s[1] is l[1])
s[0]=10
print(s,l)
print(s[0] is l[0])


# In[36]:


print(1,2,3,4,55,)


# In[38]:


for n in range(1,11):
    print(n,end=',')


# In[41]:


for n in range(1,11):
    print(n,sep ='*')


# In[42]:


print(22,33,55,66,7,8,8,sep='*')


# In[ ]:




