def fib(num):
	if num == 0:
		return 0
	elif num == 1:
		return 1
	else:
		return fib(num - 1) + fib(num - 2)
		

n = int(input("Enter the limit: "))

for i in range(n + 1):
	print(fib(i), end=" ")
	
print()
