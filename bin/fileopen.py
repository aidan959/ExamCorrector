#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" USED FOR OPENING AND INTERPRETING ANSWERS AS VARIABLES"""
import MySQLdb

# Reads the file and creates a list of classifiers(questions) and their meanings
def read_sample_answers(name):
    """Opens the questions and sample answers text document, and filters it by class."""
    # Temporary Variables
    one_shot = False
    file_obj = open(name, "r")
    
    currentclassifier = ""
    lines_and_classifiers = {}
    classifierlist = []
    filelines = []
    with file_obj as f:
        for line in f:
            line = line.replace("\n", "")
            # Checks if is classifier
            if "//" in line:
                pass
            else:  
                if "[" and "]" in line or one_shot is False:
                    one_shot = True
                    line = line.replace("[", "")
                    line = line.replace("]", "")
                    classifierlist.append(line)
                    currentclassifier = line

                    filelines = []
                else:
                    if line != "":
                        #print(line)
                        filelines.append(line)
                        lines_and_classifiers[currentclassifier] = filelines

        return lines_and_classifiers
def get_questions(name):
    """Opens the questions and sample answers text document, and filters it by class."""
    # Temporary Variables
    one_shot = False
    file_obj = open(name, "r")
    
    currentclassifier = ""
    lines_and_classifiers = []
    classifierlist = []
    filelines = []
    with file_obj as f:
        for line in f:
            line = line.replace("\n", "")
            # Checks if is classifier
            if "[" and "]" in line or one_shot is False:
                one_shot = True
                line = line.replace("[", "")
                line = line.replace("]", "")
                classifierlist.append(line)
                currentclassifier = line

    return classifierlist
#Am now using mySQL
# """def read_answer(name):
#     Opens answers from the students.
#     # Temporary Variables
#     one_shot = False
#     file_obj = open(name, "r")
#     current_question = ""
#     lines_and_question = {}
#     question_list = []
#     filelines = []
#     with file_obj as f:
#         for line in f:
#             line = line.replace("\n", "")
#             # Checks if is classifier
#             if "[" and "]" in line or one_shot is False:
#                 one_shot = True
#                 line = line.replace("[", "")
#                 line = line.replace("]", "")
#                 question_list.append(line)
#                 current_question = line

#                 filelines = []
#             else:
#                 if line != "":
#                     filelines.append(line)
#                     lines_and_question[current_question] = filelines

#         return lines_and_question""".decode('utf8')
def DBConnect():
    """Returns a database connection for the program to use"""
    return (MySQLdb.connect(host="stmarysys.org",  # your host
                            user="s4u155",       # username
                            passwd="devKycBu",     # password
                            db="s4u155_examcorrector"))   # name of the database)

def get_students():
    """Gets all of the student ids"""
    dc = DBConnect()
    cursor = dc.cursor()
    examnumbers = []
    cursor.execute("CALL s4u155_examcorrector.select_examnumbers();")
    for row in cursor.fetchall():
       for innerrow in row:
            examnumbers.append(innerrow)
    return examnumbers
def read_answers(exam_number):
    """
    Function to read from database
    :param l: Exam Number
    :type l: int
    """
    get_students()
    dc = DBConnect()
    cursor = dc.cursor()
    cursor.execute("call s4u155_examcorrector.select_answer_by_examnumber({0})".format(str(exam_number)))
    for row in cursor.fetchall():
        answers = row[0].split("//")
    return answers
""" SAMPPLE METHOD
for i in get_students():
    for rawr in read_answers(i):
        print rawr
for i in get_students():
    for rawr in read_answers(i):
        print rawr"""
def submit_result(exam_number, marks, marksString):
    """
    Function to read from database
    :param l: Exam Number
    :type l: int
    """
    dc = DBConnect()
    cursor = dc.cursor()
    cursor.execute("call s4u155_examcorrector.submit_results({},{},{});".format(str(exam_number), str(marks), str(marksString)))
