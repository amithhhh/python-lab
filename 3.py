str = input("Enter the string: ")

upper, special, digit, swapped = "", "", "", ""

for i in str:
	if i.isupper():
		upper += i
		swapped += i.lower()
	elif not i.isalnum():
		special += i
	elif i.isdigit():
		digit += i
	elif i.islower():
		swapped += i.upper()

print(f"upper: {upper}")
print(f"special: {special}")
print(f"digit: {digit}")
print(f"swapped: {swapped}")
