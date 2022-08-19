#                                  CS657 Assignment 2
## Author
Jeet Sarangi - 21111032 - jeets21@iitk.ac.in <br>


## Directory Structure:
##### Q1_outputs : This folder contains all the similarity between words for each embedding type fasttext,cbow,skipgram and glove
##### Q2 : This contains the ipynb code for fine tuning the Indic bert using given NER dataset.
##### Q3_outs : This contains top bigrams,trigrams and unigrams for the given dataset.

#### Codes:
`pkltotxt.py` : for converting pkl results to txt.<br>
`Q3a.py`,`Q3B.py`,`Q3C.py` : Used to find all bigrams,unigram and trigrams counts.<br>
`Question1_50.py` & `Question1_100.py` : Used to find all similarity between embeddings for 50 dimensions and 100 dimensions respectively.
## Link to Dataset:
Link to Dataset for NER: https://drive.google.com/drive/folders/1yWZfZVzAtDwepHS6By0zyYm2mqO2bQyq?usp=sharing <br>
Link to Dataset for language corpora : https://indicnlp.ai4bharat.org/corpora/ <br>
Link to Dataset for embeddings : https://www.cfilt.iitb.ac.in/diptesh/embeddings/monolingual/non-contextual/ <br>
## Steps to run:
1.To get Similarity run Question1_50.py,Question1_100.py.<br>
2.To get the bigram ,trigrams and Quadgrams run Q3a,Q3b,Q3c.<br>
3.For fine tuning using Indic-Bert run the .ipynb file in Q2 folder.<br>