#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
#import pandas as pd
import math
import csv
import random


punctuations = [',','.','-','"',"'",'(',')','?','[',']','{','}','/',':',';','\n','\t']
pronouns=["i", "me", "mine", "my", "you", "your", "yours", "we", "us", "ours"]

def hotelNegT_train_read():

    f = open('hotelNegT-train.txt','r',encoding='utf-8')
    f1 = open('negative-words.txt', 'r',encoding='utf-8')
    f1list = f1.read().splitlines()
    f2 = open('positive-words.txt','r',encoding='utf-8')
    f2list = f2.read().splitlines()
    
    for line in f:
        line = line.strip('\n')
        content = line.split('\t')
        #print(content)
        review = content[1]
        review = review.lower()
        ID = content[0]
        #print(review)
        for punct in punctuations:
            review = review.replace(punct, "")
        #print(review)
        review_split = review.split(' ')
        #print(review_split)
        neg_count = 0
        pos_count = 0
        find = 0
        pronouns_count = 0
        ex_mark = 0
        total_count = 0
        tag = 0
        for word in review_split:
            if word in f1list:
                neg_count +=1 
#         print(neg_count)
            if word in f2list:
                pos_count +=1
            if word == "no":
                find = 1
#         print(find)
            if word in pronouns:
                pronouns_count +=1
#         print(pronouns_count)
            if word.endswith(('!')):
                ex_mark = 1
#         print(ex_mark)
            total_count += 1 
            ln_total_count = (np.log(total_count))
#         print(ln_total_count)
        neg_rev = [ID, pos_count, neg_count, find, pronouns_count, ex_mark, ln_total_count, tag]
#        print(neg_rev) 
        writer.writerow({'ID':ID, 'X1': pos_count, 'X2': neg_count, 'X3': find, 'X4': pronouns_count, 'X5': ex_mark, 'X6': ln_total_count, 'Y': tag})
#       
    

# hotelNegT_train_read()

def hotelPosT_train_read():
    
    f = open('hotelPosT-train.txt','r',encoding='utf-8')
    f1 = open('negative-words.txt', 'r',encoding='utf-8')
    f1list = f1.read().splitlines()
    f2 = open('positive-words.txt','r',encoding='utf-8')
    f2list = f2.read().splitlines()
    
    for line in f:
        line = line.strip('\n')
        content = line.split('\t')
        #print(content)
        review = content[1]
        review = review.lower()
        ID = content[0]
#         print(review)
#         print(ID)
        for punct in punctuations:
            review = review.replace(punct, "")
        #print(review)
        review_split = review.split(' ')
        #print(review_split)
        neg_count = 0
        pos_count = 0
        find = 0
        pronouns_count = 0
        ex_mark = 0
        total_count = 0
        tag = 1
        for word in review_split:
            if word in f1list:
                neg_count +=1 
#         print(neg_count)
            if word in f2list:
                pos_count +=1
            if word == "no":
                find = 1
#         print(find)
            if word in pronouns:
                pronouns_count +=1
#         print(pronouns_count)
            if word.endswith(('!')):
                ex_mark = 1
#         print(ex_mark)
            total_count += 1 
            ln_total_count = (np.log(total_count))
#         print(ln_total_count)
        pos_rev = [ID, pos_count, neg_count, find, pronouns_count, ex_mark, ln_total_count, tag]
        writer.writerow({'ID':ID, 'X1': pos_count, 'X2': neg_count, 'X3': find, 'X4': pronouns_count, 'X5': ex_mark, 'X6': ln_total_count, 'Y':tag})
#        print(pos_rev)  
        
def testset_read():
    
    f = open('HW2-testset.txt','r',encoding='utf-8')
    f1 = open('negative-words.txt', 'r',encoding='utf-8')
    f1list = f1.read().splitlines()
    f2 = open('positive-words.txt','r',encoding='utf-8')
    f2list = f2.read().splitlines()
    
    for line in f:
        line = line.strip('\n')
        content = line.split('\t')
        #print(content)
        review = content[1]
        review = review.lower()
        ID = content[0]
#         print(review)
#         print(ID)
        for punct in punctuations:
            review = review.replace(punct, "")
        #print(review)
        review_split = review.split(' ')
        #print(review_split)
        neg_count = 0
        pos_count = 0
        find = 0
        pronouns_count = 0
        ex_mark = 0
        total_count = 0
        #tag = 1
        for word in review_split:
            if word in f1list:
                neg_count +=1 
#         print(neg_count)
            if word in f2list:
                pos_count +=1
            if word == "no":
                find = 1
#         print(find)
            if word in pronouns:
                pronouns_count +=1
#         print(pronouns_count)
            if word.endswith(('!')):
                ex_mark = 1
#         print(ex_mark)
            total_count += 1 
            ln_total_count = (np.log(total_count))
#         print(ln_total_count)
        pos_rev = [ID, pos_count, neg_count, find, pronouns_count, ex_mark, ln_total_count]
        writer.writerow({'ID':ID, 'X1': pos_count, 'X2': neg_count, 'X3': find, 'X4': pronouns_count, 'X5': ex_mark, 'X6': ln_total_count})
#        print(pos_rev)  

#save as CSV file

with open ('hotleTrain.csv', mode='w', newline='') as csv_file:
    fieldnames= ['ID', 'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'Y']
    writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
    writer.writeheader()
    hotelPosT_train_read()
    hotelNegT_train_read()
csv_file.close()

with open ('testset.csv', mode='w', newline='') as csv_file:
    fieldnames= ['ID', 'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'Y']
    writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
    writer.writeheader()
    testset_read()
csv_file.close()


# In[5]:


ip = open('hotleTrain.csv', 'r')
data = ip.readlines()
header, rest = data[0],data[1:]
header
rest
from random import shuffle
shuffle(rest)
#print(rest)

ip_test = open('testset.csv', 'r')
data_1 = ip_test.readlines()
header_1, rest_1 = data_1[0],data_1[1:]
#print(header_1)
#print(rest_1)


# In[6]:


def sigmoid(z):
    return 1/(1+pow(math.e,-z))

def gradient_descent(w, x, y):
    gradient=[]
    for i in x:
        gradient.append((sigmoid(np.dot(w,x))-y)*i)
    return gradient

W1=[0,0,0,0,0,0,0]
W3=[0,0,0,0,0,0,0]
learnRate = 0.1

trainingSet = rest[0:int(len(rest)*0.8)]
testSet = rest[int(len(rest)*0.8):len(rest)]
trainingSet1 = rest
testSet_1= rest_1

#print(len(trainingSet))
#print(len(testSet))

#traing part
for feature in trainingSet:
    feature = feature.split(',')
    #print(feature)
    extracted_restX = feature[1:7]
    #print(extracted_restX)
    extracted_restY = feature[7]
    #print(extracted_restY)
    result_restX = list(map(float, extracted_restX))
    result_restY = float(extracted_restY)
    #print(type(result_restY))
    #add  bias term
    result_restX.append(1)
    #print(result_restX)
    W2 = W1- learnRate * np.asarray(gradient_descent(W1,result_restX, result_restY))
    W1 = W2
    #return W1
print('Weight-training vector: ', W1)

#test part
count = 0
for feature_test in testSet:
    feature_test = feature_test.split(',')
    extracted_testX = feature_test[1:7]
    extracted_testY= feature_test[7]
    #print(extracted_testX)
    result_testX = list(map(float, extracted_testX))
    result_testY = float(extracted_testY)
    result_testX.append(1)
    #print(result_testX)
    test_result = sigmoid(np.dot(W1, result_testX))
    #print(test_result)
    #print (result_testY)
    if (test_result >= 0.5 and result_testY ==1) or (test_result < 0.5 and result_testY ==0):
        count=count+1
    #print(count)

test_check = count/(len(testSet))*100
print('The accuracy: ', test_check,'%' )

for feature1 in trainingSet1:
    feature1 = feature1.split(',')
    #print(feature)
    extracted_restX_1 = feature1[1:7]
    #print(extracted_restX)
    extracted_restY_1 = feature1[7]
    #print(extracted_restY)
    result_restX_1 = list(map(float, extracted_restX_1))
    result_restY_1 = float(extracted_restY_1)
    #print(type(result_restY))
    #add  bias term
    result_restX_1.append(1)
    #print(result_restX)
    W4 = W3- learnRate * np.asarray(gradient_descent(W3,result_restX_1, result_restY_1))
    W3 = W4
    #return W1
print('Weight-test-training vector: ', W3)

#testset part
f=open("test_result.txt", "w")      
for feature_test_1 in testSet_1:
    feature_test_1 = feature_test_1.split(',')
    extracted_testX_1 = feature_test_1[1:7]
    extracted_testY_1= feature_test_1[7]
    #print(extracted_testX_1)
    #print(type(extracted_testY_1))
    result_testX_1 = list(map(float, extracted_testX_1))
    result_testY_1 = extracted_testY_1
    result_testX_1.append(1)
    #print(result_testX_1)
    test_result_1 = sigmoid(np.dot(W3, result_testX_1))
    #print(test_result_1)
    #print (result_testY)
#     if (test_result >= 0.5 and result_testY ==1) or (test_result < 0.5 and result_testY ==0): 
    if test_result_1 >= 0.5:
        f.write(str(feature_test_1[0]) + '\tPOS\n')
    else:
        f.write(str(feature_test_1[0] + '\tNEG\n'))
f.close()
           
  


# In[ ]:





# In[ ]:




