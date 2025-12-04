
f = open("sample.txt", "r")
text = f.read()
f.close()

old_word = input("Enter the old text: ")
new_word = input("Enter the new text: ")

updated_text = text.replace(old_word, new_word)

f = open("sample.txt", "w")
f.write(updated_text)
f.close()

print("All occurrences of", old_word, "replaced with", new_word)
