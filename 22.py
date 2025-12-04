
f = open("sample.txt", "r")

lines = 0
words = 0

for line in f:
    lines += 1                       
    word_list = line.split()         
    words += len(word_list)          

f.close()

print("Number of lines:", lines)
print("Number of words:", words)
