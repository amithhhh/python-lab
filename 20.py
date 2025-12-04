

source = input("Enter the source file name: ")
destination = input("Enter the destination file name: ")

with open(source, "rb") as src:
     with open(destination, "wb") as dest:
          dest.write(src.read())

print("File duplicated successfully!")

