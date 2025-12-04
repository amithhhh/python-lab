
src = open("sample.txt", "r")

dest = open("dest.txt", "a")

for line in src:
    dest.write(line)

src.close()
dest.close()

print("File appended successfully.")
