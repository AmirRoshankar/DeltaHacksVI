import csv

with open('hepatitis.csv', 'r') as file, open('states.csv', 'rb') as fileTwo:
	reader = csv.DictReader(file)
	readerTwo = csv.DictReader(fileTwo)

	week = 0
	state = "AK"

	stateCount = 0

	for row in reader:# and line in readerTwo:
		if (row['week']) > "198100":
			break
		#if (line['state'] != state):
		#	state = line['state']
		#	print("0", end="\t")
		if (row['week'] != week):
			week = row['week']
			print("\n" + row['week'] + "\t" + row['cases'], end="\t")
		else:
			print(row['cases'], end="\t")

file.close()
fileTwo.close()

