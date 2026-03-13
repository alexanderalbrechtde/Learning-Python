import pandas as pd


def array():
    fruits = ['apple', 'banana', 'mango']
    for n in fruits:
        print(n)


# array()

def square():
    num = [1, 2, 3, 4, 5]
    for n in num:
        print(n * n)


# square()

def mix():
    num = [1, 2, 3, 4, 5]
    fruits = ['apple', 'banana', 'mango', 'pineapple', 'cherry']
    # print (len(fruits))
    for f, n in zip(fruits, num):
        print(n, f)
        print(len(f))


# mix()

num = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'mango', 'pineapple', 'cherry']

df = pd.DataFrame({'Number': num, 'Fruits': fruits})

print(df)
