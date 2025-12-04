emp = (  (1, "Toni", 2000), (2, "modric", 5000), (3,"case", 2100) )

 

id = tuple(sorted(emp, key=lambda x: x[0]))

name = tuple(sorted(emp, key=lambda x: x[1]))

salary = tuple(sorted(emp, key=lambda x: x[2], reverse=True))

print("\nBy id: \n", id)

print("\nBy name: \n", name)

print("\nBy salary (desc):\n", salary)

