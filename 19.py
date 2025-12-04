
dictionary = {
    "aberration": "A departure from what is normal or expected, typically unwelcome.",
    "benevolent": "Well-meaning and kindly; showing goodwill.",
    "cognizant": "Having knowledge or being aware of something.",
    "deleterious": "Causing harm or damage.",
    "ephemeral": "Lasting for a very short time.",
    "fortuitous": "Happening by chance, often in a lucky way.",
    "gregarious": "Fond of company; sociable.",
    "lucid": "Expressed clearly; easy to understand.",
    "magnanimous": "Generous or forgiving, especially towards a rival.",
    "obfuscate": "To make something unclear or difficult to understand.",
}


word = input("Enter a word to search: ").lower()

if word in dictionary:
    print("Meaning:", dictionary[word])
else:
    print("Word not found in dictionary.")
