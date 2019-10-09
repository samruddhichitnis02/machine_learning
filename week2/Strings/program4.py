"""Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is
less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
"""

n=input('Enter a string-')
if(len(n)>=3):
    if n[-3:]=='ing':
        n=n+'ly'
        print(n)
    if n[-3:] !='ing':
        n=n+'ing'
        print(n)
else:
    print(n)