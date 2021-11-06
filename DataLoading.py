#Course: CMPS3500
#CLASS Project
#Date: 2021-11-06
#Student 1: Tiara Smith
#Student 2: Tristan Bock
#Student 3: Marcos Lara
#ReadCSV.py
'''
This function accepts a CSV file and returns a 2-dimensional list
of the header and all values. If an exception is raised, it
returns to the caller with -1.
'''
def readcsv(file):
    try:
        spreadsheet = open(file)
    except BaseException:
        return -1
    else:
        values = []
        header = [elem.strip() for elem in spreadsheet.readline().split(",")]
        values.append(header)
        for lines in spreadsheet:
            values.append([item.strip() for item in lines.split(",")])
        return values