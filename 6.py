def alterString(str):
	if str[:2] == "is":
		return str
	else:
		return "is" + str


str = input("Enter the string: ")

newStr = alterString(str)

print(f"New String: {newStr}")
