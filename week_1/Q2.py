def myFunction():
	numberOfRecords = int(input("Enter Number Of Records: "))
	print(f"\nEnter {numberOfRecords} Students Records in The Following Format: ")

	records = []

	for x in range(numberOfRecords):
		rollNo = input("Roll NO: ")
		name = input("Name: ")
		age = int(input("Age: "))
		marks = int(input("Marks: "))
		while marks > 100:
			marks = int(input("Error, Marks cannot be > 100, re-input: "))
		records.append({'RollNo':rollNo, 'Name':name, 'Age':age, 'Marks':marks})
		print()

	print("Results\n")
	print("RollNo | Name | Age | Marks")

	for x in range(numberOfRecords):
		print(records[x]["RollNo"], end=" | ")
		print(records[x]["Name"], end=" | ")
		print(records[x]["Age"], end=" | ")
		print(records[x]["Marks"])

	summ = 0
	for x in range(numberOfRecords):
		summ = summ + records[x]["Marks"]

	print(f"\nAverage = {summ / numberOfRecords}")

	marks = []
	for x in range(numberOfRecords):
		tempMarks = [records[x]["Marks"]]
		marks.append(tempMarks)

	print("Class Highest = ",max(marks))
	print("Class Lowest = ",min(marks))

myFunction()