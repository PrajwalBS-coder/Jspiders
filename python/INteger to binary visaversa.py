#!/usr/bin/env python
# coding: utf-8

# In[5]:


n=13
pos=1
num=0
while(n!=0):
    ld=n%2;
    num+=ld*pos
    n//=2
    pos*=10
print(num)


# In[10]:


n=1101
num=0
pwr=0
while(n!=0):
    ld=n%10
    num+=ld*(2**pwr)
    n//=10
    pwr+=1
num


# In[ ]:


num=22
while(num>9):
    dsum=0
    while(num!=0):
        ld=num%10
        dsum+=ld**2
        num//=10
        
    num=dsum
if num==1 or num==7:
    print("HAPPY NUMBER")
else:
    print("NOT A HAPPY NUMBER")


# In[ ]:


num=192
stnum=str(num*1)+str(num*2)+str(num*3)
print(stnum)
for val in range(1,10):
    if str(val) not in stnum:
        print("NOT A FACINATING NO")
        break
else:
    print("FACINATING NO")


# In[ ]:


var=10
n=0
while(n*(n+1))<=var:
    if (n*(n+1))==var:
        print("PRONIC NUMBER")
        break
    n+=1
else:
    print("NOT PRONIC NO")
        


# In[ ]:




