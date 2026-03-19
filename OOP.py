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

    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def description(self):
        return '{0} is {1} years old.'.format(self.name, self.age)

    def language(self, language):
        return '{0} is from {1} and speake {2}.'.format(self.name, self.location, language)

    def set_location(self, location):
        self.location = location

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_location(self):
        return self.location


alex = Human('Alex', '21', 'Germany')

alex.set_location('Berlin')

print(alex.description())
print(alex.language('german'))
print(alex.get_name() + ' is here')
