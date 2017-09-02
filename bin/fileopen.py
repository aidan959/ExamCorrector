#pylint: disable=invalid-name
#USED FOR OPENING AND INTERPRETING ANSWERS AS VARIABLES


#Reads the file and creates a list of classifiers(questions) and their meanings
def rFile(name):
    oneShot = False
    fileObj = open(name, "r")
    #Temporary Variables
    currentclassifier = ""
    linesnclassifiers = {}
    classifierlist = []
    filelines = []
    with fileObj as f:
        for line in f:
            line = line.replace("\n","")
            #Checks if is classifier 
            if "[" and "]" in line or oneShot is False:
                oneShot = True
                line = line.replace("[", "")
                line = line.replace("]", "")
                classifierlist.append(line)
                currentclassifier = line
                
                filelines=[]
            else:
                if line != "":
                    filelines.append(line)
                    linesnclassifiers[currentclassifier] = filelines
                
       
        return linesnclassifiers
