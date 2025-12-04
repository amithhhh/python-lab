import re

text = "Maria bought her first laptop on 22/05/2016 and her friend on 9-8-2017. There was also a sale on 01.12.2021."

date_pattern = r"\b\d{1,2}[\/\-.]\d{1,2}[\/\-.]\d{4}\b"

dates = re.findall(date_pattern, text)

print("Dates found in the text:", dates)
