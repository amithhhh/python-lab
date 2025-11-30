class Rectangle:
	def __init__(self, length, breadth):
		self.length = length
		self.breadth = breadth
	def area(self):
		return self.length * self.breadth
	def perimeter(self):
		return 2* (self.length + self.breadth)


l = int(input("Enter the length: "))
b = int(input("Enter the breadth: "))

rect = Rectangle(l, b)

area = rect.area()
peri = rect.perimeter()

print(f"Area: {area} || Perimeter: {peri}")
