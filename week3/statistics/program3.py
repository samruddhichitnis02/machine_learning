"""Write a program to perform multiplication of given matrix and vector
			X = [[ 5, 1 ,3], [ 1, 1 ,1], [ 1, 2 ,1]], Y = [1, 2, 3]"""



Y=[1,2,3]

X=[[5,1,3],
   [1,1,1],
   [1,2,1]]

result=[0,0,0]

for i in range(1):
    for j in range(len(Y)):
        for k in range(len(Y)):
            result[j]=result[j]+Y[k]*X[k][j]

print(result)