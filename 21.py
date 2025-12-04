file = open("sample.txt", "r")
text = file.read()
file.close()

chars = 0
alphabets = 0
vowels = 0
numbers = 0
special = 0

vowel_list = "aeiouAEIOU"

for ch in text:
    chars += 1

    if ch.isalpha():
        alphabets += 1
        if ch in vowel_list:
            vowels += 1
    elif ch.isdigit():
        numbers += 1
    else:
        if ch not in ['\n', '\t', ' ']: 
            special += 1

print("Total characters:", chars)
print("Alphabets:", alphabets)
print("Vowels:", vowels)
print("Numerals:", numbers)
print("Special characters:", special)
