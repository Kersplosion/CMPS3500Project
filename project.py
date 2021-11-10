#Course: CMPS3500
#CLASS Project
#Date: 2021-11-06
#Student 1: Tiara Smith
#Student 2: Tristan Bock
#project.py
import csv
# asks the user what file they want to open. 
file_name = input ("Which file do you want to open? \n1.InputDataSample.csv\n2.Boston_Lyft_Uber_Data.csv\nEnter: ")
# if the file is InputDataSample.csv 
if(file_name == '1'):
	#user input for file operations
	select=""

	while(select!="0"):
		select = input("\nPlease select an option:\n 1. Perform Numerical Analysis\n 2. Search\n 0. Quit\n Enter: ")
		#Numerical Analysis
		if(select == "1"):
			with open("InputDataSample.csv", "r") as file:
				csv_reader = csv.DictReader(file, delimiter=',')
				example = list(csv_reader)

				#print(example)
				listA = []
				listB = []
				countA = 0
				countB = 0
				totalA = 0
				totalB = 0
				minA = 0
				maxA = 0
				minB = 0
				maxB = 0
				for lines in example:
					countA += 1
					totalA += int(lines['Column A'])
					# appending column A to the list A element 
					listA.append(int(lines['Column A']))
					if (countA == 1):
						#Initialize values to first in list
						minA = int(lines['Column A'])
						maxA = int(lines['Column A'])
					#Change min value if greater than current
					if (minA > int(lines['Column A'])):
						minA = int(lines['Column A'])
					#Change max value if less than current
					if (maxA < int(lines['Column A'])):
						maxA = int(lines['Column A'])
					#print(lines['Column A'])
				#sort the list
				listA.sort()

				# converts list to a set
				# if the file is InputDataSample.csv 
				setA = set(listA)

				for lines in example:
					countB += 1
					totalB += int(lines['Column B'])
					# appending column B to the list B element 
					listB.append(int(lines['Column B']))

					if (countB == 1):
						#Initialize values to first in list
						minB = int(lines['Column B'])
						maxB = int(lines['Column B'])
					#Change min value if greater than current
					if (minB > int(lines['Column B'])):
						minB = int(lines['Column B'])
					#Change max value if less than current
					if (maxB < int(lines['Column B'])):
						maxB = int(lines['Column B'])
					#print(lines['Column B'])
				#sort the list
				listB.sort()
				# converts list to a set
				# a set removes duplicate entries
				setB = set(listB)
				#to find the mean of column A and B
				meanA = totalA/countA
				meanB = totalB/countB
				totalA = 0
				totalB = 0

				# finds the variance for Column A and B
				for lines in example:
					totalA += (int(lines['Column A']) - meanA)**2
					totalB += (int(lines['Column B']) - meanB)**2

				VarianceA = totalA/countA
				VarianceB = totalB/countB

				print("Descriptor\t\tColumn A\t\tColumn B")
				print("**********\t\t********\t\t********")
				print("Count     \t\t", countA, "\t\t\t", countB)
				print("Unique    \t\t", len(setA), "\t\t\t", len(setB))
				print("Mean      \t\t", meanA, "\t\t", meanB)
				print("Median    \t\t", listA[int(countA/2)-1], "\t\t", listB[int(countB/2)-1])
				print("Mode      \t\t", max(set(listA), key=listA.count), "\t\t", max(set(listB), key = listB.count))
				print("SD        \t\t", VarianceA**(1/2), "\t", VarianceB**(1/2))
				print("Variance  \t\t", VarianceA, "\t", VarianceB) 
				print("Min       \t\t", minA, "\t\t\t", minB)
				print("P20       \t\t", listA[int((20/100) * 10000)], "\t\t", listB[int((20/100) * 10000)])
				print("P40       \t\t", listA[int((40/100) * 10000)], "\t\t", listB[int((40/100) * 10000)])
				print("P50       \t\t", listA[int((50/100) * 10000)], "\t\t", listB[int((50/100) * 10000)])
				print("P60       \t\t", listA[int((60/100) * 10000)], "\t\t", listB[int((60/100) * 10000)])
				print("P80       \t\t", listA[int((80/100) * 10000)], "\t\t", listB[int((80/100) * 10000)])
				print("Max       \t\t", maxA, "\t\t", maxB)
				#for lines in csv_reader:
				#	count = count + 1
				#	print(lines['price'])
					#print(lines['cab_type'])
		#searching
		elif(select=="2"):
			with open("InputDataSample.csv", "r") as file:
				csv_reader = csv.DictReader(file, delimiter=',')
				example = list(csv_reader)
				listA = []
				listB = []
				resultsA = []
				resultsB = []
				countA = 0
				countB = 0
				for lines in example:
					listA.append(int(lines['Column A']))
					listB.append(int(lines['Column B']))
				search = input("1. Search Column A\n2. Search Column B\n3. Search Dataset\nEnter: ")
				if (search=="1"):
					searchA = input("Enter a value to search: ")
					#assign value and search list
					for i in range(len(listA)):
						#finds a match
						if (int(searchA) == listA[i]):
							#store result with offset 2 due to csv format, increment count
							# the header takes up one row and it starts at 0
							resultsA.append(i+2)
							# total amount of times the number is present in column A
							countA+=1
					#print results
					print(searchA, "is present", countA, "times in Column A")
					print("Details:")
					print("*****************************")
					for i in range(countA):
						#iterate results
						print(searchA, "is present in Column A row", resultsA[i])
				
				elif (search=="2"):
					searchB = input("Enter a value to search: ")
					#assign value and search list
					for i in range(len(listB)):
						#finds a match
						if (int(searchB) == listB[i]):
							#store result with offset 2 due to csv format, increment count
							# the header takes up one row and it starts at 0
							resultsB.append(i+2)
							# total amount of times the number is present in column B
							countB+=1
					#print results
					print(searchB, "is present", countB, "times in Column B")
					print("Details:")
					print("*****************************")
					for i in range(countB):
						#iterate results
						print(searchB, "is present in Column B row", resultsB[i])

				elif (search == "3"):
					searchD = input("Enter a value to search: ")
					#assign value and search list
					for i in range(len(listA)):
						#finds a match
						if (int(searchD) == listA[i]):
							#store result with offset 2 due to csv format, increment count
							# the header takes up one row and it starts at 0
							resultsA.append(i+2)
							countA+=1
					#print results
					for i in range(len(listB)):
						#finds a match
						if (int(searchD) == listB[i]):
							#store result with offset 2 due to csv format, increment count
							# the header takes up one row and it starts at 0
							resultsB.append(i+2)
							countB+=1
					#print results
					print(searchD, "is present", countA+countB, "times in the dataset")
					print("Details:")
					print("*****************************")
					for i in range(countA):
						#iterate results
						print(searchD, "is present in Column A row", resultsA[i])
					for i in range(countB):
						#iterate results
						print(searchD, "is present in Column B row", resultsB[i])

				else:
					print("Invalid Input")

		#exit
		elif(select=="0"):
			print("Goodbye...")
		#bad input
		else:
			print("Invalid input\n")
# if the file is Boston_Lyft_Uber_Data.csv 
elif (file_name == '2'):
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
			spreadsheet.close()
			return values

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
			if (len(s) == 1 and len(s) != len(valueArray[row])): #if a row has all duplicate entries.
				flag = True
			if flag:
				toDelete.append(row) #collect all rows flagged for deletion into an index list.
		toDelete.sort(reverse=True)
		for row in toDelete:
			valueArray.pop(row) #We pop rows that qualify from the bottom up so we avoid range errors.

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
		
		
	data = readcsv("Boston_Lyft_Uber_Data.csv")	
	data = rowClean(data)
	data = colClean(data)
	select = 1
	while(select != '0'):
		select = input("\nSelect from the following options.\n1. Perform Numerical Analysis\n2. Search\n0. Quit\nEnter: ")
		if(select == '1'):
			# prints out all the row names on the same line
			print("Descriptor\t", end = "", flush = True)
			for i in range(len(data[0])):
				print(data[0][i], "\t", end = "", flush = True)
			
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
						1+1
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
						1+1
					else:
						# appends values to the list
						listNums.append(float(row[i]))
				# calculates mean and appends to the list
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
						1+1
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
						1+1
					else:
						# appends values to the list
						listNums.append(float(row[i]))
				# calculates mode
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
						1+1
					else:
						# appends values to the list
						count += 1
						# calculates variance 
						listTotal += (float(row[i]) - listOfMeans[i])**2
				# appends variance
				listOfVariances.append(listTotal/count)

			print("")
			print("SD\t\t", end = "", flush = True)
			for i in range(0, len(data[0])):
				# calculates standard deviation
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
						1+1
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
						1+1
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
						1+1
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
						1+1
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
						1+1
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
						1+1
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
						1+1
					else:
						# appends values to the list
						listNums.append(float(row[i]))
				# finds max value
				print(max(listNums),"\t\t", end = "", flush = True)

						

		elif(select == '2'):
			
			#print(data[0][0])

			#df = pd.DataFrame(data=data)
			#df.to_csv("example.csv")
			#for row in data:
				#print(row[4])

			# boolean flag to track valid input
			isValid = False
			val = input("Input the value you want to search: ")
			while(not isValid):
				colnum = input("Input the column number you want to search (0-6) or leave blank to search dataset: ")
				if(len(colnum) == 0):
					isValid = True
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
else: 
	print("Invalid selection.")

