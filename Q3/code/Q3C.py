#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import pickle
vowels=['अ','आ','इ','ई','उ','ऊ','ऋ','ए','ऐ','ओ','औ','अं','अः']

consonent=['क','ख','ग','घ','ङ','च','छ','ज','झ','ञ','ट','ठ','ड','ढ','ण','त','थ','द','ध',
           'न','प','फ','ब','भ','म','य','र','ल','व','श','ष','स','ह','क्ष','त्र','ज्ञ']

matra=['ा','ि','ी','ु','ू','ृ','ॄ','ॅ','ॆ','े','ै','ॉ','ॊ','ो','ौ','्']

matra_mapping={'ा':'आ','ि':'इ','ी':'ई','ु':'उ','ू':'ऊ','े':'ए','ै':'ऐ','ो':'ओ','ौ':'औ','ृ':'ऋ',
               'ॄ':'ऋऋ','ॉ':'ओ','ॅ':'ए','ं':'अं','ँ':'अं','ः':'अः','ॆ':'ए','ॊ':'ओ','्र':' ','्':'अ'}

digits=['०','१','२','३','४','५','६','७','८','९','1','2','3','4','5','6','7','8','9','0']

punctuations=['।',':',';',',','.','\'','\\','/','-','‘','’','(',')','"','|']


# In[9]:


def find_syllables(word):
    
    res = []
    word = word+" "
    s = ""
    
    for i in range(len(word)-1):
        if word[i] in vowels:
            s += word[i]
            res.append(s)
            s = ""
        elif word[i] in consonent:
            if word[i+1] in vowels+[' ']+consonent:
                s=s+word[i]+'्'+'अ'
                res.append(s)
                string=""
            elif word[i+1] in matra:
                s = s+word[i]+'्'+matra_mapping[word[i+1]]
                res.append(s)
                s=""
    return res


# In[10]:


def generate_ngrams(word_list,gram):
    temp=zip(*[word_list[i:] for i in range(0,gram)])
    ans=[' '.join(gram) for gram in temp]
    return ans


# In[11]:


def find_tot(n,path):    
    dict_count = {}
#     path = "data/small/"
    file_idx = 1
    for file_name in os.listdir(path):
        file=open(path+str(file_name),encoding='utf-8',errors = 'ignore')
        for line in file:
                for temp in digits:
                    line=line.replace(temp," ")
                for temp in punctuations:
                    line=line.replace(temp," ")
                temp=line.split()
#                 words = generate_ngrams(temp,n)
                for j in temp:
                    if(len(j) <= 0):
                        continue
                    j = find_syllables(j)
                    j = generate_ngrams(j,n)
                    
                    for i in j:
                        if(i in dict_count.keys()):
                            dict_count[i] = dict_count[i]+1
                        else:
                            dict_count[i] = 1
        file.close()
        print(file_idx)
        file_idx += 1
    res=sorted(dict_count.items(), key=lambda x: x[1], reverse=True)[:100] 
    res=[i[0] for i in res]
    return res


# In[12]:


find_tot(2,'data/small/')


# ## Unigram:

# In[13]:


r = find_tot(1,'data/small/')
with open('Q3C_unigram.pkl','wb') as f:
    pickle.dump(r, f)
r


# ## Bigram:

# In[14]:


r = find_tot(2,'data/small/')
with open('Q3C_Bigram.pkl','wb') as f:
    pickle.dump(r, f)
r


# ## Trigram:

# In[15]:


r = find_tot(3,'data/small/')
with open('Q3C_Trigram.pkl','wb') as f:
    pickle.dump(r, f)
r


# In[ ]:




