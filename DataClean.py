#Course: CMPS3500
#Class Project
#Date: 2021-11-06
#Student 1: Tiara Smith
#Student 2: Tristan Bock
#DataClean.py
'''
These functions remove rows with empty cells and rows with duplicate cells,
and remove columns with nonnumeric cells.
'''
def rowClean(valueArray):
    listOfLists = []
    listOfDeletions = []
    for row in range(1, len(valueArray)): #Skip the first line because it's the header and contains labels.
        listOfLists.append(valueArray[row])

    for i in range(len(listOfLists)):
        if ('' in listOfLists[i]):
            listOfDeletions.append(i)
        for j in range(len(listOfLists)):
            if(i == j) :
                continue
            else:
                if (listOfLists[i] == listOfLists[j]):
                    listOfDeletions.append(j)

    listOfDeletions.sort(reverse=True)
    for val in listOfDeletions:
        listOfLists.pop(val)

    valueArray = listOfLists
    return valueArray

def colClean(valueArray):
    toDeleteSet = set()
    for col in range(len(valueArray[0])):
        for row in valueArray[1:]:
            if (row[col].lstrip('-').replace('.', '', 1).isnumeric() == False):
                toDeleteSet.add(col) #if a column contains a nonnumeric string, flag for deletion

    toDelete = sorted(toDeleteSet, reverse=True) #This is now a list in descending order
    for item in toDelete:
        for row in valueArray:
            del row[item] #Pop from right to left to avoid range errors
    return valueArray

def removeEmpty(valueArray):
    return [x for x in valueArray if x != []] #Removes all empty lists from the set after cleaning.