#Course: CMPS3500
#CLASS Project
#Date: 2021-11-06
#Student 1: Tiara Smith
#Student 2: Tristan Bock
#project.py
import DataClean
import DataLoading

# checks user input to see if it is a float while searching
# user is able to enter a float when the program asks for the 
# value they want to search
def isFloat(num):
	try:
		float(num)
		return True
	except ValueError:
		return False

# checks user input to see if it is an int while searching
# user is only able to enter an Int when the program asks 
# for the column number they want to search
def isInt(num):
	try:
		int(num)
		return True
	except ValueError:
		return False



validFile = False
while(not validFile):
	# asks the user what file they want to open.
	file_name = input("\nEnter a file you want to open. \nEnter: ")
	# checks to see if it a CSV file
	# if not then ask the user to open the file again
	x = file_name.split(".")
	if("csv" not in x[len(x)-1]):
		print("Invalid file type. Must be a CSV file.")
	else:
		validFile = True
data = DataLoading.readcsv(file_name)	
data = DataClean.rowClean(data)
data = DataClean.colClean(data)

# prints out the first 10 rows to prove that it is being cleaned
print('\n')

if(len(data) < 10):
	for i in range(0,len(data)):
		print(data[i])
else:
	for i in range(0,10):
		print(data[i])
select = 1
while(select != '0'):
	select = input("\nSelect from the following options.\n1. Perform Numerical Analysis\n2. Search\n0. Quit\nEnter: ")
	if(select == '1'):
		# prints out all the row names on the same line
		print("Descriptor\t", end = "", flush = True)
		for i in range(len(data[0])):
			print(data[0][i], "\t ", end = "", flush = True)
		
		print("")
		for i in range(len(data[0]) + 1):
			print("************\t", end = "", flush = True)
		
		print("")
		print("Count\t\t", end = "", flush = True)
		# iterate columns
		for i in range(0, len(data[0])):
			count = 0
			# iterate rows
			for row in data:
				count+=1
			print(count, "\t\t", end = "", flush = True)

		print("")
		print("Unique\t\t", end = "", flush = True)
		# iterate columns
		for i in range(0, len(data[0])):
			listNums = []
			# iterate rows
			for row in data:
				# skips first entry in column since it is a header
				if (row[i] == data[0][i]):
					continue
				else:
					# appends values to the list
					listNums.append(float(row[i]))
			setNums = set(listNums)
			print(len(setNums), "\t\t", end = "", flush = True)
		
		print("")
		print("Mean\t\t", end = "", flush = True)
		# iterate columns
		listOfMeans = []
		for i in range(0, len(data[0])):
			listNums = []
			# iterate rows
			for row in data:
				# skips first entry in column since it is a header
				if (row[i] == data[0][i]):
					continue
				else:
					# appends values to the list
					listNums.append(float(row[i]))
			# calculates mean and appends to the list
			# takes the sum of each column and divides by each length
			print("%0.2f" %(sum(listNums)/len(listNums)), "\t\t", end = "", flush = True)
			listOfMeans.append((sum(listNums)/len(listNums)))

		
		print("")
		print("Median\t\t", end = "", flush = True)
		# iterate columns
		for i in range(0, len(data[0])):
			listNums = []
			# iterate rows
			for row in data:
				# skips first entry in column since it is a header
				if (row[i] == data[0][i]):
					continue
				else:
					# appends values to the list
					listNums.append(float(row[i]))
			# sorts list
			listNums.sort()
			# finds median
			print(listNums[int(len(listNums)/2)], "\t\t", end = "", flush = True)

		print("")
		print("Mode\t\t", end = "", flush = True)
		# iterate columns
		for i in range(0, len(data[0])):
			listNums = []
			# iterate rows
			for row in data:
				# skips first entry in column since it is a header
				if (row[i] == data[0][i]):
					continue
				else:
					# appends values to the list
					listNums.append(float(row[i]))
			# calculates mode
			# gets the count of every value in the dataset, prints the max count (mode)
			print(max(set(listNums), key=listNums.count), "\t\t", end = "", flush = True)
		
		listOfVariances = []
		# Calculate variance but do not print, store for calculating SD
		# iterate columns
		for i in range(0, len(data[0])):
			listTotal = 0
			count = 0
			# iterate rows
			for row in data:
				# skips first entry in column since it is a header
				if (row[i] == data[0][i]):
					continue
				else:
					# appends values to the list
					count += 1
					# calculates variance
					# variance is the average of the sum of list of values minus it's mean squared
					listTotal += (float(row[i]) - listOfMeans[i])**2
			# appends variance
			listOfVariances.append(listTotal/count)

		print("")
		print("SD\t\t", end = "", flush = True)
		for i in range(0, len(data[0])):
			# calculates standard deviation
			# SD = sqrt of variance
			print("%0.2f" %(float(listOfVariances[i]))**(1/2), "\t\t", end = "", flush = True)

		print("")
		print("Variance\t", end = "", flush = True)
		for i in range(0, len(data[0])):
			# prints variance
			print("%0.2f" %(float(listOfVariances[i])), "\t\t", end = "", flush = True)


		print("")
		print("Min\t\t", end = "", flush = True)
		# iterate columns
		for i in range(0, len(data[0])):
			listNums = []
			# iterate rows
			for row in data:
				# skips first entry in column since it is a header
				if (row[i] == data[0][i]):
					continue
				else:
					# appends values to the list
					listNums.append(float(row[i]))
			# finds min value
			print(min(listNums),"\t\t", end = "", flush = True)


		print("")
		print("P20\t\t", end = "", flush = True)
		# iterate columns
		for i in range(0, len(data[0])):
			listNums = []
			# iterate rows
			for row in data:
				# skips first entry in column since it is a header
				if (row[i] == data[0][i]):
					continue
				else:
					# appends values to the list
					listNums.append(float(row[i]))
			# finds 20th percentile
			print(listNums[int((20/100) * len(listNums))], "\t\t", end = "", flush = True)

		print("")
		print("P40\t\t", end = "", flush = True)
		# iterate columns
		for i in range(0, len(data[0])):
			listNums = []
			# iterate rows
			for row in data:
				# skips first entry in column since it is a header
				if (row[i] == data[0][i]):
					continue
				else:
					# appends values to the list
					listNums.append(float(row[i]))
			# finds 40th percentile
			print(listNums[int((40/100) * len(listNums))], "\t\t", end = "", flush = True)

		print("")
		print("P50\t\t", end = "", flush = True)
		# iterate columns
		for i in range(0, len(data[0])):
			listNums = []
			# iterate rows
			for row in data:
				# skips first entry in column since it is a header
				if (row[i] == data[0][i]):
					continue
				else:
					# appends values to the list
					listNums.append(float(row[i]))
			# finds 50th percentile
			print(listNums[int((50/100) * len(listNums))], "\t\t", end = "", flush = True)

		print("")
		print("P60\t\t", end = "", flush = True)
		# iterate columns
		for i in range(0, len(data[0])):
			listNums = []
			# iterate rows
			for row in data:
				# skips first entry in column since it is a header
				if (row[i] == data[0][i]):
					continue
				else:
					# appends values to the list
					listNums.append(float(row[i]))
			# finds 60th percentile
			print(listNums[int((60/100) * len(listNums))], "\t\t", end = "", flush = True)

		print("")
		print("P80\t\t", end = "", flush = True)
		# iterate columns
		for i in range(0, len(data[0])):
			listNums = []
			# iterate rows
			for row in data:
				# skips first entry in column since it is a header
				if (row[i] == data[0][i]):
					continue
				else:
					# appends values to the list
					listNums.append(float(row[i]))
			# finds 80th percentile
			print(listNums[int((80/100) * len(listNums))], "\t\t", end = "", flush = True)

		print("")
		print("Max\t\t", end = "", flush = True)
		# iterate columns
		for i in range(0, len(data[0])):
			listNums = []
			# iterate rows
			for row in data:
				# skips first entry in column since it is a header
				if (row[i] == data[0][i]):
					continue
				else:
					# appends values to the list
					listNums.append(float(row[i]))
			# finds max value
			print(max(listNums),"\t\t", end = "", flush = True)

					

	elif(select == '2'):

		# boolean flag to track valid input for searching the dataset
		# will be set to false if user input for column number 
		# is nonnumeric or out of range for the dataset
		isValid = False
		val = input("Input the value you want to search: ")
		while(isInt(val) == False and isFloat(val) == False):
				print("Invalid input. Please try again.")
				val = input("Input the value you want to search: ")
		while(not isValid):
			colnum = input(f"Input the column number you want to search (0-{len(data[0]) - 1}) or leave blank to search dataset: ")
			if(len(colnum) == 0):
				isValid = True
			elif(isInt(colnum) == False):
				isValid = False
				print("Invalid input. Please try again.")
			elif(int(colnum) < 0 or int(colnum) > len(data[0])):
				isValid = False
				print("Invalid input. Please try again.")
			elif(not colnum.isnumeric()):
				isValid = False
				print("Invalid input. Please try again.")
			else:
				isValid = True
		count = 0
		rcount = 0
		# keeps track of every row the value is found in
		rlist = []
		# searching dataset
		if(len(colnum) == 0):
			# iterate columns
			for i in range(0, len(data[0])):
				rcount = 0
				# iterate rows
				for row in data:
					rcount+=1
					# val found
					if(val == row[i]):
						# keeps track of the total occurences of val
						count+=1
						# appends a tuple containing row and column information
						rlist.append((rcount,data[0][i]))

			print(val, " is present ", count, " times in dataset")
			print("Details:")
			print("**********************************")
			for i in range(len(rlist)):
				print(val, " is present in ", rlist[i][1], " row ", rlist[i][0])
		# finds all occurences of val
		# searching the columns 
		else:	
			for row in data:
				# keeps track of current row
				rcount+=1
				# val found
				if(val == row[int(colnum)]):
					count+=1
					# appends current row to the list
					rlist.append(rcount)

			print(val, " is present ", count, " times in ", data[0][int(colnum)])
			print("Details:")
			print("**********************************")
			for num in rlist:
				print(val, " is present in ", data[0][int(colnum)], " row ", num)

	elif(select == '0'):
		print("Goodbye...")
	else:
		print("Invalid Selection")
