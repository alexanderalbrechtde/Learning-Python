def plus_one(num):
    return num + 1


# set a function into a variable to use it in the way of a variable
add_one = plus_one
print(add_one(5))


# give a function as a parameter
def function_call(function):
    number_to_add = 10
    return function(number_to_add)


print(function_call(plus_one))


# functon create another function
def greet():
    def say_hi():
        return 'Hi'

    return say_hi


greeting = greet()
print(greeting())


# decorator of the greet-function, if we call greet, greet is automatically in the def decorator(greet) and the output lands between before and after
def decorator(function):
    def wrapper():
        print('before')
        function()
        print('after')

    return wrapper


@decorator
def greet():
    print('Hello')


greet()


def uppercase(function):
    def wrapper():
        result = function()
        return result.upper()

    return wrapper


def lowercase(function):
    def wrapper():
        result = function()
        return result.lower()

    return wrapper


def greeting():
    return 'hello there'


decorator = uppercase(greeting)
print(decorator())


# in the use case of 2 or more decorator, will the nearest to the function be the first one in the order
@lowercase
@uppercase
def greeting2():
    return 'hello, my name is ALEX  '


print(greeting2())

# arguments in decorator are given in the wrapper and to call in the function call at the end
def arguments(function):
    def arguments_wrapper(arg1, arg2):
        print('My arguments are: {0}, {1}'.format(arg1, arg2))
        function(arg1, arg2)

    return arguments_wrapper


@arguments
def love(love1, love2):
    print('I love {0} and {1}'.format(love1, love2))


love("pizza", "cars")
