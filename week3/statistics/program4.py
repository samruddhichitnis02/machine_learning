"""Write a program to multiply matrices in problem 1
"""
# X=[[12,7,3],
#    [4,5,6],
#    [7,8,9]]

# Y=[[5,8,1],
#    [6,7,3],
#    [4,5,9]]



def store_in_X():  #Creating a Matrix for X by taking input from user
    X=[ ]
    m=int(input('Enter the number of rows-'))
    n=int(input('Enter the number of coloumns-'))
    for i in range(m):
        X.append([ ])
    for i in range(0,m):
        for j in range(0,n):
            X[i].append(j)
            X[i][j]=int(input('Enter the elements-'))
    return X

def store_in_Y(): #creating a Matrix for Y by taking input from user
    Y = []
    m = int(input('Enter the number of rows-'))
    n = int(input('Enter the number of coloumns-'))
    for i in range(m):
        Y.append([])
    for i in range(0, m):
        for j in range(0, n):
            Y[i].append(j)
            Y[i][j] = int(input('Enter the elements-'))
    return Y



X=store_in_X()
Y=store_in_Y()
result=[ ] #Matrix to store the product of X and Y

for i in range(len(X)):
    result.append([ ])
for i in range(len(X)):
    for j in range(len(Y)):
        result[i].append(j)
        result[i][j]=0


for i in range(len(X)): #Multiplying the Matrices X and Y
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j]=result[i][j]+X[i][k]*Y[k][j]



for i in range(len(X)): #printing the result Matrix
    for j in range(len(Y)):
        print(result[i][j],end=' ')
    print()