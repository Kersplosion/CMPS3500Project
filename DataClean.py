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
    toDelete = []
    for row in range(1, len(valueArray)): #Skip the first line because it's the header and contains labels.
        flag = False
        for item in valueArray[row]:
            if item == '': #if a row has a missing column entry
                flag = True
        s = set(valueArray[row])
        if len(s) != len(valueArray[row]): #if a row has a duplicate entry
            flag = True
        if flag:
            toDelete.append(row) #collect all rows flagged for deletion into an index list.
    toDelete.sort(reverse = True)
    for row in toDelete:
        valueArray.pop(row) #We pop rows that qualify from the bottom up so we avoid range errors.

    return valueArray

def colClean(valueArray):
    toDeleteSet = {}
    for col in range(len(valueArray[0])):
        for row in valueArray:
            if not row[col].isnumeric():
                toDeleteSet.append(col) #if a column contains a nonnumeric string, flag for deletion

    toDelete = sorted(toDeleteSet, reverse=True) #This is now a list in descending order
    for item in toDelete:
        for row in valueArray:
            row.pop(item) #Pop from right to left to avoid range errors
    return valueArray