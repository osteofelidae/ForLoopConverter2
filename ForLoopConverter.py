import string

def checkVar(varIndex, strInput):
    strInput = " " + strInput + " "
    if not((strInput[varIndex]) in string.ascii_lowercase) and not((strInput[varIndex+2]) in string.ascii_lowercase):
        return True
    else:
        return False
    
def findVars(varName, strInput):
    indexList = []
    for checkIndex in range(len(strInput)):
        if checkVar(checkIndex, strInput) and (strInput[checkIndex] == varName):
            indexList.append(checkIndex)
    return indexList



inFileName = input("Input input file path... ")
outFileName = input("Input output file path...")

inFile = open(inFileName, "r+")

print(inFile.readlines)

inFile.close()