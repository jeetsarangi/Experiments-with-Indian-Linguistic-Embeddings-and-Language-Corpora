#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[2]:


def generate_ngrams(word_list,gram):
    temp=zip(*[word_list[i:] for i in range(0,gram)])
    ans=[' '.join(gram) for gram in temp]
    return ans


# In[3]:


# def make_bigrams(word_list):
#     bigrams = []
#     if(len(word_list) < 2):
#         return bigrams
#     temp = word_list[0]
#     for i in range(1,len(word_list)):
#         temp = temp+word_list[i]
#         bigrams.append(temp)
#         temp = word_list[i]
#     return bigrams


# In[4]:


# def make_trigrams(word_list):
#     trigrams = []
#     if(len(word_list) < 3):
#         return trigrams
#     temp = word_list[0]+word_list[1]
#     for i in range(2,len(word_list)):
#         temp = temp+word_list[i]
#         bigrams.append(temp)
#         temp = word_list[i-1]+word_list[i]
#     return trigrams


# In[5]:


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
                words = generate_ngrams(temp,n)
                for i in words:
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


# ## Unigrams:

# In[6]:


r = find_tot(1,'data/small/')
with open('Q3B_unigram.pkl','wb') as f:
    pickle.dump(r, f)


# In[7]:


r


# ## Bigram:

# In[8]:


r = find_tot(2,'data/small/')
with open('Q3B_bigram.pkl','wb') as f:
    pickle.dump(r, f)
r


# ## Trigram:

# In[9]:


r = find_tot(3,'data/small/')
with open('Q3B_trigram.pkl','wb') as f:
    pickle.dump(r, f)
r


# In[ ]:




