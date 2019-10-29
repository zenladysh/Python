#!/usr/bin/env python
# coding: utf-8

# In[118]:


def anagrams():
    content = []
    with open('zaliznyak.txt', 'r') as file:
        for line in file:
            content.append(line.strip())
    sortCont = (sorted(content,key = lambda x: len(x)))
                
    #res1 = [item for item in content]
    #res2 = [len(item) for item in content]    
    #res = dict(zip(res1,res2))
    #len(sortCont
    spis = []
    finSpis = []
    n = 0
    for i in range(150):       
        spis.append([])
        j = n
        for j in range(150):
            
            for item in sortCont:
                if sorted(sortCont[j]) == sorted(item) and len(item) == i:
                            
                    spis[i].append(sortCont[j])
            n = j
                
            
                   
                   
            
    """def findAnagram(spis,k):
        anagram = []
        for j in spis[k]:        

            for i in range(len(spis[k])):   
                anagram.append([])
                if sorted(j) == sorted(spis[k][i]):

                    anagram[i].append(j)
        finAn = []
        
        for i in range(len(anagram)):
            
            if len(anagram[i]) >= 2 and anagram[i] not in finAn:
                finAn.append(anagram[i])

        return finAn
  
        
    anagrams = []    
    for i in range(2,8):
        anagrams += findAnagram(spis,i)"""
    """with open('fileout.txt', 'a') as file:
        for i in range(len(anagrams)):
            file.write(str(anagrams[i]))
            file.write('\n')"""
   
    return spis


# In[ ]:


anagrams()

