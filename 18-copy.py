
dictionary = {
    "acquiesce": "To accept something reluctantly without protest.",
    "catharsis": "The release of strong or repressed emotions.",
    "esoteric": "Understood by only a small number of people.",
    "mellifluous": "Sweet or musical; pleasant to hear.",
    "nefarious": "Wicked or criminal.",
    "serendipity": "The occurrence of events by chance in a happy way."
}

word = input("Enter a word to search: ").lower()

if word in dictionary:
    print("Meaning:", dictionary[word])
else:
    print("Word not found in dictionary.")
