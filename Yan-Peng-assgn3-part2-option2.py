#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import Counter
from collections import defaultdict
import numpy as np
import math
import random
import re


# In[2]:


text = open("hobbit-train.txt",'r',encoding='utf-8')
text=text.read()


# In[3]:


len(text)


# In[4]:


sentenceEnders = re.compile('[.!?]')
sentenceList = sentenceEnders.split(text)
#print(sentenceList)
#words = text.split()
#print(words)
sentenceList_s = ["<s> <s> "+ sen +" </s> " for sen in sentenceList]
text1 = ''.join(sentenceList_s)
words = text1.split()
print(words)


# In[5]:


#words = [char for char in text]


# In[6]:


rawfreqs = Counter(words)
print(rawfreqs)


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


#print(word2index)


# In[12]:


word2index = defaultdict(lambda: 0, word2index)


# In[13]:


trigrams = [ (word2index[words[i-2]],word2index[words[i-1]], word2index[words[i]]) for i in range(2, len(words)) ]


# In[14]:


#print(trigrams)


# In[15]:


trigramFreqs = Counter(trigrams)


# In[16]:


#print(trigramFreqs)


# In[17]:


print(len(trigramFreqs))


# In[18]:


bigrams = [(word2index[words[i-1]], word2index[words[i]]) for i in range(1, len(words)) ]


# In[19]:


bigramFreqs = Counter(bigrams)
print(len(bigramFreqs))


# In[20]:


#compute unograms
unigrams = [word2index[word] for word in words]
unigramFreqs = Counter(unigrams)
#print(unigramFreqs)
#print(len(unigramFreqs))


# In[21]:


def unigramProb(unigram): 
    return np.log((unigramFreqs[unigram]+1)/(sum(unigramFreqs.values())+len(unigramFreqs)))


# In[22]:


def bigramProb(bigram):
    return np.log((bigramFreqs[bigram]+1)/(unigramFreqs[bigram[0]]+len(unigramFreqs)))


# In[23]:


def trigramProb(trigram):
    return (trigramFreqs[trigram]+1)/(bigramFreqs[(trigram[0],trigram[1])]+len(unigramFreqs))


# In[24]:


def gen_sentence_triProb(trigram):
    return (trigramFreqs[trigram])/(bigramFreqs[trigram[0], trigram[1]])


# In[25]:


def trigramSentenceProb(words):   
    return sum(np.log([trigramProb((word2index[words[i-2]],word2index[words[i-1]], word2index[words[i]])) for i in range(2, len(words))]))


# In[26]:


def trigram_sentence_prob(words):
    return unigramProb(word2index[words[0]])+bigramProb((word2index[words[0]],word2index[words[1]]))+trigramSentenceProb(words)


# In[27]:


def trigram_sentence_ppl(words):
    return np.exp(-trigram_sentence_prob(words)/len(words))


# In[28]:


test1="In a hole in the ground"
sentence = test1.split()
#newTrigramSentenceProb = unigramProb(word2index[sentence[0]])+bigramProb((word2index[sentence[0]],word2index[sentence[1]]))+trigramSentenceProb(sentence)


# In[29]:


trigram_sentence_prob(sentence)


# In[30]:


#trigram_sentence_ppl= np.exp((-newTrigramSentenceProb)/len(sentence))


# In[31]:


trigram_sentence_ppl(sentence)


# In[32]:


#test = open("hw-test.txt",'r',encoding='utf-8')
#test=test.read()


# In[33]:


#test = test.split('\n')
#print(test)


# In[34]:


#output_file = open('Yan-Peng-test.txt','w')
#test_words=test.split()


# In[35]:


#[output_file.write(str(trigram_sentence_ppl(test_words.split()))+'\n')for test_words in test]


# In[36]:


def generation_sentence_tri():
    text2=[w2 for w2, f2 in unigramFreqs.items()]
    word_list = list(word2index.keys())
    gen_sentence_list =  [word2index['<s>'], word2index['<s>']]
    count=2
    
    while gen_sentence_list[count-1] != word2index['</s>']:
        gen_tri_sentence = [(gen_sentence_list[count - 2], gen_sentence_list[count - 1], w2) for w2 in text2]
        gen_tri_probs = [gen_sentence_triProb((gen_sentence_list[count - 2], gen_sentence_list[count - 1], w2)) for w2 in text2]
        gen_tri_probs_norm = [float(i) / sum(gen_tri_probs) for i in gen_tri_probs]
        gen_radom_list = np.random.choice(text2, 1, p=gen_tri_probs_norm)
        gen_sentence_list.append(gen_radom_list[0])
        count = count + 1
        #print(gen_sentence_list)
        word_list = list(word2index.keys())
    
    sentence = ''
    for w3 in gen_sentence_list:
        sentence = sentence + ' ' + word_list[w3]
    
    return sentence
    #return(gen_sentence_list)


# In[39]:


output_file=open("Yan-Peng-assgn3-part2-option21.txt", "w") 
for i in range(50):
    gen_sentence = generation_sentence_tri()
    gen_sentence = gen_sentence.split()
    result_tri_senPpl=trigram_sentence_ppl(gen_sentence)
    gen_sentence_result = ' '.join(gen_sentence)
    
    output_file.write(str(gen_sentence_result) + '\n' + str(result_tri_senPpl)+'\n')
    #print(gen_sentence_result)
    #print(result_tri_senPpl)
output_file.close()    


# In[ ]:




