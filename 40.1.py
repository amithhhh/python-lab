import logging

logging.basicConfig(
		filename="40.1.txt",
		level=logging.INFO
	)

try:
	a = int(input("Enter the first number: "))
	b = int(input("Enter the second number: "))
	c = a / b
	print(f"c={c}")
except ValueError:
	logging.error("ValueError: Non-integer value recieved")
	print("Please input only integer values.")
except ZeroDivisionError:
	logging.error("ZeroDivisionError: Zero at the denominator")
	print("Denominator can't be zero.")
except Exception:
	logging.error(f"Exception: Unexpected occurred.")
	print("Unexpected error.")
