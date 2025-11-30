def generatePrime(lower, upper):
	for i in range(lower, upper + 1):
		flag = True
		for j in range(2, i//2 + 1):
			if i % j == 0:
				flag = False
		if flag:
			print(i, end = "\t")

	print()

lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))

generatePrime(lower, upper)
