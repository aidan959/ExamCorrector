#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" USED FOR OPENING AND INTERPRETING ANSWERS AS VARIABLES"""
#region imports
import configparser
import os
import sys
import MySQLdb
DBCONN = 0
#regionend

CONFIGFNAME = 'main.ini'
def create_config(cfgfile=CONFIGFNAME):
    """Creates a config for the program"""
    config = configparser.ConfigParser()
    config['Database'] = {
        "server": "sample.org",
        "sqluser": "username",
        "sqlpasswd": "sqlpassword",
        "sqlschema": "sqlschema"
    }
    with open(cfgfile, 'w') as configfile:
        config.write(configfile)
def load_config(which='db', cfgfile=CONFIGFNAME):
    """Loads the config for the database"""
    config = configparser.ConfigParser()
    config.read(cfgfile)
    if which == 'db':
        tempserver = config['Database']['server']
        tempsqluser = config['Database']['sqluser']
        tempsqlpasswd = config['Database']['sqlpasswd']
        tempsqlschema = config['Database']['sqlschema']
        return tempserver, tempsqluser, tempsqlpasswd, tempsqlschema
    else:
        return 0
if os.path.exists(CONFIGFNAME):
    DBCFG = load_config()
    SERVER = DBCFG[0]
    SQLUSER = DBCFG[1]
    SQLPASSWD = DBCFG[2]
    SQLSCHEMA = DBCFG[3]
else:
    create_config()
    sys.exit()
def read_sample_answers(name):
    """Opens the questions and sample answers text document, and filters it by class.
       Reads the file and creates a list of classifiers(questions) and their meanings"""
    one_shot = False
    file_obj = open(name, "r")
    currentclassifier = ""
    lines_and_classifiers = {}
    classifierlist = []
    filelines = []
    with file_obj as temp_f:
        for line in temp_f:
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
    #currentclassifier = ""
    #lines_and_classifiers = []
    classifierlist = []
    #filelines = []
    with file_obj as temp_f:
        for line in temp_f:
            line = line.replace("\n", "")
            # Checks if is classifier
            if "[" and "]" in line or one_shot is False:
                one_shot = True
                line = line.replace("[", "")
                line = line.replace("]", "")
                classifierlist.append(line)
                #currentclassifier = line

    return classifierlist
def db_connect(server="stmarysys.org",
               sqluser="s4u155",
               sqlpasswd="devKycBu",
               sqlschema="s4u155_examcorrector"):
    """Returns a database connection for the program to use"""
    return (MySQLdb.connect(host=server,  # your host
                            user=sqluser,       # username
                            passwd=sqlpasswd,     # password
                            db=sqlschema,
                            charset='utf8'))   # name of the database)
def get_students(examcentre):
    """Gets all of the student ids"""
    database_connection = DBCONN
    cursor = database_connection.cursor()
    examnumbers = []
    #if examcentre.lower() == "all":
    cursor.execute("CALL s4u155_examcorrector.select_examnumbers();")
    #else:
        #cursor.execute("CALL s4u155_examcorrector.select_examnumbers_on_examcentre({0});"
                     #  .format(str(examcentre)))
    for row in cursor.fetchall():
        for innerrow in row:
            examnumbers.append(innerrow)
    return examnumbers
def read_answers(exam_number, centre="all"):
    """
    Function to read from database
    :param l: Exam Number
    :type l: int
    """
    get_students(centre)
    database_connection = DBCONN
    cursor = database_connection.cursor()
    cursor.execute("call s4u155_examcorrector.select_answer_by_examnumber({0})"
                   .format(str(exam_number)))
    for row in cursor.fetchall():
        answers = row[0].split("//")
    return answers
""" SAMPLE METHOD
for i in get_students():
    for rawr in read_answers(i):
        print rawr
for i in get_students():
    for rawr in read_answers(i):
        print rawr"""
def submit_result(exam_number, marks, marks_string):
    """
    Function to read from database
    :param l: Exam Number
    :type l: int
    """
    db_conn = DBCONN
    cursor = db_conn.cursor()
    cursor.execute("call s4u155_examcorrector.submit_results({},{},{});".format(str(exam_number),
                                                                                str(marks),
                                                                                str(marks_string)))
DBCONN = db_connect(SERVER, SQLUSER, SQLPASSWD, SQLSCHEMA)
