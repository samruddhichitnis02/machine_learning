""" Write a python program to add below matrices
   			        X = [[12,7,3],
    			        [4 ,5,6],
    			        [7 ,8,9]]
			        Y = [[5,8,1],
    			        [6,7,3],
    			        [4,5,9]]
"""




X=[[12,7,3],
   [4,5,6],
   [7,8,9]]

Y=[[5,8,1],
   [6,7,3],
   [4,5,9]]

result=[ ]
for i in range(len(X)):
    result.append([ ])
for i in range(len(X)):
    for j in range(len(Y)):
        result[i].append(j)
        result[i][j]=0


for i in range(len(X)):
    for j in range(len(Y)):
        result[i][j]=X[i][j]+Y[i][j]


for i in range(len(X)):
    for j in range(len(Y)):
        print(result[i][j],end=' ')
    print( )