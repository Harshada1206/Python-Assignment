#1

for i in range(1,11):
  print(i)


#2

num = int(input("Enter a number: "))

for i in range(1,11):
  print(num,"x",i,"=",num * i)

#3

num = int(input("Enter a number: "))
fact = 1

for i in range(1 , num+1 ):
  fact = fact * i
print("Factorial= ", fact)

#4

n = int(input("Enter how many number: "))
a = 0
b = 1
for i in range(n):
  print(i)
  c = a + b
  a = b
  b = c

#5

num = int(input("enter a number: "))
count = 0

for i in range(1, num + 1):
  if num % 1 == 0:
    count = count +1
    if count == 2:
      print("Prime number..")
    else:
      print("not a prime number..")

#6

num = int(input("Enter a number: "))
rev = 0

while num > 0:
  digit = num % 10
  rev = rev * 10 + digit
  num = num // 10
print("Reverse= ", rev)

#7

num = int(input("enter a number: "))
count = 0

while num > 0:
 num = num//10
 count = count + 1
print("Total Digits= ", count)

#8

total = 0
for i in range(1,101):
  if i % 2 ==0:
    total =  total + i
print("Sum of even numbers=", total)

#9

n = 5
for i in range( 1 , n + 1):
  print( "*" * i)

#10

num = int(input("Enter a number: "))
print("divisors are:")
for i in range(1, num +1):
  if num % 1 == 0:
    print(i)


