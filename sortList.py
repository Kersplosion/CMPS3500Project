#Course: CMPS3500
#CLASS Project
#Date: 2021-11-06
#Student 1: Tiara Smith
#Student 2: Tristan Bock
#sortList.py

# a function to sort a list in ascending order (merge sort)
def sortL(value):
    if len(value) > 1:
        # finding the mid of the array
        mid = len(value)//2
        # dividing the array elements
        L = value[:mid]
        R = value[mid:]
        # sort the first half
        sortL(L)
        # sort the second half
        sortL(R)
        i = 0
        j = 0
        k = 0
        # copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                value[k] = L[i]
                i+=1
            else:
                value[k] = R[j]
                j+=1
            k+=1
        while i < len(L):
            value[k] = L[i]
            i+= 1
            k+=1
        while j < len(R):
            value[k] = R[j]
            j+=1
            k+=1
    return(value)

def ReverseSort(value):
    if len(value) > 1:
        # finding the mid of the array
        mid = len(value)//2
        # dividing the array elements
        L = value[:mid]
        R = value[mid:]
        # sort the first half
        ReverseSort(L)
        # sort the second half
        ReverseSort(R)
        i = 0
        j = 0
        k = 0
        # copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                value[k] = L[i]
                i+=1
            else:
                value[k] = R[j]
                j+=1
            k+=1
        while i < len(L):
            value[k] = L[i]
            i+= 1
            k+=1
        while j < len(R):
            value[k] = R[j]
            j+=1
            k+=1
    return(value)