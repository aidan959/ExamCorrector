"""Main for the computer aided exam marker"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Classifies Sentences As right or wrong answers
#region imports and file setups
import sys
import json
import datetime
import time
import logging
import codecs
import numpy as np
import nltk
from nltk.stem.lancaster import LancasterStemmer
import interactions as fo
LOGGER = logging
LOGGER.basicConfig(filename='log/debug.log', level=logging.DEBUG)
try:
    EXAMCENTER = sys.argv[1]
except IndexError:
    EXAMCENTER = "all"
else:
    EXAMCENTER = "all"
finally:
    pass
try:
    QUESTIONANSWERS = fo.read_sample_answers("cspeqaa.txt")
except FileNotFoundError:
    LOGGER.warning("No file")
    sys.exit()
nltk.download('punkt')
#endregion
#region place holders
#  pylint: disable=invalid-name
# Forced Python to utilize utf-8
if sys.stdout.encoding != 'cp850':
    sys.stdout = codecs.getwriter('cp850')(sys.stdout.buffer, 'strict')
if sys.stderr.encoding != 'cp850':
    sys.stderr = codecs.getwriter('cp850')(sys.stderr.buffer, 'strict')
#endregion
#region Variable Declaration

stemmer = LancasterStemmer()
training_data = []
WORDS = []
CLASSES = []
DOCUMENTS = []
IGNORE_WORDS = ['?']
TRAINING = []
OUTPUT = []
#endregion

for key, value in list(QUESTIONANSWERS.items()):
    for sent in value:
        training_data.append({"class":key, "sentence":sent})
# 3 classes of training data
# loop through each sentence in our training data
for pattern in training_data:
    # tokenize each word in the sentence
    w = nltk.word_tokenize(pattern['sentence'])
    # add to our WORDS list
    WORDS.extend(w)
    # add to documents in our corpus
    DOCUMENTS.append((w, pattern['class']))
    # add to our classes list
    if pattern['class'] not in CLASSES:
        CLASSES.append(pattern['class'])

# stems each word, lowers their case and makes them into a list
WORDS = [stemmer.stem(w.lower()) for w in WORDS if w not in IGNORE_WORDS]
WORDS = list(set(WORDS))

# LOGS ALL INFO INSTEAD OF PRINTING TO TERMINAL
CLASSES = list(set(CLASSES))

LOGGER.info(str(len(DOCUMENTS))+ "documents")
LOGGER.info(str(len(CLASSES))+ "classes" + str(CLASSES))
LOGGER.info(str(len(WORDS)) + "unique stemmed WORDS" + str(WORDS))


# create an empty array for our output
output_empty = [0] * len(CLASSES)

# training set, bag of WORDS for each sentence
for doc in DOCUMENTS:
    # initialize our "bag" of words
    BAG = []
    # list of tokenized words for the pattern
    pattern_words = doc[0]
    # stem each word
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
    # create our bag of words array
    for w in WORDS:
        if w in pattern_words:
            BAG.append(1)
        else:
            BAG.append(0)
    TRAINING.append(BAG)
    # output is = '0' for every tag and is = 1 for the current tag
    output_row = list(output_empty)
    output_row[CLASSES.index(doc[1])] = 1
    OUTPUT.append(output_row)

# sample training/output
I = 0
W = DOCUMENTS[I][0]
# logging for the code
LOGGER.info([stemmer.stem(word.lower()) for word in W])
LOGGER.info(TRAINING[I])
LOGGER.info(OUTPUT[I])

#region neural definitions
class AnswerClassifier():
    """The neural network"""
    def __init__(self):
        self.synapse_0 = None
        self.synapse_1 = None
    @classmethod
    def sigmoid(cls, x):
        """Computes the sigmoid functions nonlinearity"""
        returns = 1/(1+np.exp(-x))
        return returns
    # convert output of sigmoid function to its derivative
    @classmethod
    def sigmoid_output_to_derivative(cls, out_put):
        """Converts the output of the sigmoid function to it's derivative"""
        return out_put*(1-out_put)
    @classmethod
    def clean_up_sentence(cls, sentence):
        """tokenize the pattern"""
        sentence_words = nltk.word_tokenize(sentence)
        # stem each word
        sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
        return sentence_words
    def bow(self, sentence, words, show_details=False):
        """return bag of words array: 0 or 1 for each word in the bag that exists in the sentence"""
        sentence_words = self.clean_up_sentence(sentence)
        # bag of words
        bag = [0]*len(words)
        for s in sentence_words:
            for i, tempw in enumerate(words):
                if tempw == s:
                    bag[i] = 1
                    if show_details:
                        LOGGER.info("found in bag: {0}".format(tempw))

        return np.array(bag)
    def think(self, sentence, show_details=False):
        """Loops through the neural net code"""
        x = self.bow(sentence.lower(), WORDS, show_details)
        if show_details:
            LOGGER.info("sentence:", sentence, "\n bow:", x)
        # input layer is our bag of words
        l0 = x
        # matrix multiplication of input and hidden layer
        l1 = self.sigmoid(np.dot(l0, self.synapse_0))
        # output layer
        l2 = self.sigmoid(np.dot(l1, self.synapse_1))
        return l2
    def train(self, x, y,
              hidden_neurons=10,
              alpha=1,
              epochs=50000,
              dropout=False,
              dropout_percent=0.5):
        """computer goes through the sampling etc"""
        LOGGER.info("Training with {0} neurons, alpha:{1}, dropout:{2} {3}".format(hidden_neurons,
                                                                                   str(alpha),
                                                                                   dropout,
                                                                                   dropout_percent
                                                                                   if dropout
                                                                                   else ''))
        LOGGER.info("Input matrix: %{0}x%{1}    Output matrix: %{2}x%{3}".format(len(x),
                                                                                 len(x[0]),
                                                                                 1,
                                                                                 len(CLASSES)))
        np.random.seed(1)

        last_mean_error = 1
        # randomly initialize our weights with mean 0
        self.synapse_0 = 2*np.random.random((len(x[0]), hidden_neurons)) - 1
        self.synapse_1 = 2*np.random.random((hidden_neurons, len(CLASSES))) - 1

        prev_synapse_0_weight_update = np.zeros_like(self.synapse_0)
        prev_synapse_1_weight_update = np.zeros_like(self.synapse_1)

        synapse_0_direction_count = np.zeros_like(self.synapse_0)
        synapse_1_direction_count = np.zeros_like(self.synapse_1)

        for j in iter(list(range(epochs+1))):

            # Feed forward through layers 0, 1, and 2
            layer_0 = x
            layer_1 = self.sigmoid(np.dot(layer_0, self.synapse_0))
            if dropout:
                layer_1 *= np.random.binomial([np.ones((len(x), hidden_neurons))],
                                              1-dropout_percent)[0] * (1.0/(1-dropout_percent))

            layer_2 = self.sigmoid(np.dot(layer_1, self.synapse_1))

            # how much did we miss the target value?
            layer_2_error = y - layer_2

            if (j% 10000) == 0 and j > 5000:
                # if this 10k iteration's error is greater than the last iteration, break out
                if np.mean(np.abs(layer_2_error)) < last_mean_error:
                    LOGGER.info("delta after "+str(j)+" iterations:"
                                + str(np.mean(np.abs(layer_2_error))))
                    last_mean_error = np.mean(np.abs(layer_2_error))
                else:
                    LOGGER.debug("break:", np.mean(np.abs(layer_2_error)), ">", last_mean_error)
                    break

            # in what direction is the target value?
            # were we really sure? if so, don't change too much.
            layer_2_delta = layer_2_error * self.sigmoid_output_to_derivative(layer_2)

            # how much did each l1 value contribute to the l2 error (according to the weights)?
            layer_1_error = layer_2_delta.dot(self.synapse_1.T)

            # in what direction is the target l1?
            # were we really sure? if so, don't change too much.
            layer_1_delta = layer_1_error * self.sigmoid_output_to_derivative(layer_1)

            synapse_1_weight_update = (layer_1.T.dot(layer_2_delta))
            synapse_0_weight_update = (layer_0.T.dot(layer_1_delta))

            if j > 0:
                synapse_0_direction_count += np.abs(((synapse_0_weight_update > 0)+0)
                                                    - ((prev_synapse_0_weight_update > 0) + 0))
                synapse_1_direction_count += np.abs(((synapse_1_weight_update > 0)+0)
                                                    - ((prev_synapse_1_weight_update > 0) + 0))
            self.synapse_1 += alpha * synapse_1_weight_update
            self.synapse_0 += alpha * synapse_0_weight_update

            prev_synapse_0_weight_update = synapse_0_weight_update
            prev_synapse_1_weight_update = synapse_1_weight_update

        now = datetime.datetime.now()

        # persist synapses
        synapse = {'synapse0': self.synapse_0.tolist(), 'synapse1': self.synapse_1.tolist(),
                   'datetime': now.strftime("%Y-%m-%d %H:%M:%S"),
                   'words': WORDS,
                   'classes': CLASSES}
        synapse_file = "synapses.json"

        with open(synapse_file, 'w') as outfile:
            json.dump(synapse, outfile, indent=4, sort_keys=True)
        LOGGER.info("saved synapses to:" + synapse_file)
    def classify(self, sentence, show_details=False):
        """Needed for correcting, where it runs the neural code and
        returns how accurate the computer thinks the students answer is."""
        results = self.think(sentence, show_details)
        results = [[i, r] for i, r in enumerate(results) if r > ERROR_THRESHOLD]
        results.sort(key=lambda x: x[1], reverse=True)
        return_results = [[CLASSES[r[0]], r[1]] for r in results]
        LOGGER.debug("{0} \n classification: {1}".format(sentence, return_results))
        return results, return_results[0][0]
#endregion
NN = AnswerClassifier()
X = np.array(TRAINING)
Y = np.array(OUTPUT)
start_time = time.time()
NN.train(X, Y, hidden_neurons=20, alpha=0.1, epochs=100000, dropout=False, dropout_percent=0.2)
elapsed_time = time.time() - start_time
LOGGER.info("processing time:" + str(elapsed_time) + "seconds")
# probability threshold
ERROR_THRESHOLD = 0.2
# load our calculated synapse values
SYNAPSE_FILE = 'synapses.json'
with open(SYNAPSE_FILE) as data_file:
    SYNAPSE = json.load(data_file)
    NN.synapse_0 = np.asarray(SYNAPSE['synapse0'])
    NN.synapse_1 = np.asarray(SYNAPSE['synapse1'])

class ExamCorrector():
    """Class to initilize the ability to correct."""
    neural_network = AnswerClassifier()
    def __init__(self, nn=NN):
        """Initialize class"""
        self.neural_network = nn
    def examnumbersplit(self, examnumbers, numofgroups=4):
        """Splits the exam numbers into equally defined groups to support multithreading"""
        pass
    def correctExam(self, students, questionids):
        """function that corrects the exams"""
        for i in students:
            answermarks = []
            totalmarks = 0
            answermarks, markedstring = self.correctStudent(i, answermarks, questionids)

            totalmarks = (len(answermarks)) * 2
            #print("Total: "+ str(totalmarks))
            #print("Marks: "+ str(sum(answermarks)))

            try:
                result = sum(answermarks)/totalmarks
            except ZeroDivisionError:
                # print("student got zero or error")
                result = 0
            else:
                result = 0
            finally:
                fo.submit_result(i, result, markedstring)
        #print("Result: "+str(result*100) + "%")

    def correctStudent(self, number, marks, answers):
        """Corrects a specific student"""
        marksString = ""
        tempi = 0
        for row in fo.read_answers(number):
            #print(row)
            #print(classify(row))
            try:
                percent, question = self.neural_network.classify(row)
                #print (percent)
                #print (question)
                #print (answers[i])
                if percent[0][1] > float(0.85) and question == answers[tempi]:
                    #print("Correct")
                    marksString += "2"
                    marks.append(2)
                elif percent[0][1] > float(0.75) and question == answers[tempi]:
                    marksString += "1"
                    #print("incorrrect")
                    marks.append(1)
                else:
                    marksString += "0"
                    marks.append(0)
                tempi += 1
            except IndexError:
                marksString += "0"
                marks.append(0)
                tempi += 1
        return marks, marksString
NEWCORRECTOR = ExamCorrector()
NEWCORRECTOR.correctExam(fo.get_students(EXAMCENTER), fo.get_questions("cspeqaa.txt"))
