import string

def checkVar(varIndex, varName, strInput):
    varNameLength = len(varName)
    strInputProcessed = " " + strInput + " "
    strOperation = strInputProcessed[varIndex:varIndex + varNameLength + 2]
    if not(strOperation[0] in string.ascii_lowercase) and not(strOperation[-1] in string.ascii_lowercase) and strOperation[1:-1] == varName:
        return True
    else:
        return False
    
def findVars(varName, strInput):
    indexList = []
    for index in range(len(strInput)):
        if checkVar(index, varName, strInput):
            indexList.append(index)
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

def findVarName(strInput):
    endIndex = strInput.index(" in ")
    strOutput = strInput[4:endIndex]
    return strOutput

def findCondition(strInput):
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

def parseCondition(strInput):
    strOutput = str(strInput)
    codeOutput = eval(strOutput)
    return codeOutput

def deleteString(startIndex, stopIndex, strInput):
    strOutput = strInput
    strOutput = strOutput[:startIndex] + strOutput[stopIndex:]
    return strOutput

def replaceMultiple(strReplacer, strToReplace, strInput, arrayReplaceIndexes):
    lengthArrayReplace = len(arrayReplaceIndexes)
    lengthStrToReplace = len(strToReplace)
    lengthStrReplacer = len(strReplacer)
    strOutput = strInput
    for index in range(lengthArrayReplace):
        replaceIndex = arrayReplaceIndexes[index]
        strOutput = deleteString(replaceIndex, replaceIndex + lengthStrToReplace, strOutput)
        strOutput = strOutput[:replaceIndex] + strReplacer + strOutput[replaceIndex:]
        for index2 in range(lengthArrayReplace):
            arrayReplaceIndexes[index2] += lengthStrReplacer - lengthStrToReplace
    return(strOutput)



inFileName = input("Input input file path... ")
outFileName = input("Input output file path... ")

inFile = open(inFileName, "r")
outFile = open(outFileName, "w")

inFileArray = inFile.readlines()
inFileArray.append("#END OF FILE")
outFileArray = []
inFile.close()


inFileArray = removeNextLine(inFileArray)

print("File contents:")
print(inFileArray)
print("")

lineCount = 0
inFileArrayLength = len(inFileArray)

while lineCount < inFileArrayLength:
    
    line = inFileArray[lineCount]
    rawLine = removeIndent(line)
    indentLevel = findIndentLevel(line)
    
    if rawLine[:3] == "for":
        arrayCheck = inFileArray[lineCount+1:]
        forItems = findForItems(arrayCheck, indentLevel)
        forCondition = findCondition(rawLine)
        forVar = findVarName(rawLine)
        
        print("For found!")
        print("Lines to check indent:")
        print(arrayCheck)
        print("")
        print("Lines in for loop:")
        print(forItems)
        print("")
        print("Variable name to search for:")
        print(forVar)
        
        appendList = []
        
        for loopVar in parseCondition(forCondition):
            for line2 in forItems:
                operationLine = line2
                varIndexes = findVars(forVar, operationLine)
                operationLine = replaceMultiple(str(loopVar), forVar, operationLine, varIndexes)
                appendList.append(operationLine)
        
        for tempVar in range(len(forItems)):
            del inFileArray[lineCount+1]
        del inFileArray[lineCount]
            
        print(inFileArray)
        
        insertIndex = lineCount
        for line2 in appendList:
            tempLineContents = (" " * 5 * indentLevel) + line2[4:]
            inFileArray.insert(insertIndex, tempLineContents)
            insertIndex += 1
            
        print(inFileArray)
        
    lineCount += 1
    inFileArrayLength = len(inFileArray)

for line in inFileArray:
    outFile.writelines(line+"\n")

outFile.close()
        
#TODO: add checking back in the program for array inputs into for loop
#      --> maybe just find all array declarations in program and run them