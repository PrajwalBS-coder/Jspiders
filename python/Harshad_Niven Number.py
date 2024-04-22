#!/usr/bin/env python
# coding: utf-8

# In[6]:


n=int(input())
c=n
rev=0
while(n!=0):
    rev+=(n%10)
    n//=10
print(rev)
if(c%rev==0):
    print("Harshad Number")
else:
    print("Not Harshad Number")


# In[ ]:




