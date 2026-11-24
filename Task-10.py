#1

class Car:

    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self):
        self.speed = self.speed + 10
        print("Speed after acceleration:", self.speed)

    def brake(self):
        self.speed = self.speed - 10
        if self.speed < 0:
            self.speed = 0
        print("Speed after braking:", self.speed)


car1 = Car("Eeco","BMW", 50)

print(car1.brand)
print(car1.model)

car1.accelerate()
car1.brake()


#2

class BankAccount:

  def __init__(self, balance):
    self.balance = balance

  def deposit(self , amount):
     self.balance = self.balance + amount
     print("Deposited: ", amount)

  def withdraw(self , amount):
    if amount <= self.balance:
        self.balance = self.balance - amount
        print("Withdraw: ", amount)
    else:
        print("Insufficient balance!")

  def display(self):
     print("Balance: ", self.balance)

account = BankAccount(5000)

account.deposit(2000)
account.withdraw(1000)
account.display()


     
#3

class Student:

    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        avg = (self.m1 + self.m2 + self.m3) / 3
        print("Average marks:", avg)


s1 = Student("Harshada", 80, 90, 85)

print("Student name:", s1.name)
s1.average()


#4

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area:", self.length * self.width)

    def perimeter(self):
        print("Perimeter:", 2 * (self.length + self.width))


r1 = Rectangle(10, 5)

r1.area()
r1.perimeter()


#5
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee Name:", self.name)
        print("Monthly Salary:", self.salary)
        print("Annual Salary:", self.salary * 12)


e1 = Employee("Harshada", 25000)

e1.display()


#6


class Book:

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


b1 = Book("Python Basics", "John", 500)

b1.display()



#7


import math

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area:", math.pi * self.radius ** 2)

    def circumference(self):
        print("Circumference:", 2 * math.pi * self.radius)


c1 = Circle(5)

c1.area()
c1.circumference()


#8


class Laptop:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def discount(self, percentage):
        discount_amount = self.price * percentage / 100
        final_price = self.price - discount_amount

        print("Brand:", self.brand)
        print("Original Price:", self.price)
        print("Discount:", discount_amount)
        print("Final Price:", final_price)


l1 = Laptop("HP", 50000)

l1.discount(10)


#9

class Flight:

    def __init__(self, total_seats):
        self.total_seats = total_seats
        self.booked_seats = 0

    def book_seat(self):
        if self.booked_seats < self.total_seats:
            self.booked_seats += 1
            print("Seat booked successfully")
        else:
            print("No seats available")

    def display(self):
        print("Total seats:", self.total_seats)
        print("Booked seats:", self.booked_seats)
        print("Available seats:", self.total_seats - self.booked_seats)


f1 = Flight(3)

f1.book_seat()
f1.book_seat()
f1.display()



#10

class Shop:

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(product, "added successfully")

    def list_products(self):
        print("Available Products:")

        for product in self.products:
            print(product)


shop1 = Shop()

shop1.add_product("Laptop")
shop1.add_product("Mobile")
shop1.add_product("Keyboard")

shop1.list_products()