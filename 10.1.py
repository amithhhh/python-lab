#binary to decimal
import math

def bintodec(bin):
	pos = 0
	dec = 0
	rem = 0
	while (bin != 0):
		rem = bin % 10
		dec += rem * math.pow(2, pos)
		bin = bin // 10 
		pos += 1
	return dec

val = int(input("Enter the number(binary): "))

decimal = bintodec(val)

print(f"decimal value: {decimal}")
