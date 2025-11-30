import math

def dectobin(dec):
	pos = 0
	rem = 0
	bin = 0
	while(dec != 0):
		rem = dec % 2
		bin += rem * math.pow(10, pos)
		dec = dec // 2
		pos += 1
	return int(bin)

val = int(input("Enter the decimal value: "))

binary = dectobin(val)

print(f"binary: {binary}") 
