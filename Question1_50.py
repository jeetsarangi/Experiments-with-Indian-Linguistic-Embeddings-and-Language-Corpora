#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from numpy.linalg import norm
from gensim.models import Word2Vec
from gensim.models import FastText
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate


# In[2]:


def cosine_similarity(vector_1,vector_2):
    vector_1 = np.array(vector_1)
    vector_2 = np.array(vector_2)
    similarty = np.dot(vector_1,vector_2)/(np.linalg.norm(vector_1) * np.linalg.norm(vector_2))
    return similarty


# In[3]:


gloveFile=open("hi/50/glove/hi-d50-glove.txt","r",encoding = "utf8",errors = "ignore")


# In[4]:


# Glov_file = open("hi/100/glove/hi-d100-glove.txt","rb")


# In[5]:


glove_dict = {}
while True:
    line = gloveFile.readline()
    if not line:
        break
    line = line.split(" ")
    temp = line[1:]
    glove_dict[line[0]] = [float(i) for i in temp]


# In[6]:


sim_file = open("Word Similarity/hindi.txt","r",encoding = "utf8",errors = "ignore")


# In[7]:


similarity_list = []
truth = []
while True:
    line = sim_file.readline()
    if not line:
        break
    line = line.split(",")
    if len(line)<=1:
        break
    similarity_list.append([line[0],line[1]])
    truth.append(float(line[2]))
similarity_list
# file=pd.read_csv('iiith_wordsim/hindi.txt',header = None)
# file


# In[8]:


truth


# In[9]:


cbow = Word2Vec.load("hi/50/cbow/hi-d50-m2-cbow.model")


# In[10]:


skipgram = Word2Vec.load("hi/50/sg/hi-d50-m2-sg.model")


# In[11]:


fasttext = FastText.load("hi/50/fasttext/hi-d50-m2-fasttext.model")


# In[12]:


def similarity(model,data):
    res = []
    for rw in data:
        c = 0
        temp = cosine_similarity(model[rw[0]],model[rw[1]])
#         print(temp)
#         if(temp >= threshold):
#             c = 1
        res.append(temp)
    return res


# In[13]:


# def accuracy(v1,v2):
#     count = 0
#     for i in range(len(v1)):
#         if(v1[i] == v2[i]):
#             count+=1
#     return count/len(v1)


# In[14]:


def accuracy_new(v1,v2,th):
    count = 0
    res = []
    for i in range(len(v1)):
        if((v1[i] >= th and v2[i] >= th) or (v1[i] < th and v2[i] < th)):
            res.append(1)
        else:
            res.append(0)
            
    return res


# In[15]:


thresholds=[0.4,0.5,0.6,0.7,0.8,0.9]


# In[16]:


# truth = [i for i in range(len(similarity_list))]


# In[17]:


import pandas as pd


# ## Glove:

# In[18]:


# print('---------------GLOVE------------------')
# print('Threhold          Accuracy')
# for threshold in thresholds:
#     print(str(threshold)+'\t'+str(accuracy_new(truth,similarity(threshold,glove_dict,similarity_list),threshold)))


# In[20]:


print('---------------GLOVE------------------')
model_similarity = similarity(glove_dict,similarity_list)
for threshold in thresholds:
    labels = accuracy_new(truth,model_similarity,threshold)
    temp = {'word1':[r[0] for r in similarity_list],'word2':[r[0] for r in similarity_list],'Similarity Score':model_similarity,'Ground Truth similarity score':truth,'Label':labels}
    df = pd.DataFrame(temp)
    name = 'Q1_50_Glove_similarity_'+str(threshold*10)+'.csv'
    print(threshold)
    df.to_csv(name,encoding = 'utf8')


# In[ ]:


df


# ## CBow

# In[ ]:


# print('---------------CBow------------------')
# print('Threhold          Accuracy')
# for threshold in thresholds:
#     print(str(threshold)+'          '+str(accuracy(truth,find_similarity(threshold,cbow.wv,similarity_list),threshold)))


# In[21]:


print('---------------CBOW------------------')
model_similarity = similarity(cbow.wv,similarity_list)
for threshold in thresholds:
    labels = accuracy_new(truth,model_similarity,threshold)
    temp = {'word1':[r[0] for r in similarity_list],'word2':[r[0] for r in similarity_list],'Similarity Score':model_similarity,'Ground Truth similarity score':truth,'Label':labels}
    df = pd.DataFrame(temp)
    name = 'Q1_50_cbow_similarity_'+str(threshold*10)+'.csv'
    print(threshold)
    df.to_csv(name,encoding = 'utf8')


# ## FastText

# In[22]:


# print('---------------FastText------------------')
# print('Threhold          Accuracy')
# for threshold in thresholds:
#     print(str(threshold)+'          '+str(accuracy(truth,find_similarity(threshold,fasttext.wv,similarity_list),threshold)))


# In[23]:


print('---------------Fasttext------------------')
model_similarity = similarity(fasttext.wv,similarity_list)
for threshold in thresholds:
    labels = accuracy_new(truth,model_similarity,threshold)
    temp = {'word1':[r[0] for r in similarity_list],'word2':[r[0] for r in similarity_list],'Similarity Score':model_similarity,'Ground Truth similarity score':truth,'Label':labels}
    df = pd.DataFrame(temp)
    name = 'Q1_50_FASTTEXT_similarity_'+str(threshold*10)+'.csv'
    print(threshold)
    df.to_csv(name,encoding = 'utf8')


# ## SkipGram

# In[24]:


# print('---------------Skipgram------------------')
# print('Threhold          Accuracy')
# for threshold in thresholds:
#     print(str(threshold)+'          '+str(accuracy(truth,find_similarity(threshold,skipgram.wv,similarity_list),threshold)))


# In[25]:


print('---------------SkipGram------------------')
model_similarity = similarity(skipgram.wv,similarity_list)
for threshold in thresholds:
    labels = accuracy_new(truth,model_similarity,threshold)
    temp = {'word1':[r[0] for r in similarity_list],'word2':[r[0] for r in similarity_list],'Similarity Score':model_similarity,'Ground Truth similarity score':truth,'Label':labels}
    df = pd.DataFrame(temp)
    name = 'Q1_50_SkipGram_similarity_'+str(threshold*10)+'.csv'
    print(threshold)
    df.to_csv(name,encoding = 'utf8')


# In[ ]:




