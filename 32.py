import re

# Sample text
text = "John was born on 12/08/2003 and his sister on 5-7-2005. Another date is 23.09.2020."

# Regular expression pattern for dates
date_pattern = r"\b\d{1,2}[\/\-.]\d{1,2}[\/\-.]\d{4}\b"

# Find all dates in the text
dates = re.findall(date_pattern, text)

print("Dates found in the text:", dates)
