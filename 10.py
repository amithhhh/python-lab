def binary_to_decimal(b):
    return int(b, 2)

def decimal_to_binary(d):
    return bin(d)[2:]

print("1. Binary to Decimal")
print("2. Decimal to Binary")

choice = int(input("Enter your choice: "))

if choice == 1:
    b = input("Enter binary number: ")
    print("Decimal =", binary_to_decimal(b))

elif choice == 2:
    d = int(input("Enter decimal number: "))
    print("Binary =", decimal_to_binary(d))

else:
    print("Invalid choice")
