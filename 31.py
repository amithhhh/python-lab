import re


text = "Hello world! This world is beautiful. Welcome to the world of Python."

print(f"sample text: {text}")
old_word = input("Enter the text you want to change from the text: ")
new_word = input("Enter the new word: ")

 
updated_text = re.sub(old_word, new_word, text)

print("Original Text:")
print(text)
print("Updated Text:")
print(updated_text)
