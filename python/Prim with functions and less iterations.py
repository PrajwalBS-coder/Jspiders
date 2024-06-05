#!/usr/bin/env python
# coding: utf-8

# In[9]:


def isprime(n):
    """
    kgfhgvity
    """
    c=0
    for var in range(1,n+1):
        if(n%var==0):
            c=c+1
            
            
    return (c==2)


var=97
if(isprime(var)):
    print("Prime")
else:
    print("Not Prime")


# In[16]:


def isprime(n):
    for fa in range(2,n//2):
        return(n//fa)


print(isprime(2))    
if(isprime(11)>=1):
    print("Prime")
else:
    print("Not Prime")


# In[ ]:




