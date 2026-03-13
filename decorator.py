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


def upperCase(function):
    def wrapper():
        result = function()
        return result.upper()

    return wrapper


def greeting():
    return 'hello there'


decorator = upperCase(greeting)
print(decorator())
