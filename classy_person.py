'''
Starter code!
don't forget the use of 'self' and to have the methods:
1. __init__
2. increase_age
3. say_greeting
4. count_to_age
'''

class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name
        # print(self.name, "constructed")
        
    def increase_age(self):
        self.age += 1
        # print(self.age)
    
    def say_greeting(self):
        print(f'Hello world! My name is {self.name}!')
        
    def count_to_age(self):
        Birth = 1
        while Birth <= self.age:
            
            print(Birth)
            Birth +=1
# Kamron = Person(30, "Kamron")
# chuck = Person(age=56, name='Charles R. Severance')
# print(chuck.age)

# chuck.increase_age()
# print(chuck.age)

# chuck.say_greeting()
# chuck.count_to_age()

# print(Kamron.age)
# print(Kamron.count_to_age())


# You won't need to call anything here.
# Assignment:
# You've learned how to make a Python class that has its own values, methods and initializes its values.
# Build a class called Person
# This class should have a constructor that takes in a name and age and sets its values accordingly.
# This class should have 4 methods:
# __init__ method that passed name and age to itself.
# increase_age method that increases the object's age by 1
# say_greeting method that prints out: Hello world! My name is { objects_name }!
# count_to_age method that prints 1 to the current age of the object as a loop.
# Starter Code
# ''' Starter code! don't forget the use of 'self' and to have the methods:
# init
# increase_age
# say_greeting
# count_to_age '''
# Expected output
# I'll be construction an object with your class. If the object I made is nathan = Person(32, "Nathan") I would expect:
# print(nathan.age)
# 32
# nathan.say_greeting()
# Hello world! My name is Nathan!
# nathan.increase_age()
# print(nathan.age)
# 33
# nathan.count_to_age()
# 1
# 2
# ... (numbers 3-32)
# 33