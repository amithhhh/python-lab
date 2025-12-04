import re

text = "Maria bought her first laptop on 22/05/2016 and her friend on 9-8-2017. There was also a sale on 01.12.2021."

uppercase = re.findall(r"[A-Z]", text)
lowercase = re.findall(r"[a-z]", text)
special   = re.findall(r"[^A-Za-z0-9\s]", text)

print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Special Characters:", special)
