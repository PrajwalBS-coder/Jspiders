#!/usr/bin/env python
# coding: utf-8

# In[2]:


n=2
for l in range(n):
    print('*'*3)


# In[7]:


n=4
for l in range(n):
    print('*'*n)


# In[8]:


n=5
for l in range(n):
    print('*'*l)


# In[9]:


n=4
for l in range(5,0,-1):
    print('%'*l)    


# In[19]:


n=5
space=n-1
star=1
for l in range(n):
    print( ' '*space + '*' *star)
    space-=1
    star+=1


# In[2]:


n=5
space=0
star=n
for l in range(n):
    print(f'{" "*space}{"*"*star}')
    space+=1
    star-=1


# In[6]:


print("Using my approach")
n=5
space=0
star=n
for l in range(n):
    print(' '*l+"*"*(n-l))


# In[9]:


n=7
space=n-1
star=1
for l in range(1,n+1):
    print(f'{" "*space}{"+"*star}')
    space-=1
    star+=2


# In[15]:


n=7
for l in range(-1,n+1):
    print(f'{" "*(n-l)}{"+"*(l+2)}')


# In[20]:


n=7
space=0
star=(2*n)-1
for l in range(n):
    print(f'{" "*space}{"+"*star}')
    space+=1
    star-=2


# In[35]:


n=8
space=0
star=(2*n)-1
for l in range(n):
    print(f'{" "*l} {"+"*(n-l)}')


# In[30]:


n=7
space=n//2
star=1
for l in range((n//2+1)):
    print(f'{" "*space}{"+"*star}')
    space-=1
    star+=2
space=1
star=n-2
for l in range((n//2+1)):
    print(f'{" "*space}{"+"*star}')
    space+=1
    star-=2


# In[31]:


n=7
space=0
star=n
for l in range((n//2+1)):
    print(f'{" "*space}{"+"*star}')
    space+=1
    star-=2
space=1
star=n-2
for l in range((n//2)):
    print(f'{" "*space}{"+"*star}')
    space-=1
    star+=2


# In[34]:


n=7
space=n//2
star=1
num=1
for l in range((n//2+1)):
    print(f'{" "*space}{str(num)*star}')
    space-=1
    star+=2
    num+=1
space=1
star=n-2
for l in range((n//2+1)):
    print(f'{" "*space}{str(num)*star}')
    space+=1
    star-=2
    num+=1


# In[ ]:




