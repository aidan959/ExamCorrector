""" USED FOR OPENING AND INTERPRETING ANSWERS AS VARIABLES"""

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
def read_answer(name):
    """Opens answers from the students."""
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

        return lines_and_question
