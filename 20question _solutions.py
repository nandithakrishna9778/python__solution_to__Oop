#1. Student Class
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Student Name: {self.name}, Marks: {self.marks}")

student1 = Student("Alice", 92)
student1.display()


#2. Laptop Constructor
class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

laptop1 = Laptop("Dell", 1200)
print(f"Brand: {laptop1.brand}, Price: ${laptop1.price}")


#3. Rectangle Area
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

rect = Rectangle(10, 5)
print(f"Area of Rectangle: {rect.calculate_area()}")


#4. Employee Variables
class Employee:
    company_name = "Tech Corp"  # Class variable

    def __init__(self, employee_name):
        self.employee_name = employee_name  # Instance variable

emp1 = Employee("John")
emp2 = Employee("Sarah")

print(f"{emp1.employee_name} works at {Employee.company_name}")
print(f"{emp2.employee_name} works at {Employee.company_name}")


#5. Calculator Static Method
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

result = Calculator.add(5, 7)
print(f"Sum: {result}")

#6. Animal Method Overriding
class Animal:
    def sound(self):
        return "Some generic animal sound"

class Cat(Animal):
    def sound(self):  # Overriding the parent method
        return "Meow"

animal = Animal()
cat = Cat()
print(animal.sound())
print(cat.sound())


#7. Multilevel Inheritance
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

mgr = Manager("Alice", "E123", "IT")
print(f"Manager: {mgr.name}, ID: {mgr.emp_id}, Dept: {mgr.department}")


#8. Multiple Inheritance
class Father:
    def showFather(self):
        print("I am the Father.")

class Mother:
    def showMother(self):
        print("I am the Mother.")

class Child(Father, Mother):
    def showChild(self):
        print("I am the Child.")

child = Child()
child.showFather()
child.showMother()
child.showChild()

#9. BankAccount Override 
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if self.balance - amount < 100:  # Enforcing $100 minimum balance
            print("Withdrawal denied: Minimum balance of $100 required.")
        else:
            super().withdraw(amount)

acc = SavingsAccount(150)
acc.withdraw(100) # Denied
acc.withdraw(40)  # Allowed


#10.Private Variables
class Account:
    def __init__(self, initial_balance):
        self._balance = initial_balance  # Private/Protected variable

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited {amount}. New Balance: {self._balance}")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew {amount}. New Balance: {self._balance}")
        else:
            print("Insufficient funds.")

my_account = Account(500)
my_account.deposit(200)
my_account.withdraw(100)


#11. Polymorphism with Loop
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)

class Square:
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

shapes = [Circle(5), Square(4)]

for shape in shapes:
    print(f"Area of {type(shape).__name__}: {shape.area():.2f}")


#12. Abstract Classes
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Bike(Vehicle):
    def start(self):
        print("Bike starting with a kick...")

class Car(Vehicle):
    def start(self):
        print("Car starting with a key turn...")

bike = Bike()
car = Car()
bike.start()
car.start()


#13. Division by Zero
def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

divide_numbers(10, 2)
divide_numbers(10, 0)


#14. Invalid Input Handling
try:
    user_input = int(input("Enter a whole number: "))
    print(f"You entered: {user_input}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")


#15. Calculator Exceptions
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
    print(f"The result is {result}")
except ValueError:
    print("Error: Please input valid numeric values.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


#16. Finally Clause for Files
  file = None
try:
    file = open("sample.txt", "w")
    file.write("Hello, World!")
    print("Writing to file successful.")
except IOError:
    print("An error occurred while handling the file.")
finally:
    if file:
        file.close()
        print("File closed successfully.")


#17. Custom Exception 
class InsufficientBalanceError(Exception):
    pass

def make_withdrawal(balance, amount):
    try:
        if amount > balance:
            raise InsufficientBalanceError("Withdrawal exceeds current balance!")
        balance -= amount
        print(f"Transaction successful. Remaining balance: {balance}")
    except InsufficientBalanceError as e:
        print(f"Error: {e}")

make_withdrawal(100, 150)



#18. Voting Eligibility
def check_voting_eligibility(age):
    try:
        if age < 18:
            raise ValueError("You must be 18 or older to vote.")
        print("You are eligible to vote!")
    except ValueError as e:
        print(f"Exception: {e}")

check_voting_eligibility(20)
check_voting_eligibility(16)



#19. Index Errors 
my_list = ["Apple", "Banana", "Cherry"]

try:
    index = int(input("Enter an index (0-2) to fetch a fruit: "))
    print(f"Fruit at index {index} is {my_list[index]}")
except IndexError:
    print("Error: Index is out of range. Please choose a valid index.")
except ValueError:
    print("Error: Please enter an integer.")


#20. Try-Except-Else
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Division by zero error.")
    else:
        print(f"Division successful. Result is: {result}")

safe_divide(20, 4)
safe_divide(20, 0)


