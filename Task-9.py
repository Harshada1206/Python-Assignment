#1

try:
    a = 10
    b = 0
    result = a / b

    print(result)
except ZeroDivisionError:
    print("Cannot divied by zero")


#2

try:
    num = int(input("Enter a number: "))

    print("Number = ",num)

except ValueError:
    print("Please enter a valid interger..")


#3

try:
    with open(r"C:\Users\Harshada bagul\sample.txt", "r") as file:
        content = file.read()

        print(content)

except FileNotFoundError:
    print("File not found..")


#4

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second  number: "))
    result = num1 / num2

    print("Result =" , result)

except ValueError:
    print("please enter values only..")

except ZeroDivisionError:
    print("Connot divided by zero..")

except Exception:
    print("Something wet wrong..")


#5

try:
    file = open(r"C:\Users\Harshada bagul\sample.txt", "r") 
    content = file.read()

    print(content)

except FileNotFoundError:
    print("File not found..")
finally:
    print("program completed..")


#6

class InvalidAgeError(Exception):
    pass
try:
    age = int(input("Enter you age: "))

    if age  < 18:
        raise InvalidAgeError("Age must be 18 or above 18..")
    print("You are eligible")

except ValueError:
    print("Enter valid age..")
except InvalidAgeError as e:
    print(e)


#7

numbers = [10, 20 ,30 ,40 ,50]

try:
    print(numbers[5])

except IndexError:
    print("Index is out of range..")


#8

try:
    a = int(input("Enter first number :" ))
    b = int(input("Enter second number: "))
    result = a / b

    print(result)

except ValueError:
    print("Invalid input!!!!!Enter only number..")

except ZeroDivisionError:
    print("Cannot divided by zero....")

except Exception as e:
    print("Error..", e)

finally:
    print("Program finished...")


#9

import logging

logging.basicConfig(
    filename = "error.log" ,
    level = logging.ERROR
)

try:
    a = 10 
    b = 4

    result = a / b

except Exception as e:
    print("Error occured: %s",e)

print("Check error.log file")



#10

import re

try:
    email = input("Enter your email: ")

    pattern = r'^[\w.-]+@[\w.-]+\.\w+$'

    if not re.match(pattern , email):
      raise ValueError("Invalid emial address...")

    print("Invalid email address")

except ValueError as e:
    print(e)