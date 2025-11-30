a = int(input("Enter the value1: "))
b = int(input("Enter the value2: "))

while b != 0:
	a,b = b, a % b

print(f"GCD: {a}")
