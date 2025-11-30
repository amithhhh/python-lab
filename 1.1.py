num = int(input("Enter the number: "))

i = 2
flag = True

while (i <= num//2):
	if (num % i == 0):
		flag = False
		break
	i += 1

if flag:
	print(f"{num} is a prime number.")
else:
	print(f"{num} is not a prime number.")
