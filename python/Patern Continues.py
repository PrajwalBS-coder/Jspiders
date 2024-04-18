#!/usr/bin/env python
# coding: utf-8

# In[9]:


n=3
for l in range(n):
    for k in range(n):
        print("*",end=" ")
    print()


# In[10]:


n=5
for l in range(n):
    for k in range(l):
        print("*",end= " ")
    print()


# In[12]:


n=5
for l in range(5,0,-1):
    for k in range(l):
        print("*",end= " ")
    print()


# In[28]:


n=6
sp=n-1
st=1
for l in range(1,n+1,1):
    for s in range(sp):
        print(" ",end= " ")
    for stt in range(st):
        print("*",end=" ")
    
    sp-=1
    st+=1
    print()


# In[33]:


n=6
sp=0
st=n
for l in range(n):
    for s in range(sp):
        print(" ",end= " ")
    for stt in range(st):
        print("*",end=" ")
    
    sp+=1
    st-=1
    print()


# In[41]:


n=4
sp=0
st=(2*n)-1
for l in range(n):
    for s in range(sp):
        print(" ",end= " ")
    for stt in range(st):
        print("*",end=" ")
    
    sp+=1
    st-=2
    print()


# In[44]:


n=4
sp=n-1
st=1
for l in range(1,n+1,1):
    for s in range(sp):
        print(" ",end= " ")
    for stt in range(st):
        print("*",end=" ")
    
    sp-=1
    st+=2
    print()


# In[48]:


n=5
num=1
for l in range(1,n):
    for c in range(l):
        print(l,end=" ")
    print()


# In[50]:


n=5
num=5
for l in range(1,n+1):
    for c in range(l):
        print(num,end=" ")
    print()
    num-=1


# In[61]:


n=4
sp=n
for l in range(1,n+2):
    for i in range(sp):
        print(" ",end=" ")
    for c in range(l):
        print(l,end=" ")
    print()
    sp-=1


# In[75]:


n=5
sp=1
for l in range(n,0,-1):
    for i in range(sp):
        print(" ",end=" ")
    for c in range(l):
        print(l,end=" ")
    print()
    sp+=1


# In[69]:


n=4
sp=1
num=n
for l in range(n,0,-1):
    for i in range(sp):
        print(" ",end=" ")
    for c in range(l):
        print(num,end=" ")
    print()
    sp+=1
    num-=1


# In[86]:


var=4
for e in range(2,n+2,1):
    for val in range(1,e):
        print(val,end=" ")
    print()


# In[ ]:




