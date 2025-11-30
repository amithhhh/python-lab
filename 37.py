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
            exit()
        temp = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                temp.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return temp

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            print("Rows or columns mismatch for subtraction.")
            exit()
        temp = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                temp.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return temp

    def __mul__(self, other):
        if self.cols != other.rows:
            print("Rows or columns mismatch for multiplication.")
            exit()
        temp = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    temp.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return temp


m = Matrix(3, 3)
n = Matrix(3, 3)

print("Enter the first matrix:")
m.initMatrix()
print("Enter the second matrix:")
n.initMatrix()

o = m + n
print("Addition:")
print(o.matrix)

p = m - n
print("Subtraction:")
print(p.matrix)

q = m * n
print("Multiplication:")
print(q.matrix)
