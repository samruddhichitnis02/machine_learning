"""Write a Python program to get a string from a given string where all occurrences of its first char have been changed
to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'"""


n=input('Enter a string-')
a=n[0]
for i in range(len(n)):
    if(a==n[i]):
        n=n.replace(a,'$')
        n=a+n[1:]

print(n)
