try:
	a = int(input("Enter the first number: "))
	b = int(input("Enter the second number: "))
	c = a / b
	print(f"c={c}")
except ValueError:
	print("Please input only integer values.")
except ZeroDivisionError:
	print("Denominator can't be zero.")
except Exception:
	print("Unexpected error.")
