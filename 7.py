def findCommon(list1, list2):
	flag = False
	for i in range(len(list1)):
		for j in range(len(list2)):
			if list1[i] == list2[j]:
				flag = True
				break
	return flag

a = list(map(int, input("Enter the list 1 seperated by comma: ").split(",")))
b = list(map(int, input("Enter the list 2 seperated by comma: ").split(",")))

common = findCommon(a, b)

if common:
	print("They have common elements.")
else:
	print("They don't have common elements.")
