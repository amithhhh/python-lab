def matrix(n):

    M=[]

    for i in range(n):

        print("Enter elements of row",i+1,end=" : ")

        r=list(map(int,(input()).split()))

        M.extend([r])

    return M

def add_sub(a,b,m,n):

    r=[[a[i][j] + b[i][j] for j in range(n)] for i in range(m) ]

    print("\nMatrix Addition      :\n",r)

    r=[[a[i][j] - b[i][j] for j in range(n)] for i in range(m)]

    print("Matrix Subtraction   :\n",r)

def multiply(a, b):

    r = [[0]*len(b[0]) for _ in range(len(a))]

    if len(b)!=len(a[0]):

        print("Matrix multiplication is not possible !")

        return

    for i in range(len(a)): # rows in A : m

        for j in range(len(b[0])): # columns in B : q

            for k in range(len(b)): # rows in B : p = n(column in A)

                r[i][j] += a[i][k] * b[k][j]

    print("Matrix Multiplication:\n",r) 

m=list(map(int,(input("Enter no. of rows and columns in 1st matrics : ")).split()))

p=list(map(int,(input("Enter no. of rows and columns in 2nd matrics : ")).split()))

print(" \nEnter elements of 1st Matrix")

A=matrix(m[0])

print(" \nEnter elements of 2nd Matrix")

B=matrix(p[0])

if len(A[0])==len(B[0]) and len(A)==len(B):

    add_sub(A,B,m[0],m[1])

else:

    print("Matrix additon and subtraction is not possible!")

multiply(A,B)

