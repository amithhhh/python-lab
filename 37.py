class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    def initMatrix(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = int(input(f"Enter the element at matrix[{i}][{j}]: "))

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            print("Rows or columns mismatch for addition.")
            return None
        temp = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                temp.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return temp

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            print("Rows or columns mismatch for subtraction.")
            return None
        temp = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                temp.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return temp

    def __mul__(self, other):
        if self.cols != other.rows:
            print("Rows or columns mismatch for multiplication.")
            return None
        temp = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    temp.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return temp

row1 = int(input("Enter the row of first matrix: "))
col1 = int(input("Enter the column of second matrix: "))
m = Matrix(row1, col1)
row2 = int(input("Enter the row of second matrix: "))
col2 = int(input("Enter the column of second matrix: "))
n = Matrix(row2, col2)

print("Enter the first matrix:")
m.initMatrix()
print("Enter the second matrix:")
n.initMatrix()

o = m + n
if o != None:
	print("Addition:")
	print(o.matrix)

p = m - n
if p !=  None:
	print("Subtraction:")
	print(p.matrix)

q = m * n
if q != None:
	print("Multiplication:")
	print(q.matrix)
