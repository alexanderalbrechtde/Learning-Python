class Car:
    company = 'VW'

    def __init__(self, model, age):
        self.model = model
        self.age = age


polo = Car('polo', 20)
passat = Car('passat', 101)

# query the attribute from different objects
print(polo.model)
print(passat.company)

# change parameters
polo.age = 30

print(polo.age)


class Human:

    def __init__(self, name: str, age: int, location: str) -> None:
        self.__name = name
        self.__age = age
        self.__location = location

    # getter will be decorated with property
    @property
    def name(self) -> str:
        return self.__name

    # and with that the setter will be named with name.setter
    @name.setter
    def name(self, name: str):
        self.__name = name

    @name.deleter
    def name(self):
        print('Name wurde gelöscht!')
        self.__name = ''

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        self.__location = location

    def description(self):
        return '{0} is {1} years old.'.format(self.name, self.age)

    def language(self, language):
        return '{0} is from {1} and speake {2}.'.format(self.name, self.location, language)


alex = Human('Alex', 21, 'Germany')

alex.location = 'Berlin'

print(alex.description())
print(alex.language('german'))
print(alex.name + ' is here')
