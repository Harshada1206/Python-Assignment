#1

age = int(input("Enter the age: "))
if age >=18:
    print("Eligible for vote..")
else:
    print("not Eligible for vote..")

#2

marks = int(input("Enter you marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
else:
    print("Grade C")

#3

light = input("Enter taffic light color: ")

if light == "Red":
    print("Stoppp..")
elif light == "Yellow":
    print("Waitt..")
elif light == "Green":
    print("Goo..")
else:
    print("Invalid color..")

#4

balance = int(input("Enter your balance: "))
amount = int(input("Enter your withdrawal amount: "))

if amount <= balance:
    print("Withdrawal Successfull..")
else:
    print("Insufficient Balance..")

#5

num = int(input("Enter your number: "))
if num > 0:
    print("Positive number..")
elif num < 0:
    print("Negative number..")
else:
    print("Zero..")

#6

num = int(input("enter your number: "))

if num >= 10 and num <= 50:
    print("Number is between the range..")
else:
    print("Number is outside the range..")

#7

username = input("Enter Username:")
password = input("Enter password:")

if username == "admin" and password == "1234":
    print("Login successfull...")
else: 
    print("Invalid username and password..")

#8

units = int(input("Enter electircity units: "))
if units <=100:
    bill = units * 5
elif units <= 200:
    bills = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10

print("Electricity bill:", bill)

#9

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
operator = input("Enter operators(+,-,*,/):")
if operator == "+":
    print("addition:",a+b)
elif operator == "-":
    print("Subtraction:",a-b)
elif operator == "*":
    print ("Multiplication:", a*b)
elif operator == "/":
 if b != 0:
    print("Division:",a/b)
else:
    print("Invalid operator")

#10

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))
if a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle..")
elif a == b and b ==c:
    print("Equilateral triangle..")
elif a == b and b == c and a == c:
    print("Isoseles triangle..")
else:
    print("scalene triangle..")


