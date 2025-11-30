import os

path = input("Enter the path: ")

try:
	if os.path.exists(path):
		print("[-]File already exists!")
	
	choice = input("Do you want to overwrite it (yes/no): ")
	if  choice.lower() != "yes":
		exit()
	with open(path, "w") as file:
		content = input("Enter the content: ")
		file.write(content)
except PermissionError:
	print("Permission denied.")
except FileNotFoundError:
	print("Invald file path")
except Exception as e:
	print("Unexpected error.")
	

