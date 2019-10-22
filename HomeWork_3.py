#!/usr/bin/env python
# coding: utf-8

# In[31]:


def getNum():
    getNum = input('Введите число n: ')
    print('n = ', getNum)
    return int(getNum)


# In[32]:


def conversN(num):
        
    numD = {}
    
    for k in range(1,num+1):
        n = k
        i = 0
        
        while k > 1:
        
            if  k % 2 == 0:
                k = k / 2
                i += 1
            else:
                k = 3 * k + 1
                i += 1
                
        numD.update({n:i})
        
    return numD


# In[33]:


def maxVal(numD):
    v=list(numD.values())
    k=list(numD.keys())
    maxD = k[v.index(max(v))]
    return (maxD, numD.get(maxD))


# In[34]:


def collatz():
    n = getNum()
    numLen = (maxVal(conversN(n)))
    print(numLen)


# In[35]:


collatz()

