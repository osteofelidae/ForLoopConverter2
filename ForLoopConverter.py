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

def findIndentLevel(strInput):
    spaceCount = 0
    checkIndex = 0
    while strInput[checkIndex] == " ":
        spaceCount += 1
        checkIndex += 1
    indentLevel = int(spaceCount / 4)
    return indentLevel

def removeNextLine(arrayInput):
    arrayOperation = arrayInput
    for number in range(len(arrayOperation)-2):
        item = arrayOperation[number]
        arrayOperation[number] = item[0:-1]
    return arrayOperation

def removeIndent(strInput):
    indentLevel = findIndentLevel(strInput)
    if indentLevel != 0:
        strOutput = strInput[indentLevel*5-1:]
    else:
        strOutput = strInput
    return strOutput

def getVariableName(strInput):
    endIndex = strInput.index(" in ")
    strOutput = strInput[4:endIndex]
    return strOutput

def getCondition(strInput):
    startIndex = strInput.index(" in ") + 4
    strOutput = strInput[startIndex:-1]
    return strOutput

def findForItems(arrayInput, indentLevelInput):
    lineCount = 0
    arrayOutput = []
    while findIndentLevel(arrayInput[lineCount]) > indentLevelInput:
        arrayOutput.append(arrayInput[lineCount])
        lineCount += 1
    return arrayOutput

inFileName = input("Input input file path... ")
outFileName = input("Input output file path... ")

inFile = open(inFileName, "r")
outFile = open(outFileName, "w")

inFileArray = inFile.readlines()
inFileArray.append("#END OF FILE")
outFileArray = []
inFile.close()


inFileArray = removeNextLine(inFileArray)
print(inFileArray)

lineCount = 0
inFileArrayLength = len(inFileArray)

while lineCount < inFileArrayLength:
    
    line = inFileArray[lineCount]
    rawLine = removeIndent(line)
    indentLevel = findIndentLevel(line)
    
    if rawLine[:3] == "for":
        arrayCheck = inFileArray[lineCount+1:]
        forItems = findForItems(arrayCheck, indentLevel)
        
        print(arrayCheck)
        print(forItems)
        
    lineCount += 1
    inFileArrayLength = len(inFileArray)
        
        
        
        
        
        
        
        
        