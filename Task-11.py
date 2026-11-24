#1

class Animal:
    def eat(self):
        print("Animals can eat")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

d = Dog()
d.eat()
d.bark()

c = Cat()
c.eat()
c.meow()


#2

class Vehicle:
    def vehicle_type(self):
        print("This is a vehicle")

class Car(Vehicle):
    def car_type(self):
        print("This is a car")

class ElectricCar(Car):
    def electric(self):
        print("This is an electric car")

e = ElectricCar()

e.vehicle_type()
e.car_type()
e.electric()


#3

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

a = Animal()
a.sound()

d = Dog()
d.sound()


#4

class Father:
    def show_father(self):
        print("This is Father class")

class Mother:
    def show_mother(self):
        print("This is Mother class")

class Child(Father, Mother):
    def show_child(self):
        print("This is Child class")

c = Child()

c.show_father()
c.show_mother()
c.show_child()


#5

class Circle:
    def area(self):
        print("Area of Circle")

class Rectangle:
    def area(self):
        print("Area of Rectangle")

def calculate(shape):
    shape.area()

c = Circle()
r = Rectangle()

calculate(c)
calculate(r)



#6

class Bank:
    def account(self):
        print("Bank Account")

class SavingsAccount(Bank):
    def account(self):
        print("Savings Account")

class CurrentAccount(Bank):
    def account(self):
        print("Current Account")

s = SavingsAccount()
c = CurrentAccount()

s.account()
c.account()



#7

class Student:
    def __init__(self):
        self.__name = "Harshada"

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

s = Student()

print("Old Name:", s.get_name())

s.set_name("Riya")

print("New Name:", s.get_name())



#8

class Person:
    def display(self):
        print("This is a person")

class Teacher(Person):
    def teach(self):
        print("Teacher teaches students")

class Student(Person):
    def study(self):
        print("Student studies")

t = Teacher()
t.display()
t.teach()

s = Student()
s.display()
s.study()


#9

class MusicPlayer:
    def play(self):
        print("Playing music")

class Spotify(MusicPlayer):
    def play(self):
        print("Playing music on Spotify")

m = MusicPlayer()
m.play()

s = Spotify()
s.play()


#10

class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def show(self):
        super().show()
        print("This is Child class")

c = Child()
c.show()