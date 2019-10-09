"""Write a program to find inverse matrix of matrix X in problem 1	"""



X=[[12,7,3],
   [4,5,6],
   [7,8,9]]

result=[ ]
for i in range(len(X)):
    result.append([ ])
for i in range(len(X)):
    for j in range(len(X)):
        result[i].append(j)

a=(X[0][0]*((X[1][1]*X[2][2])-(X[1][2]*X[2][1])))
b=-(X[0][1]*((X[1][0]*X[2][2])-(X[2][0]*X[1][2])))
c=(X[0][2]*((X[1][0]*X[2][1])-(X[2][0]*X[1][1])))

det=a+b+c


A11=(X[1][1]*X[2][2])-(X[2][1]*X[1][2])
A12=-((X[1][0]*X[2][2])-(X[1][2]*X[2][0]))
A13=(X[1][0]*X[2][1])-(X[2][0]*X[1][1])
A21=-((X[0][1]*X[2][2])-(X[2][1]*X[0][2]))
A22=(X[0][0]*X[2][2])-(X[2][0]*X[0][2])
A23=-((X[0][0]*X[2][1])-(X[0][1]*X[2][0]))
A31=(X[0][1]*X[1][2])-(X[1][1]*X[0][2])
A32=-((X[0][0]*X[1][2])-(X[1][0]*X[0][2]))
A33=(X[0][0]*X[1][1])-(X[1][0]*X[0][1])

Y=[[A11,A21,A31],
   [A12,A22,A32],
   [A13,A23,A33]]

determinant=1/det

for i in range(len(X)):
    for j in range(len(X)):
        result[i][j]=determinant*Y[i][j]

for i in range(len(Y)):
    for j in range(len(Y)):
        print(result[i][j],end=' ')
    print( )