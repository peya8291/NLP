#!/usr/bin/env python
# coding: utf-8

# In[2]:


from collections import Counter
from collections import defaultdict
import numpy as np
import math


# In[3]:


text = open("hobbit-train.txt",'r',encoding='utf-8')
text=text.read()


# In[4]:


len(text)


# In[5]:


words = text.split()
len(words)


# In[6]:


rawfreqs = Counter(words)
#print(rawfreqs)


# In[7]:


#rawfreqs.items()


# In[8]:


word2index = defaultdict(lambda: len(word2index))
print(word2index)


# In[9]:


word2index["<UNK>"]


# In[10]:


[word2index[word] for word, freq in rawfreqs.items() if freq > 1]


# In[11]:


print(len(word2index))


# In[12]:


word2index = defaultdict(lambda: 0, word2index)


# In[13]:


trigrams = [ (word2index[words[i-2]],word2index[words[i-1]], word2index[words[i]]) for i in range(2, len(words)) ]


# In[30]:


#print(trigrams)


# In[15]:


trigramFreqs = Counter(trigrams)


# In[32]:


#print(trigramFreqs)


# In[16]:


print(len(trigramFreqs))


# In[17]:


bigrams = [(word2index[words[i-1]], word2index[words[i]]) for i in range(1, len(words)) ]


# In[18]:


bigramFreqs = Counter(bigrams)
print(len(bigramFreqs))


# In[19]:


#compute unograms
unigrams = [word2index[word] for word in words]
unigramFreqs = Counter(unigrams)
print(len(unigramFreqs))


# In[20]:


def unigramProb(unigram): 
    return np.log((unigramFreqs[unigram]+1)/(sum(unigramFreqs.values())+len(unigramFreqs)))


# In[21]:


def bigramProb(bigram):
    return np.log((bigramFreqs[bigram]+1)/(unigramFreqs[bigram[0]]+len(unigramFreqs)))


# In[22]:


def trigramProb(trigram):
    return (trigramFreqs[trigram]+1)/(bigramFreqs[(trigram[0],trigram[1])]+len(unigramFreqs))


# In[49]:


def trigramSentenceProb(words):   
    return sum(np.log([trigramProb((word2index[words[i-2]],word2index[words[i-1]], word2index[words[i]])) for i in range(2, len(words))]))


# In[70]:


def trigram_sentence_prob(words):
    return unigramProb(word2index[words[0]])+bigramProb((word2index[words[0]],word2index[words[1]]))+trigramSentenceProb(words)


# In[71]:


def trigram_sentence_ppl(words):
    return np.exp(-trigram_sentence_prob(words)/len(words))


# In[66]:


test1="In a hole in the ground"
sentence = test1.split()
#newTrigramSentenceProb = unigramProb(word2index[sentence[0]])+bigramProb((word2index[sentence[0]],word2index[sentence[1]]))+trigramSentenceProb(sentence)


# In[75]:


trigram_sentence_prob(sentence)


# In[68]:


#trigram_sentence_ppl= np.exp((-newTrigramSentenceProb)/len(sentence))


# In[74]:


trigram_sentence_ppl(sentence)


# In[114]:


test = open("hw-test.txt",'r',encoding='utf-8')
test=test.read()
#print(test)


# In[115]:


test = test.split('\n')
#print(test)


# In[116]:


output_file = open('Yan-Peng-test.txt','w')
#test_words=test.split()


# In[117]:


[output_file.write(str(trigram_sentence_ppl(test_words.split()))+'\n')for test_words in test]


# In[ ]:





# In[ ]:




