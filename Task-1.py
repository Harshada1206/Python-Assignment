#1.

print( " My name is Harshada,my age is 19,I live in Valsad." )

#2

a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
print("Sum of two number=", a + b)

#3

c = float(input("Enter temperature in celsius: "))
f = (c* 9/5)+32
print("Fahrenheit =", f)

#4

name="harshada"
print("Upper case :",name.upper())

#5

birth_year=int(input("Enter your birth year :"))
current_year= 2026
age = current_year - birth_year
print("your age is :", age)

#6

a=20
b=10
print("Before swapping: a=", a, "b=", b)
a, b=b , a
print("After swapping: a=", a ,"b=", b)

#7

length = float(input("Enter length: "))
breadth = float(input("Enter breadth"))
area = length * breadth
print("Area of Rectangle =",area)

#8

num = int(input("Enter a number: "))
if num > 0:
    print("Positive number.")
elif num < 0:
    print("Negative number:")
else:
    print("zero")

#9

a= float(input("Enter first number: "))
b = float(input("Enter second number: "))
average =(a+b) / 2
print("Average =", average)


print ("All nine programs executed successfully....")

