"""import math
print(math.pi)
print(math.pow(2,4))
print(math.sqrt(16))
print(math.sin(30))

#module
import chinmay

ans = chinmay.add(2,3)



#os module
import os

# Get the current working directory
print("Current working Directory: ", os.getcwd())

# Get all files in the directory
print("List in directory: ", os.listdir())

# Create a new directory
os.mkdir("Test directory")
print("New directory created")

# Rename the directory
os.rename("Test directory", "Test")
print("Directory renamed successfully")

# Remove the directory
os.rmdir("Test")
print("Directory removed successfully")


#sys module
import sys
print(sys.version)

print(sys.platform)

print(sys.path)


#datetime
from datetime import datetime, date, timedelta

current_datetime = datetime.now()
print(current_datetime)

print(current_datetime.strptime("%d-%m-%y %H:%H:%S"))

current_date = date.today()
print(current_date)

class Math:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b
math_inst = Math()

ans = math_inst.add(a=10, b=20)
print(ans)

ans = math_inst.multiply(a=10, b=20)
print(ans)



class Example:
    class_variable = "I am a class variable"  # shared by all instances

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @staticmethod
    def static_method():
        try:
            print(self.instance_variable)  # No 'self' in static methods
        except NameError as e:
            print("Cannot Access instance variable", e)  # Cannot Access instance variable name 'self' is not defined

        print(Example.class_variable)  # I am a class variable

    def instance_method(self):
        print(self.instance_variable)  # I am a Instance Variable
        print(Example.class_variable)  # I am a class variable

obj = Example("I am a Instance Variable")
obj.static_method()
obj.instance_method()


class Student:
    name = "Arun Kumar Sharma"  # Class variable

    def change_name(self, name):
        self.name = name  # Creating an instance variable

std1 = Student() 
std1.change_name("Sourav Kumar Sharma")  # Updating the instance variable

print(std1.name)  # Accessing the instance variable
print(Student.name)  # Accessing the class variable

class Student:
    name = "Arun Kumar Sharma"  # Class variable
    @classmethod
    def change_name(cls, name):
        cls.name = name  # Creating an instance variable

std1 = Student()
std1.change_name("Sourav Kumar Sharma")  # Updating the instance variable

print(std1.name)  # Accessing the instance variable
print(Student.name)  # Accessing the class variable

class Student:
    def __init__(self, math, phy, che):
        self.math = math
        self.phy = phy
        self.che = che

    @property
    def percentage(self):
        return str((self.math + self.phy + self.che) / 3) + "%"

std1 = Student(math=70, phy=80, che=90)
print(std1.percentage) 

std1.phy = 50
print(std1.percentage) """

A = {1, 2, 3} 
B = {4, 5, 6, 7, 8} 
result = A - B 
print(result)











