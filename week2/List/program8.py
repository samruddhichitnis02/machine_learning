"""Write a Python program to find the list of words that are longer than n from a given list of words."""


def long_words(n, str):
    x=[]
    txt = str.split(" ")
    for i in txt:
        if(len(i)>n):
            x.append(i)
    return x

print(long_words(3, "The quick brown fox jumps over the lazy dog"))