def number_to_words(num):
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
             "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty",
            "sixty", "seventy", "eighty", "ninety"]

    if num < 10:
        return ones[num]
    elif num < 20:
        return teens[num - 10]
    elif num < 100:
        if num % 10 == 0:
            return tens[num // 10]
        else:
            return tens[num // 10] + "-" + ones[num % 10]
    elif num < 1000:
        if num % 100 == 0:
            return ones[num // 100] + " hundred"
        else:
            return ones[num // 100] + " hundred and " + number_to_words(num % 100)
    else:
        if num % 1000 == 0:
            return ones[num // 1000] + " thousand"
        else:
            return ones[num // 1000] + " thousand " + number_to_words(num % 1000)


number = int(input("Enter a number (0–9999): "))
print("In words:", number_to_words(number))
