import os
import logging

logging.basicConfig(
			filename = "40.2.txt",
			level = logging.INFO
		)

path = input("Enter the path: ")

try:
	if os.path.exists(path):
		logging.error("File path already exists")
		print("[-]File already exists!")
	
	choice = input("Do you want to overwrite it (yes/no): ")
	if  choice.lower() != "yes":
		exit()
	with open(path, "w") as file:
		content = input("Enter the content: ")
		file.write(content)
except PermissionError:
	logging.error("Permission Error: permission denied")
	print("Permission denied.")
except FileNotFoundError:
	logging.error("FileNotFoundError: file not found")
	print("Invald file path")
except Exception as e:
	print("Unexpected error.")
	

