import csv
import pandas as pd

numStates = 51

with open('hepatitis.csv', 'r') as file, open('states.csv', 'rb') as fileTwo:
	reader = csv.DictReader(file)
	readerTwo = pd.read_csv('./states.csv')

	week = 0
	state = "AK"

	stateCount = 0
	line = readerTwo.iloc[stateCount, 0]
	first = True
	#print (str(line))

	for row in reader:
		if (row['week']) > "198100":
			break

		if (row['week'] != week):
			if (not first):
				for i in range(stateCount, numStates):
					print("0", end=",\t")
				print("\n", end="")
			first = False
			stateCount = 0
			line = readerTwo.iloc[stateCount, 0]
			print(row['week'], end=",\t")
			while (line != row['state']):
				print("0", end=",\t")
				stateCount += 1
				line = readerTwo.iloc[stateCount, 0]
			week = row['week']
			print(row['cases'], end=",\t")
			stateCount += 1
			line = readerTwo.iloc[stateCount, 0]


		else:
			while (line != row['state']):
				print("0", end=",\t")
				stateCount += 1
				line = readerTwo.iloc[stateCount if stateCount < numStates else numStates - 1, 0]
			print(row['cases'], end=",\t")
			stateCount += 1
			line = readerTwo.iloc[stateCount if stateCount < numStates else numStates - 1, 0]
	for i in range(stateCount, numStates):
		print("0", end=",\t")

file.close()
fileTwo.close()

