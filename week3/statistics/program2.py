"""Write a program to perform scalar multiplication of matrix and a number
 	                X = [[12,7,3],
    			        [4 ,5,6],
    			        [7 ,8,9]]
                    Y = 9
"""



X=[[12,7,3],
   [4,5,6],
   [7,8,9]]

Y=9

result=[ ]
for i in range(len(X)):
    result.append([ ])
for i in range(len(X)):
    for j in range(len(X)):
        result[i].append(j)
        result[i][j]=1


for i in range(len(X)):
    for j in range(len(X)):
        result[i][j]=Y*X[i][j]


for i in range(len(X)):
    for j in range(len(X)):
        print(result[i][j],end=' ')
    print( )