def sum(list1):
	sum = 0
	for i in list1:
		sum += i
	return sum

def mean(list1):
	return sum(list1) / len(list1)

def median(list1):
	data = sorted(list1)
	mid = len(list1) // 2

	if len(list1) % 2 == 0:
		return (data[mid - 1] + data[mid]) / 2
	else:
		return data[mid]

def variance(list1):
	sum = 0
	N = len(list1)
	m = mean(list1)
	for i in list1:
		sum += (i - m) ** 2
	return sum / N

list1 = list(map(int, input("Enter the list seperated by comma: ").split(",")))	
print(f"sum: {sum(list1)}")
print(f"mean: {mean(list1)}")
print(f"median: {median(list1)}")
print(f"variance: {variance(list1)}")
