import csv
import pandas as pd

with open('hepatitis.csv', 'r') as file, open('states.csv', 'rb') as fileTwo:
	reader = csv.DictReader(file)
	readerTwo = pd.read_csv('./states.csv')

	week = 0
	state = "AK"

	stateCount = 1
	line = readerTwo.iloc[stateCount, 0]

	for row in reader:# and line in readerTwo:
		if (row['week']) > "198100":
			break

		if (row['week'] != week):
			stateCount = 1
			line = readerTwo.iloc[stateCount, 0]
			while (line != row['state']):
				stateCount += 1
				line = readerTwo.iloc[stateCount, 0]
				print("0", end="\t")
			week = row['week']
			print("\n" + row['week'] + "\t" + row['cases'], end="\t")

		else:
			while (line != row['state']):
				stateCount += 1
				line = readerTwo.iloc[stateCount, 0]
				print("0", end="\t")
			print(row['cases'], end="\t")


file.close()
fileTwo.close()

