#!/usr/bin/env python
# coding: utf-8

# In[66]:


n=input()
rn=n[::-1]
rn=int(rn)
print(rn)
n=int(n)
if n==rn:
    print("Palindrome")
else:
    print("Not Palindrome")


# In[23]:


n=int(input())
k=n
num=0
while(n>0):
    #print("en")
    r=n%10
    num=num*10+r
    n=n//10
print(num)
#print(type(n),type(num))
#print(n)
if k==num:
    print("Palindrome")
else:
    print("Not Palindrome")


# In[29]:


n=153
print(len(str(n)))


# In[67]:


n=int(input())
k=n
l=len(str(n))
sum=0
while(n>0):
    #print("en")
    r=n%10
    sum=sum+r**l
    n=n//10
print(sum)
if k==sum:
    print("Armstrong number")
else:
    print("Not Armstong Number")


# In[37]:


n=int(input())
k=n
l=len(str(n))
sum=0
while(n>0):
    #print("en")
    r=n%10
    sum=sum+r**l
    n=int(n/10)
print(sum)
if k==sum:
    print("Armstrong number")
else:
    print("Not Armstong Number")


# In[70]:


n=int(input())
k=n
num=0
c,j=0,0
while(n>0):
    #print("en")
    r=n%10
    num=num*10+r
    n=n//10
print(num)
if k!=num:
    for r in range(1,k+1):
        if(k%r==0):
            c+=1
    if c>2:
        print("Not EMIRP")
    else:
        for r in range(1,num+1):
            if(num%r==0):
                j+=1
        if(j>2):
            print("Not EMIRP")
        else:
            print("EMIRP")

else:
    print("Notttt EMIRP")
        


# In[73]:


n=int(input())
k=n
num=0
j=0
while(n>0):
    #print("en")
    r=n%10
    num=num*10+r
    n=n//10
print(num)
if k==num:
    for r in range(1,num):
        if(k%r==0):
            j+=1
    if(j>2):
        print("Not Palindromic prime")
    else:
        print("Palindromic prime")    


# In[ ]:





# In[ ]:




