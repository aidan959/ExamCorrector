#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Classifies Sentences As right or wrong answers
import interactions as fo
from nltk.stem.lancaster import LancasterStemmer
import os
import json
import glob
import datetime
import nltk
import numpy as np
import time
import logging

logger = logging
logger.basicConfig(filename='debug.log',level=logging.DEBUG)

nltk.download('punkt')
stemmer = LancasterStemmer()
"""
VARIABLE
DECLARATION
"""
training_data = []
#try:
questionsanswers = fo.read_sample_answers("cspeqaa.txt")
#except FileNotFoundError:
#    logger.warning("No file")
for key, value in list(questionsanswers.items()):
    for sent in value:
        training_data.append({"class":key, "sentence":sent})
# 3 classes of training data



words = []
classes = []
documents = []
ignore_words = ['?']
# loop through each sentence in our training data
for pattern in training_data:
    # tokenize each word in the sentence
    w = nltk.word_tokenize(pattern['sentence'])
    # add to our WORDS list
    words.extend(w)
    # add to documents in our corpus
    documents.append((w, pattern['class']))
    # add to our classes list
    if pattern['class'] not in classes:
        classes.append(pattern['class'])

# stem and lower each word and remove duplicates
words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
words = list(set(words))

# remove duplicates
classes = list(set(classes))

logger.info(str(len(documents))+ "documents")
logger.info(str(len(classes))+ "classes" + str(classes))
logger.info(str(len(words)) + "unique stemmed WORDS" + str(words))

# create our training data
training = []
output = []
# create an empty array for our output
output_empty = [0] * len(classes)

# training set, bag of WORDS for each sentence
for doc in documents:
    # initialize our bag of words
    bag = []
    # list of tokenized words for the pattern
    pattern_words = doc[0]
    # stem each word
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
    # create our bag of words array
    for w in words:
        if w in pattern_words:
            bag.append(1)
        else:
            bag.append(0)
    training.append(bag)
    # output is a '0' for each tag and '1' for current tag
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    output.append(output_row)

# sample training/output
i = 0
w = documents[i][0]
logger.info([stemmer.stem(word.lower()) for word in w])
logger.info(training[i])
logger.info(output[i])

# compute sigmoid nonlinearity
def sigmoid(x):
    returns = 1/(1+np.exp(-x))
    return returns

# convert output of sigmoid function to its derivative
def sigmoid_output_to_derivative(output):
    return output*(1-output)

def clean_up_sentence(sentence):
    """tokenize the pattern"""
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words, show_details=False):
    """tokenize the pattern"""
    sentence_words = clean_up_sentence(sentence)
    # bag of words
    bag = [0]*len(words)  
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    logger.info("found in bag: {0}".format(w))

    return(np.array(bag))

def think(sentence, show_details=False):
    x = bow(sentence.lower(), words, show_details)
    if show_details:
        logger.info("sentence:", sentence, "\n bow:", x)
    # input layer is our bag of words
    l0 = x
    # matrix multiplication of input and hidden layer
    l1 = sigmoid(np.dot(l0, synapse_0))
    # output layer
    l2 = sigmoid(np.dot(l1, synapse_1))
    return l2
def train(X, y, hidden_neurons=10, alpha=1, epochs=50000, dropout=False, dropout_percent=0.5):

    logger.info("Training with {0} neurons, alpha:{1}, dropout:{2} {3}".format(hidden_neurons,
                                                                 str(alpha),
                                                                 dropout,
                                                                 dropout_percent if dropout else ''))
    logger.info("Input matrix: %{0}x%{1}    Output matrix: %{2}x%{3}".format(len(X), len(X[0]), 1, len(classes)))
    np.random.seed(1)

    last_mean_error = 1
    # randomly initialize our weights with mean 0
    synapse_0 = 2*np.random.random((len(X[0]), hidden_neurons)) - 1
    synapse_1 = 2*np.random.random((hidden_neurons, len(classes))) - 1

    prev_synapse_0_weight_update = np.zeros_like(synapse_0)
    prev_synapse_1_weight_update = np.zeros_like(synapse_1)

    synapse_0_direction_count = np.zeros_like(synapse_0)
    synapse_1_direction_count = np.zeros_like(synapse_1)
        
    for j in iter(list(range(epochs+1))):

        # Feed forward through layers 0, 1, and 2
        layer_0 = X
        layer_1 = sigmoid(np.dot(layer_0, synapse_0))
                
        if(dropout):
            layer_1 *= np.random.binomial([np.ones((len(X),hidden_neurons))],1-dropout_percent)[0] * (1.0/(1-dropout_percent))

        layer_2 = sigmoid(np.dot(layer_1, synapse_1))

        # how much did we miss the target value?
        layer_2_error = y - layer_2

        if (j% 10000) == 0 and j > 5000:
            # if this 10k iteration's error is greater than the last iteration, break out
            if np.mean(np.abs(layer_2_error)) < last_mean_error:
                logger.info("delta after "+str(j)+" iterations:" + str(np.mean(np.abs(layer_2_error))) )
                last_mean_error = np.mean(np.abs(layer_2_error))
            else:
                logger.debug("break:", np.mean(np.abs(layer_2_error)), ">", last_mean_error )
                break
                
        # in what direction is the target value?
        # were we really sure? if so, don't change too much.
        layer_2_delta = layer_2_error * sigmoid_output_to_derivative(layer_2)

        # how much did each l1 value contribute to the l2 error (according to the weights)?
        layer_1_error = layer_2_delta.dot(synapse_1.T)

        # in what direction is the target l1?
        # were we really sure? if so, don't change too much.
        layer_1_delta = layer_1_error * sigmoid_output_to_derivative(layer_1)
        
        synapse_1_weight_update = (layer_1.T.dot(layer_2_delta))
        synapse_0_weight_update = (layer_0.T.dot(layer_1_delta))
        
        if(j > 0):
            synapse_0_direction_count += np.abs(((synapse_0_weight_update > 0)+0) - ((prev_synapse_0_weight_update > 0) + 0))
            synapse_1_direction_count += np.abs(((synapse_1_weight_update > 0)+0) - ((prev_synapse_1_weight_update > 0) + 0))        
        

        synapse_1 += alpha * synapse_1_weight_update
        synapse_0 += alpha * synapse_0_weight_update
        
        prev_synapse_0_weight_update = synapse_0_weight_update
        prev_synapse_1_weight_update = synapse_1_weight_update

    now = datetime.datetime.now()

    # persist synapses
    synapse = {'synapse0': synapse_0.tolist(), 'synapse1': synapse_1.tolist(),
               'datetime': now.strftime("%Y-%m-%\d %H:%M"),
               'words': words,
               'classes': classes
              }
    synapse_file = "synapses.json"

    with open(synapse_file, 'w') as outfile:
        json.dump(synapse, outfile, indent=4, sort_keys=True)
    logger.info ("saved synapses to:" + synapse_file)

X = np.array(training)
y = np.array(output)

start_time = time.time()

train(X, y, hidden_neurons=20, alpha=0.1, epochs=100000, dropout=False, dropout_percent=0.2)

elapsed_time = time.time() - start_time
logger.info("processing time:" + str(elapsed_time) + "seconds")


# probability threshold
ERROR_THRESHOLD = 0.2
# load our calculated synapse values
synapse_file = 'synapses.json'
with open(synapse_file) as data_file:
    synapse = json.load(data_file)
    synapse_0 = np.asarray(synapse['synapse0'])
    synapse_1 = np.asarray(synapse['synapse1'])

def classify(sentence, show_details=False):
    results = think(sentence, show_details)

    results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD ]
    results.sort(key=lambda x: x[1], reverse=True)
    return_results =[[classes[r[0]],r[1]] for r in results]
    logger.debug("{0} \n classification: {1}".format(sentence, return_results))
    return results, return_results[0][0]

def correctExam(students, questionids):
    """function that corrects the exams"""
    for i in students:
        answermarks = []
        totalmarks = 0
        answermarks, markedstring = correctStudent(i, answermarks, questionids)

        totalmarks = (len(answermarks)) * 2
        #print("Total: "+ str(totalmarks))
        #print("Marks: "+ str(sum(answermarks)))

        try:
            result = sum(answermarks)/totalmarks
        except:
         #   print("student got zero or error")
            result = 0
        fo.submit_result(i, result, markedstring)
        #print("Result: "+str(result*100) + "%")

def correctStudent(number, marks, answers):
    marksString=""
    i=0
    for row in fo.read_answers(number):
        
        #print(row)
        #print(classify(row))
        try:
            percent, question = classify(row)
            #print (percent)
            #print (question)
            #print (answers[i])
            if percent[0][1] > float(0.850) and question == answers[i]:
                #print("Correct")
                marksString += "2"
                marks.append(2)
            elif percent[0][1] > float(0.75) and question == answers[i]:
                marksString += "1"
                #print("incorrrect")
                marks.append(1)
            else:
                marksString += "0"
                marks.append(0)
            i += 1
        except IndexError:
            marksString += "0"
            marks.append(0)
            i += 1
    return marks, marksString

correctExam(fo.get_students(), fo.get_questions("cspeqaa.txt"))
