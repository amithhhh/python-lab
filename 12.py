def removeDuplicates(list1):
	newList = []
	for i in list1:
		if i not in newList:
			newList.append(i)
	return newList

list1 = list(map(int, input("Enter the list of numbers seperated by commas: ").split(",")))

list2 = removeDuplicates(list1)

print(f"new list: {list2}")
