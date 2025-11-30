def gcd(a, b):
	while b != 0:
		a, b = b, a % b
	return a


a = int(input("Enter the number1: "))
b = int(input("Enter the number2: "))

c = gcd(a, b)

print(f"GCD: {c}")
