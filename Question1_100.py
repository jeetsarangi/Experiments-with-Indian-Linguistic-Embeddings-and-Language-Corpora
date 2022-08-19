#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
from numpy.linalg import norm
from gensim.models import Word2Vec
from gensim.models import FastText
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate


# In[6]:


def cosine_similarity(vector_1,vector_2):
    vector_1 = np.array(vector_1)
    vector_2 = np.array(vector_2)
    similarty = np.dot(vector_1,vector_2)/(np.linalg.norm(vector_1) * np.linalg.norm(vector_2))
    return similarty


# In[7]:


gloveFile=open("hi/100/glove/hi-d100-glove.txt","r",encoding = "utf8",errors = "ignore")


# In[8]:


# Glov_file = open("hi/100/glove/hi-d100-glove.txt","rb")


# In[9]:


glove_dict = {}
while True:
    line = gloveFile.readline()
    if not line:
        break
    line = line.split(" ")
    temp = line[1:]
    glove_dict[line[0]] = [float(i) for i in temp]


# In[15]:


sim_file = open("Word Similarity/hindi.txt","r",encoding = "utf8",errors = "ignore")


# In[16]:


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


# In[17]:


truth


# In[18]:


cbow = Word2Vec.load("hi/100/cbow/hi-d100-m2-cbow.model")


# In[19]:


skipgram = Word2Vec.load("hi/100/sg/hi-d100-m2-sg.model")


# In[20]:


fasttext = FastText.load("hi/100/fasttext/hi-d100-m2-fasttext.model")


# In[21]:


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


# In[22]:


# def accuracy(v1,v2):
#     count = 0
#     for i in range(len(v1)):
#         if(v1[i] == v2[i]):
#             count+=1
#     return count/len(v1)


# In[37]:


def accuracy_new(v1,v2,th):
    count = 0
    res = []
    for i in range(len(v1)):
        if((v1[i] >= th and v2[i] >= th) or (v1[i] < th and v2[i] < th)):
            res.append(1)
        else:
            res.append(0)
            
    return res


# In[29]:


thresholds=[0.4,0.5,0.6,0.7,0.8,0.9]


# In[30]:


# truth = [i for i in range(len(similarity_list))]


# In[32]:


import pandas as pd


# ## Glove:

# In[38]:


# print('---------------GLOVE------------------')
# print('Threhold          Accuracy')
# for threshold in thresholds:
#     print(str(threshold)+'\t'+str(accuracy_new(truth,similarity(threshold,glove_dict,similarity_list),threshold)))


# In[49]:


print('---------------GLOVE------------------')
model_similarity = similarity(glove_dict,similarity_list)
for threshold in thresholds:
    labels = accuracy_new(truth,model_similarity,threshold)
    temp = {'word1':[r[0] for r in similarity_list],'word2':[r[0] for r in similarity_list],'Similarity Score':model_similarity,'Ground Truth similarity score':truth,'Label':labels}
    df = pd.DataFrame(temp)
    name = 'Q1_100_Glove_similarity_'+str(threshold*10)+'.csv'
    print(threshold)
    df.to_csv(name,encoding = 'utf8')


# In[50]:


df


# ## CBow

# In[51]:


# print('---------------CBow------------------')
# print('Threhold          Accuracy')
# for threshold in thresholds:
#     print(str(threshold)+'          '+str(accuracy(truth,find_similarity(threshold,cbow.wv,similarity_list),threshold)))


# In[52]:


print('---------------CBOW------------------')
model_similarity = similarity(cbow.wv,similarity_list)
for threshold in thresholds:
    labels = accuracy_new(truth,model_similarity,threshold)
    temp = {'word1':[r[0] for r in similarity_list],'word2':[r[0] for r in similarity_list],'Similarity Score':model_similarity,'Ground Truth similarity score':truth,'Label':labels}
    df = pd.DataFrame(temp)
    name = 'Q1_100_cbow_similarity_'+str(threshold*10)+'.csv'
    print(threshold)
    df.to_csv(name,encoding = 'utf8')


# ## FastText

# In[53]:


# print('---------------FastText------------------')
# print('Threhold          Accuracy')
# for threshold in thresholds:
#     print(str(threshold)+'          '+str(accuracy(truth,find_similarity(threshold,fasttext.wv,similarity_list),threshold)))


# In[54]:


print('---------------Fasttext------------------')
model_similarity = similarity(fasttext.wv,similarity_list)
for threshold in thresholds:
    labels = accuracy_new(truth,model_similarity,threshold)
    temp = {'word1':[r[0] for r in similarity_list],'word2':[r[0] for r in similarity_list],'Similarity Score':model_similarity,'Ground Truth similarity score':truth,'Label':labels}
    df = pd.DataFrame(temp)
    name = 'Q1_100_FASTTEXT_similarity_'+str(threshold*10)+'.csv'
    print(threshold)
    df.to_csv(name,encoding = 'utf8')


# ## SkipGram

# In[55]:


# print('---------------Skipgram------------------')
# print('Threhold          Accuracy')
# for threshold in thresholds:
#     print(str(threshold)+'          '+str(accuracy(truth,find_similarity(threshold,skipgram.wv,similarity_list),threshold)))


# In[56]:


print('---------------SkipGram------------------')
model_similarity = similarity(skipgram.wv,similarity_list)
for threshold in thresholds:
    labels = accuracy_new(truth,model_similarity,threshold)
    temp = {'word1':[r[0] for r in similarity_list],'word2':[r[0] for r in similarity_list],'Similarity Score':model_similarity,'Ground Truth similarity score':truth,'Label':labels}
    df = pd.DataFrame(temp)
    name = 'Q1_100_SkipGram_similarity_'+str(threshold*10)+'.csv'
    print(threshold)
    df.to_csv(name,encoding = 'utf8')

