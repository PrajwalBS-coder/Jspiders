#!/usr/bin/env python
# coding: utf-8

# In[1]:


l=[3,5,2,6,7,7,88,87,5,22]
l


# In[2]:


l.reverse()


# In[3]:


l


# In[4]:


l.sort()


# In[5]:


l


# In[6]:


l.sorted()


# In[7]:


l


# In[8]:


ll=l.copy()


# In[9]:


ll


# In[12]:


print('Tuple MEthods')


# In[13]:


t=(1,4,2,44,21,0)
t


# In[15]:


sorted(t)


# In[16]:


t


# In[17]:


sorted(t,reverse=True)


# In[18]:


t.count()


# In[19]:


t.count(11)


# In[20]:


t.count(21)


# In[22]:


t.index(33)


# In[23]:


t.index(44)


# In[24]:


print("SETS INBUILT METOTDS")


# In[26]:


s={1,2,3,4,3,3,2,2,2,2,12,12,1,21,2,12,12,12,1,21,2}


# In[27]:


s#it removes all the duplicates


# In[28]:


s.add(1)


# In[29]:


s


# In[30]:


s.add(1000)


# In[31]:


s


# In[32]:


s


# In[33]:


s.add("trthvhvyu")


# In[34]:


s


# In[35]:


s.update(1)


# In[36]:


s.update('1')


# In[37]:


s


# In[38]:


s.update(1+2j)


# In[39]:


s.update(True)


# In[40]:


s=set()


# In[41]:


s


# In[42]:


s.update('123')


# In[43]:


s


# In[44]:


s.update([1,2,23])


# In[45]:


s


# In[46]:


s.update({'a':22,'b':33})


# In[47]:


s


# In[48]:


print("REMOVE methods")


# In[49]:


s


# In[50]:


s.remove()


# In[51]:


s.remove(1)


# In[52]:


s


# In[54]:


s.discard(2)


# In[55]:


s


# In[56]:


s.remove(1)


# In[57]:


s


# In[58]:


s.pop()


# In[59]:


s


# In[60]:


s.pop()


# In[61]:


s.clear()


# In[62]:


s


# In[63]:


print('set operations')


# In[2]:


a={1,2,3,4,5,6,7}
b={3,4,5,6,7,8,9,10}


# In[65]:


a b


# In[66]:


a
b


# In[67]:


print(a,b)


# In[68]:


a.union(b)


# In[69]:


b.union(b)


# In[70]:


b.union(a)


# In[71]:


a.intersection(a)


# In[72]:


a.intersection(b)


# In[73]:


a.difference(b)


# In[3]:


b.difference(a)


# In[5]:


a.difference(a)


# In[6]:


print("dictinory builtin methods")


# In[7]:


d=dict()


# In[8]:


d


# In[9]:


d['a']=10


# In[10]:


d


# In[11]:


d[(2,3,3)]=[2,3,4,4]


# In[12]:


d


# In[13]:


d.keys()


# In[15]:


d[12,3,4,4,4]=1000


# In[16]:


d


# In[17]:


a


# In[20]:


{2}.issubset(a)


# In[23]:


{23}.issubset(a)


# In[24]:


a.issuperset({2})


# In[25]:


a.issuperset({24})


# In[26]:


d


# In[27]:


d[[1,2,3]]=33


# In[28]:


d.clear()


# In[29]:


d


# In[30]:


d.update(['87'])


# In[31]:


d


# In[32]:


d.update([33,{True,False},(1,2,3,4)])


# In[33]:


d.update([33,{True,False},(1,2)])


# In[34]:


d.update(['33',{True,False},(1,2,3,4)])


# In[35]:


d.update([33,{True,False},(1,2)])


# In[36]:


d.update(['33',{True,False},(3,4)])


# In[37]:


d


# In[39]:


d.update(['11',{'1':33,'2':22}])


# In[40]:


d


# In[41]:


d.clear()


# In[44]:


d.update({'p':1,'r':2})


# In[45]:


d


# In[48]:


d.update(([7,8],{'o':1,'y':2}))


# In[49]:


d


# In[50]:


d


# In[51]:


d.pop()


# In[52]:


d.pop('a')


# In[53]:


d.pop('p')


# In[54]:


d


# In[55]:


d.pop('r')


# In[56]:


d.pop('o')


# In[57]:


d


# In[58]:


d.pop(7)


# In[59]:


d.pop('p')


# In[62]:


d={'p': 'r', 'r': 2, 7: 8, 'o': 'y'}


# In[61]:


d


# In[63]:


d


# In[64]:


d.popitem()


# In[65]:


d


# In[66]:


d.popitem()


# In[67]:


d.popitem()


# In[68]:


d.popitem()


# In[71]:


d.popitem()


# In[92]:


d={'p': 'r', 'r': 2, 7: 8, 'o': 'y'}


# In[93]:


d


# In[80]:


d.get('p')


# In[81]:


print(d.get('e'))


# In[82]:


d.get('e',200)


# In[83]:


d


# In[85]:


d.setdefault(2)


# In[86]:


d


# In[87]:


d.keys


# In[88]:


d.keys()


# In[89]:


d.values()


# In[90]:


d.items()


# In[91]:


d.clear()


# In[94]:


d


# In[95]:


s=d.copy()


# In[96]:


s


# In[97]:


s==d


# In[98]:


s is d


# In[99]:


id(s)


# In[100]:


id(d)


# In[101]:


d.formkeys()


# In[103]:


d.fromkeys('2345',89)#it'll create new memory for the output and it won't change the original dict


# In[104]:


d


# In[ ]:




