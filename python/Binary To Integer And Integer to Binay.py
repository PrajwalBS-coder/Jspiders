#!/usr/bin/env python
# coding: utf-8

# In[29]:


n = 5

bs = ''
while n > 0:
    bs= str(n % 2) + bs
    n //= 2
print(bs)


# In[30]:


n=101
num=0
l=len(str(n))
m=l
while(n!=0):
    ld=n%10
    #print(l-m)
    num=num+ld* 2**(l-m)
    
    n//=10
    m-=1
print(num)
    


# In[ ]:




