class Complex:
	def __init__(self, real = 0, complex = 0):
		self.real = real
		self.complex = complex

	def __add__(self, other):
		temp = Complex()
		temp.real = self.real + other.real
		temp.complex = self.complex + other.complex
		return temp
	def __sub__(self, other):
		temp = Complex()
		temp.real = self.real - other.real
		temp.complex = self.complex - other.complex
		return temp

a = Complex(10, 20)
b = Complex(30, 40)

c = a + b
d = a - b

print(f"A + B = {c.real} + {c.complex}i")
print(f"A - B = {d.real} + {d.complex}i")
