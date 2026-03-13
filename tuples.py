num = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
fruits = ['banana', 'apple']
text = 'Hello World'

all = (num, fruits, text)

# not like with a list with a seccond [], you can access a variable from a list in the whole tuple
print(all[0][1])

# the : in the secont [] is for the range from the index of the first to the second number
print(all[0][0:3])

#num.count, count all the variables from a tuple
print(num.count(1))

