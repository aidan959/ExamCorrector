def splitstring(thestring):
    arr = thestring.split(",")
    returns =[]
    for i in arr:
        
        returns.append(",".join(i))
    return returns
while True:
    for i in splitstring(input()):
        print (i)