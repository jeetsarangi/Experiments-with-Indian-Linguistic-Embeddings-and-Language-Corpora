#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle


# In[2]:


infile = open('Q3a_unigram.pkl','rb')
file = pickle.load(infile)


# In[3]:


file


# In[4]:


with open("3a_unigrams.txt", 'w',encoding="utf-8") as output:
    for row in file:
        output.write(row + '\n')


# In[5]:


infile = open('Q3a_bigram.pkl','rb')
file = pickle.load(infile)


# In[6]:


with open("3a_bigrams.txt", 'w',encoding="utf-8") as output:
    for row in file:
        output.write(row + '\n')


# In[7]:


infile = open('Q3a_trigram.pkl','rb')
file = pickle.load(infile)

with open("3a_trigrams.txt", 'w',encoding="utf-8") as output:
    for row in file:
        output.write(row + '\n')


# In[8]:


infile = open('Q3a_quadgram.pkl','rb')
file = pickle.load(infile)

with open("3a_quadgrams.txt", 'w',encoding="utf-8") as output:
    for row in file:
        output.write(row + '\n')


# In[9]:


infile = open('Q3B_unigram.pkl','rb')
file = pickle.load(infile)
with open("3B_unigrams.txt", 'w',encoding="utf-8") as output:
    for row in file:
        output.write(row + '\n')
        


# In[10]:


infile = open('Q3B_bigram.pkl','rb')
file = pickle.load(infile)
with open("3B_bigrams.txt", 'w',encoding="utf-8") as output:
    for row in file:
        output.write(row + '\n')


# In[11]:


infile = open('Q3B_trigram.pkl','rb')
file = pickle.load(infile)
with open("3B_trigrams.txt", 'w',encoding="utf-8") as output:
    for row in file:
        output.write(row + '\n')


# In[12]:


infile = open('Q3C_Bigram.pkl','rb')
file = pickle.load(infile)
with open("3C_bigrams.txt", 'w',encoding="utf-8") as output:
    for row in file:
        output.write(row + '\n')


# In[13]:


infile = open('Q3C_Trigram.pkl','rb')
file = pickle.load(infile)
with open("3C_trigrams.txt", 'w',encoding="utf-8") as output:
    for row in file:
        output.write(row + '\n')


# In[14]:


infile = open('Q3C_unigram.pkl','rb')
file = pickle.load(infile)
with open("3C_unigrams.txt", 'w',encoding="utf-8") as output:
    for row in file:
        output.write(row + '\n')


# In[ ]:




