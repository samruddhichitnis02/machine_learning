"""The table below shows the height, x, in inches and the pulse rate, y, per minute,
for 9 people. Write a program to find the correlation coefficient and interpret your result.
x ⇒ 68 72 65 70 62 75 78 64 68
y ⇒ 90 85 88 100 105 98 70 65 72"""



import math
X=[68,72,65,70,62,75,78,64,68]# height X in inches
Y=[90,85,88,100,105,98,70,65,72]#pulse rate Y per minute

n=len(X) #n is the length of list X

sum_of_X=0
for i in range(len(X)):
    sum_of_X=sum_of_X+X[i]
print('Summation of X-',sum_of_X) #sum_of_X gives the sum total of all the values in list X


X_bar=(sum_of_X/n)
print('The value of X bar-',X_bar)

x=[ ] #list x contains all the value of subtraction(that is X-X_bar)
for i in range(len(X)):
    a=X[i]-X_bar
    x.append(a)


for i in range(len(x)):
    x[i]=round(x[i],2) #rounding off all the values in list x to 2 digits
print('Value of x(subtraction of X bar from X)-',x)


sum_of_x=0
for i in range(len(x)):
    sum_of_x=sum_of_x+x[i]
sum_of_x=round(sum_of_x,2)
print('Summation of x-',sum_of_x) #sum_of_x gives the sum total of all the values in list x


x_square=[ ] #list x_square holds all the values of x's square
for i in range(len(x)):
    x_square.append(x[i]*x[i])


for i in range(len(x_square)):
    x_square[i] = round(x_square[i], 2) #rounding off all the values in list x_square to 2 digits
print('Value of x*x-',x_square)

sum_of_x_square=0
for i in range(len(x_square)):
    sum_of_x_square=sum_of_x_square+x_square[i] #calculating the total value of x square

sum_of_x_square=round(sum_of_x_square,2) #rounding of the value of sum of x square to 2 digits
print('Summation of x square-',sum_of_x_square)

#n=len(X)
sum_of_Y=0
for i in range(len(Y)):
    sum_of_Y=sum_of_Y+Y[i]
print('Summation of Y-',sum_of_Y) #sum_of_Y gives the sum total of all the values in list Y


Y_bar=(sum_of_Y/n)
print('The value of Y bar is-',Y_bar)


y=[ ] #list y contains all the value of subtraction(that is Y-Y_bar)
for i in range(len(Y)):
    a=Y[i]-Y_bar
    y.append(a)


for i in range(len(y)):
    y[i]=round(y[i],2) #rounding off all the values in list y to 2 digits
print('Value of y(subtraction of Y bar from Y)-',y)


sum_of_y=0
for i in range(len(y)):
    sum_of_y=sum_of_y+y[i]
sum_of_y=round(sum_of_y,2)
print('Summation of y-',sum_of_y) #sum_of_y gives the sum total of all the values in list y



y_square=[ ] #list y_square holds all the values of y's square
for i in range(len(y)):
    y_square.append(y[i]*y[i])


for i in range(len(y_square)):
    y_square[i] = round(y_square[i], 2) #rounding off all the values in list y_square to 2 digits
print('All the values of y*y-',y_square)

sum_of_y_square=0
for i in range(len(y_square)):
    sum_of_y_square=sum_of_y_square+y_square[i] #calculating the total value of y square

sum_of_y_square=round(sum_of_y_square,2) #rounding of the value of sum of y square to 2 digits
print('Summation of y square-',sum_of_y_square)

xy=[ ] #list to hold the values of x*y
for i in range(len(x)):
    a=x[i]*y[i]
    xy.append(a)

for i in range(len(xy)):
    xy[i]=round(xy[i],2) #rounding of all the values of xy to 2 digits
print('Product of x*y-',xy)

sum_of_xy=0
for i in range(len(xy)):
    sum_of_xy=sum_of_xy+xy[i]
print('Summation of product xy-',sum_of_xy)

r=(sum_of_xy/math.sqrt(sum_of_x_square*sum_of_y_square)) #Formula for calculating correlation coefficient
print('The correlation coefficient is-',round(r,2))
print("Since the value of correlation coefficient that is r is negative it's a negative correlation")
