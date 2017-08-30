# -*- coding: utf-8 -*-
"""
Aidan Dowling.
"""
__author__ = "Aidan Dowling"
__version__ = "1.0.1"

import sys, os

# Show warnings
def warningPrint():
    sys.stdout = open(os.devnull, 'w')
def canPrint():
    if(sys.argv[1]=="true"):
        debugPrint()
    else:
        warningPrint()
     
# Show debug commands
def debugPrint():
    sys.stdout = sys.__stdout__
#important print
def iPnt(s):
    sys.stdout = sys.__stdout__
    print(s)
    canPrint()


canPrint()
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

#Imports tensorflow with nickname tf
import tensorflow as tf

x = tf.placeholder(tf.float32, [None, 784])


#defining the
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

#defining our model
y = tf.nn.softmax(tf.matmul(x, W) + b)

y_ = tf.placeholder(tf.float32, [None, 10])

cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))