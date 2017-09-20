""" USED FOR OPENING AND INTERPRETING ANSWERS AS VARIABLES"""

# Reads the file and creates a list of classifiers(questions) and their meanings
def r_file(name):
    """Opens the questions and sample answers text document, and filters it by class."""
    one_shot = False
    file_obj = open(name, "r")
    # Temporary Variables
    currentclassifier = ""
    linesnclassifiers = {}
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

                filelines = []
            else:
                if line != "":
                    filelines.append(line)
                    linesnclassifiers[currentclassifier] = filelines

        return linesnclassifiers
