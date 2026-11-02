#1

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
reminder = a % b
print("Reminder= ", reminder)

#2

num = int(input("Enter a number: "))
if num % 2 == 0:
   print("Even number..")
else:
   print("Odd number..")


#3

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
   print("Larger number =", a)
else:
   print("Larger number =", b)

#4

num = int(input("Enter a number: "))
square = num **2
cube = num **3
print("Square= ", square)
print("Cube= ", cube)

#5

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a == b:
   print("Both number are equals..")
else:
   print("Both number are not equals..")


#6

a = int(input("Enter first number: "))
b = int(input("Enter second nunmber: "))

result = a>0 and b>0

print(result)

#7

num = float(input("Enter a decimal number: "))
result = int(num)
print("Integer value: ", result)

#8

num = input("Enter a number: ")
result = int(num) * 10
print("Result= ", result)

#9

age = int(input("Enter the age: "))
if age >= 18 and age <= 60:
   print("eligible")
else:
   print("not eligible")   
if age < 18 or age > 60:
   print("Age is out of range")

#10

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

quotient = a // b
remainder = a % b

print("Quotient =", quotient)
print("Remainder =", remainder)
