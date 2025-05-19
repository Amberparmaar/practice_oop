#  Create a Class and Object
# Make a class called Student with attributes name and age. Then, create an object of that class and print the name and age.
# Add a Method
#In the Student class, add a method introduce() that prints:
#"My name is Ali and I am 20 years old" (values should come from the object).

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def introduce(self):
#         print(f"My name is {self.name} and I am {self.age} years old")

# st= Student("Amber", 30)
# print(st.name)
# print(st.age)
# st.introduce()




#Create a Class with Multiple Methods
#Create a class Calculator with methods add(), subtract(), multiply(), and divide() that take two numbers and return the result.

# class Calculator:

#     def add(self, a, b):
#         return a + b

#     def subtract(self, a, b):
#         return a - b

#     def multiply(self, a, b):
#         return a * b

#     def divide(self, a, b):
#         if b == 0:
#             return "Cannot divide by zero"                                                              
#         return a / b
    
# cal = Calculator()
# print("add:", cal.add(10, 20))
# print("subtract:", cal.subtract(10, 20))
# print("multiply:", cal.multiply(10, 20))
# print("divide:", cal.divide(10, 20))



# Inheritance Example
# Create a class Animal with a method make_sound() that prints "Some sound".
# Then create a class Dog that inherits from Animal and overrides make_sound() to print "Bark".
# Finally, create an object of Dog and call the make_sound() method.

# class Animal:
#     def make_sound(self):
#         print("Some sound")

# class Dog(Animal):
#     def make_sound(self):
#         print("Bark")

#     def info(self):
#         print("I am a dog")    

# dog = Dog()
# dog.make_sound()
# dog.info()


#  Encapsulation
# Create a class Account with a private variable __balance.
# Add methods to deposit(amount) and get_balance().
# Don’t allow direct access to __balance from outside.

# class Account:
#     def __init__(self):
#         self.__balance = 0

#     def deposit(self, amount):
#         self.__balance += amount

#     def get_balance(self):
#         return self.__balance
    
# acc = Account()
# acc.deposit(1000)
# print(acc.get_balance())    

# Encapsulation

# it is use for hiding data
# "Data ko class ke andar chhupa lena aur us tak sirf methods ke zariye access dena."
#Yeh programming mein security aur control ke liye hota hai.
# Aapko agar private variable access ya update karna hai, to aap Getters aur Setters k method ke through karte ho:


# class Bank:

#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance

#     def deposit(self, amount):
#         self.__balance += amount

#     def withdraw(self, amount):
#         if self.__balance >= amount:
#             self.__balance -= amount
#         else:
#             print("Insufficient balance")    

#     def get_balance(self):
#         return self.__balance
    
# bank = Bank("Shoukat", 2000)
# print(bank.owner)
# print(bank.get_balance())
# bank.deposit(1000)
# print(bank.get_balance())
# bank.withdraw(500)
# print(bank.get_balance())

# acess modifiers in python public , private, protected

#Access modifiers define karte hain ke aap kisi class ke variable ya method ko kahan se access kar sakte ho (andar ya baahar se).

# 1. Public (self.variable)
#Is type ka variable ya method har jaga access ho sakta hai — class ke andar bhi aur baahar bhi.

# class Student:
#     def __init__(self, name):
#         self.name = name  # Public

# s1 = Student("Ali")
# print(s1.name)  # Output: Ali (Direct access allowed)

# 2. Protected (self._variable)
#Ye sirf class ke andar aur uske subclasses mein access hota hai.
#Lekin Python mein ye sirf ek convention hai (actual restriction nahi hoti).

# class Student:
#     def __init__(self, name):
#         self._name = name  # Protected

# class ChildStudent(Student):
#     def show(self):
#         print(self._name)

# s = ChildStudent("Sara")
# s.show()          # Output: Sara
# print(s._name)    # Technically possible, but not recommended


# 3. Private (self.__variable)
#Ye sirf class ke andar hi access ho sakta hai.
#Python is variable ka naam internally change (mangle) kar deta hai: _ClassName__variable

# print(a.__balance)        ❌ Error: AttributeError


# 🧩 Question: Create a Class for a Person Profile
# 🔧 Requirements:
# Create a class Person with:

# Public Variable:

# name: Stores the person's name.

# Protected Variable:

# _age: Stores the person's age.

# Private Variable:

# __salary: Stores the person's salary.

# ✨ Functionalities:
# Add the following methods:

# display_info(): Print name and age (access public and protected).

# set_salary(salary): Set the private salary if it's a positive number.

# get_salary(): Return the private salary.

# Try to access all three variables from outside the class and observe the behavior.

# class Person:
#     def __init__(self, name, age, salary):
#         self.name = name #public
#         self._age = age #protected
#         self.__salary = salary #private

#     def display_info(self):
#         print(f"Name: {self.name}| Age: {self._age}")

#     def set_salary(self, salary):
#         if salary > 0:
#             self.__salary = salary

#     def get_salary(self):
#         return self.__salary

# p1 = Person('Amber', 45, 50000)
# p1.display_info() 
# p1.set_salary(10000)
# print(p1.get_salary()) 
# print(p1.name)
# print(p1._age)
# print(p1._Person__salary) #You can access private attributes via the name-mangled form _ClassName__attribute, but this breaks encapsulation and should be avoided.


# Abstraction kya hai?
# Abstraction ka matlab hai "fuzool cheezen chhupa kar sirf zaroori cheezen dikhana" ya "complexity ko chhupa kar asaani se use karna".

# Programming mein, abstraction ka matlab hota hai ke hum apne program ke aise parts ko design karte hain jahan hum sirf essential details ko expose karte hain aur baki complex cheezen chhupa kar rakhtay hain.

# 🧱 Syntax of Abstraction in Python:

# from abc import ABC, abstractmethod  # ABC module import karo

# class MyClass(ABC):  # Abstract base class
#     @abstractmethod
#     def my_method(self):  # Abstract method
#         pass


#  Points to Remember (Zaroor Yaad Rakhein):
# 🔹 ABC se class ko abstract banate hain (inherit karo).

# 🔹 @abstractmethod use karo har method par jo abstract hoga.

# 🔹 Abstract class ka object direct nahi ban sakta.

# 🔹 Har child class ko abstract method implement karna zaroori hai.

# 🔹 Agar kisi child class ne abstract method implement nahi kiya to error ayega.

# 🔹 Abstraction real-life examples jese Payment, Animal, Vehicle, etc. mein useful hai.

# 🔹 Abstract classes aur interfaces reuse aur maintainable code mein help karti hain.


# Practice 🎯 Task:
# Ek abstract class Animal banayein jisme make_sound() method ho. Do child classes Dog aur Cat banayein jo make_sound() ko implement karen.

# from abc import ABC, abstractmethod

# class Animal(ABC):
    
#     @abstractmethod
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         print("Dog says whoof whoof!")

# class Cat(Animal):
#     def make_sound(self):
#         print("Cat says meow meow!")
# dog = Dog() #🔹 Abstract class ka object direct nahi ban sakta.
# dog.make_sound()
# cat = Cat()
# cat.make_sound()

# 🎯 Task:
# Ek abstract class Shape banayein jisme method ho area(). Do child classes banayein: Circle aur Square.


# from abc import ABC, abstractmethod

# class Shape(ABC):

#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2   # formula Area = πr2


# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side ** 2

# circle = Circle(5)
# print(circle.area())

# square = Square(4)
# print(square.area())   

# 🧠 Exercise 3: Payment Gateway
# 🎯 Task:
# Abstract class Payment banayein jisme method pay(amount) ho. Fir JazzCash, EasyPaisa, aur BankTransfer naam ki teen child classes banayein jin mein ye method implement ho.

# 💡 Hint:
# Har class mein print karwayein: "<method> se <amount> rupees pay hua."
            
# from abc import ABC, abstractmethod

# class Payment(ABC):

#     @abstractmethod
#     def pay(self, amount):
#         pass

# class JazzCash(Payment):
#     def pay(self, amount):
#         print(f"JazzCash se {amount} rupees pay hua.")

# class EasyPaisa(Payment):

#      def pay(self, amount):
#         print(f"EasyPaisa se {amount} rupees pay hua.")

# class BankTransfer(Payment):
#     def pay(self, amount):
#         print(f"BankTransfer se {amount} rupees pay hua.")

# jazz = JazzCash()
# jazz.pay(1000)

# easy = EasyPaisa()
# easy.pay(2000)

# bank = BankTransfer()
# bank.pay(3000)

# 🔶 Polymorphism kya hota hai?


# Polymorphism ka matlab hota hai "bohat si shapes lena". Programming mein iska matlab hai ke ek function ya method ka behavior object ke type ke mutabiq badal jaye.

# Yaane ke same naam ka function ya method, lekin alag-alag tarike se kaam karta hai depending on object.

# class Cat:
#     def speak(self):
#         return "Meow"

# class Dog:
#     def speak(self):
#         return "Bark"

# def animal_sound(animal):
#     print(animal.speak())

# c = Cat()
# d = Dog()

# animal_sound(c)  # Output: Meow
# animal_sound(d)  # Output: Bark


# Decorators

# Python Decorators kya hain?
# Decorators aik special tarah ka function hota hai jo doosre function ki functionality ko modify ya extend kar sakta hai bina asal function ke code ko badle.

# Samajhne ke liye yeh socho:

# Tumhare paas ek function hai, jise tum call karte ho.

# Ab tum chahte ho ke function ke kaam se pehle ya baad mein kuch extra cheez ho jaye, magar asal function ko change nahi karna.

# Yeh kaam decorators karte hain.

# Decorators kyu use karte hain?
# Code ko reuse karne ke liye

# Functionality ko bina original function badle extend karne ke liye

# Jaise logging, timing, authorization, debugging, etc.

# 🔹 Decorators in Class — Simple Explanation
# Python mein decorator ek function hota hai jo kisi aur function ya method ka behavior badalne ke liye use hota hai — bina uska code change kiye.

# Aap decorators functions ke sath bhi use karte ho aur classes ke andar methods ke sath bhi.

# 🔸 Common Decorators in Classes
# @staticmethod

# @classmethod

# @property

#  1. @staticmethod
# Yeh method class ke sath related hota hai, lekin self ya cls nahi leta. Isay object banaye bagair bhi call kiya ja sakta hai.

# class Math:
#     @staticmethod
#     def add(x, y):
#         return x + y

# print(Math.add(2, 3))  # Output: 5


# ✅ 2. @classmethod
# Yeh method cls parameter leta hai, jo class ko represent karta hai. Isay class ya object dono se call kiya ja sakta hai.

# class Person:
#     count = 0

#     def __init__(self):
#         Person.count += 1

#     @classmethod
#     def how_many(cls):
#         return f"{cls.count} persons created"

# p1 = Person()
# p2 = Person()

# print(Person.how_many())  # Output: 2 persons created

# ✅ 3. @property
# Is decorator ka use kisi method ko property ki tarah access karne ke liye hota hai.

# class Circle:
#     def __init__(self, radius):
#         self._radius = radius

#     @property
#     def area(self):
#         return 3.14 * self._radius * self._radius

# c = Circle(5)
# print(c.area)  # Output: 78.5


# Decorator         	Purpose

# @staticmethod	    Method jo self/cls use nahi karta
# @classmethod	    Method jo class (cls) ko use karta hai
# @property	        Method ko property jaisa behave karwana



# def decorator(func):
#     def wrapper():
#         print("before function call")
#         func()
#         print("after function call")
#     return wrapper

# class CheckDecorator:
#     @decorator
#     def my_function():
#         print("hello world")

# CheckDecorator.my_function()



# def upper_case_decorator(function):
#     def wrapper():
#         result = function()
#         return result.upper()
#     return wrapper

# @upper_case_decorator
# def greet():
#     return "hello world"

# print(greet())
