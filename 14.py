sentence = input("Enter a sentence: ")

sentence = sentence.lower()

frequency = {}

for char in sentence:
    if char.isalpha(): 
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

print("Letter frequencies:")
for letter, count in sorted(frequency.items()):
    print(f"{letter}: {count}")
