#imports tensorflow and numpy as shortcuts for ease of access
import tensorflow as tf
import numpy as np
#A text Convulutional Neural Network
class TextCNN(object):
    #A CNN for text classification, using embedded layer, followed by a convolutional, max-pooling/softmax layer
    #code to run upon initialization
    def __init__(self, sequence_length, num_classes, vocab_size, embedding_size, filter_sizes, num_filters):
        #
        self.input_x=tf.placeholder(tf.int32, [None, sequence_length], name= "input_x")
        self.input_y=tf.placeholder(tf.float32, [None, num_classes], name = "input_y")
        self.dropout_keep_prob=tf.placeholder(tf.float32, name ="dropout_keep_prob")
        
