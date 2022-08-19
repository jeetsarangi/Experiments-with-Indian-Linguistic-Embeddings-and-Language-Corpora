#!/usr/bin/env python
# coding: utf-8

# In[9]:


import os
from collections import Counter
import pickle


# In[10]:


vowels=['अ','आ','इ','ई','उ','ऊ','ऋ','ए','ऐ','ओ','औ','अं','अः']

consonant=['क','ख','ग','घ','ङ','च','छ','ज','झ','ञ','ट','ठ','ड','ढ','ण','त','थ','द','ध',
           'न','प','फ','ब','भ','म','य','र','ल','व','श','ष','स','ह','क्ष','त्र','ज्ञ']

matra=['ा','ि','ी','ु','ू','ृ','ॄ','ॅ','े','ै','ॉ','ो','ौ','ं','ः','ँ','्र']

matra_mapping={'ा':'आ','ि':'इ','ी':'ई','ु':'उ','ू':'ऊ','े':'ए','ै':'ऐ','ो':'ओ','ौ':'औ','ृ':'ऋ',
               'ॄ':'ऋ','ॉ':'ओ','ॅ':'ए','ं':'अं','ँ':'अं','ः':'अः','्र':'र्','्':'अ'}

digits=['०','१','२','३','४','५','६','७','८','९','1','2','3','4','5','6','7','8','9','0']

punctuations=['।',':',';',',','.','\'','\\','/','-','‘','’','(',')','"','|']


half_cons = [i+'्' for i in ['क','ख','ग','घ','ङ','च','छ','ज','झ','ञ','ट','ठ','ड','ढ','ण','त','थ','द','ध','न','प','फ','ब','भ','म','य','र','ल','व','श','ष','स','ह']]


# In[11]:


def sep_chars(word):
    
    res = []
    word = word+'श'
    Letters = ['्','़','अ','+']
    for i in range(len(word)-1):
        
        if (word[i] in matra) or (word[i] in vowels):
            res.append(word[i])
        elif word[i] in consonant:
            if word[i+1] in matra:
                res.append(word[i]+Letters[0])
            elif word[i+1] in [Letters[0],Letters[1]]:
                res.append(word[i]+word[i+1])
            elif word[i+1] in consonant+vowels:
                res.append(word[i]+Letters[0])
                res.append(Letters[2])
                
    return res
            


# In[32]:


j = sep_chars('कमल')
j


# In[13]:


def n_grams(lis,gram):
    temp = lis
    temp = zip(*[temp[i:] for i in range(0,gram)])
    ans=[''.join(ngram) for ngram in temp]
    return ans


# In[35]:


n_grams(j,4)


# In[36]:


def top_find(n):
    file_no = 1
    count_dict = {}
    for file_name in os.listdir("data/small"):
        file=open('data/small/'+str(file_name),encoding='utf-8',errors = 'ignore')
        for line in file:
            for temp in digits:
                line=line.replace(temp," ")
            for temp in punctuations:
                line=line.replace(temp," ")
            temp=line.split()
            for word in temp:
                chars = sep_chars(word)
                if len(chars) == 0:
                    continue
                chars = n_grams(chars,n)
                for ch in chars:
                    if ch in ['',' ']+matra:
                        continue
                    if ch in count_dict.keys():
                        count_dict[ch] = count_dict[ch]+1
                    else:
                        count_dict[ch] = 1
        file.close()
        print(file_no)
        file_no += 1
    n_gram100_chars=sorted(count_dict.items(), key=lambda x: x[1], reverse=True)[:100] 
    return n_gram100_chars


# ## Unigram:

# In[21]:


top100_uni = top_find(1)


# In[25]:


top = [i[0] for i in top100_uni]
top


# In[26]:


with open('Q3a_unigram.pkl','wb') as f:
    pickle.dump(top,f)


# ## Bigram:

# In[37]:


top100_bi = top_find(2)
top = [i[0] for i in top100_bi]
top


# In[38]:


with open('Q3a_bigram.pkl','wb') as f:
    pickle.dump(top,f)


# ## Trigram:

# In[39]:


top100_tri = top_find(3)
top = [i[0] for i in top100_tri]
top


# In[40]:


with open('Q3a_trigram.pkl','wb') as f:
    pickle.dump(top,f)


# ## Quadrigram:

# In[41]:


top100_quad = top_find(4)
top = [i[0] for i in top100_quad]
top


# In[42]:


with open('Q3a_quadgram.pkl','wb') as f:
    pickle.dump(top,f)


# In[ ]:




