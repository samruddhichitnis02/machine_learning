"""Write a program to find transpose matrix of matrix Y in problem 1"""

Y = [[5,8,1],
     [6,7,3],
     [4,5,9]]

a11=Y[0][0]
a12=Y[0][1]
a13=Y[0][2]
a21=Y[1][0]
a22=Y[1][1]
a23=Y[1][2]
a31=Y[2][0]
a32=Y[2][1]
a33=Y[2][2]

transpose=[[a11,a21,a31],
           [a12,a22,a32],
           [a13,a23,a33]]
for i in range(len(Y)):
    for j in range(len(Y)):
        print(transpose[i][j],end=' ')
    print( )