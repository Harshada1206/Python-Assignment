

#1

import mymath

print("Addition: ", mymath.add(12,6))
print("Multiplication: ", mymath.multiply(2,10))

#2

import string
name = "Harshada"

print("Uppercase: ", string.uppercase(name))
print("Lowercase: ", string.lowercase(name))
print("Reverse: ", string.reverse(name))


#3

import random

for i in range(5):
    num = random.randint(1 , 100)
    print(num)

#4

import datetime
now = datetime.datetime.now()
print("Current date : ",now.date())
print("Current time: ",now.time())

#5

import math

num = int(input("Enter a number: "))

result = math.factorial(num)

print("Factorial:", result)


#6

from shapes import circle,rectangle
print("Circle area: ",circle.area(5))
print("Rectangle area: ",rectangle.area(10,5))


#7

from calculator import add,subtract,multiply
print("Addition: ",add(10,10))
print("Subtraction: ",subtract(10,5))
print("multiplication: ",multiply(2,5))


#8

import random 
numbers = [ 1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffle lists: ", numbers)


#9

from datetime import date
date1  = date(2026 , 1, 1)
date2 = date(2026, 11, 2)
difference = date2 - date1
print("Difference: ",difference.days, "days")


#10

import os

files = os.listdir(".")

print("Files in directory:")

for file in files:
    print(file)