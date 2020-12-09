def printNameDiagonally():
	name = input("Enter Your Name: ")
	print("Name is: ",name)
	print("\nDiagonally it becomes:")

	for i in range(len(name)):
		if i == 0:
			print(name[0])
		else:
			print("   "*i,name[i])

	print()

	for i in reversed(range(len(name))):
		if i == 0:
			print(name[0])
		else:
			print("   "*i,name[i])

printNameDiagonally()