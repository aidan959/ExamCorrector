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
                        filelines.append(line)
                        lines_and_classifiers[currentclassifier] = filelines

        return lines_and_classifiers
#Am now using mySQL
"""def read_answer(name):
    Opens answers from the students.
    # Temporary Variables
    one_shot = False
    file_obj = open(name, "r")
    current_question = ""
    lines_and_question = {}
    question_list = []
    filelines = []
    with file_obj as f:
        for line in f:
            line = line.replace("\n", "")
            # Checks if is classifier
            if "[" and "]" in line or one_shot is False:
                one_shot = True
                line = line.replace("[", "")
                line = line.replace("]", "")
                question_list.append(line)
                current_question = line

                filelines = []
            else:
                if line != "":
                    filelines.append(line)
                    lines_and_question[current_question] = filelines

        return lines_and_question"""
def get_students():
    databaseconnection = MySQLdb.connect(host="localhost",  # your host
                                         user="examiner",       # username
                                         passwd="aidan",     # password
                                         db="examcorrector")   # name of the database
    cursor = databaseconnection.cursor()
    examnumbers=[]
    cursor.execute("SELECT exam_number FROM students")
    for row in cursor.fetchall():
       print row
def read_answers(exam_number):
    """Function to read from database"""
    get_students()
    databaseconnection = MySQLdb.connect(host="localhost",  # your host
                                         user="examiner",       # username
                                         passwd="aidan",     # password
                                         db="examcorrector")   # name of the database
    cursor = databaseconnection.cursor()

    cursor.execute("SELECT answers FROM students WHERE exam_number = " + str(exam_number))
    for row in cursor.fetchall():
        answers = row[0].split("//")
    return answers

print read_answers(123456)
