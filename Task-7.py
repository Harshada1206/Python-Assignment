#1

def prime(num):
    if num <= 1:
        print("Not a prime number...")
    else:
      for i in range (2,num):
        if num % 1 == 0:
         print("not a prime number..")
         break
        else:
         print("prime number")
prime(7)


#2

def reverse_string(text):
  print(text[::-1])

reverse_string("harshada")

#3

def factorial(num):
  fact = 1
  for i in range(1,num+1):
    fact = fact * 1
    print("factorial = ", fact)
factorial(5)

#4

def simple_interest(p,r,t):
  si = (p*r*t) / 100
  print("Simple Intrest =",si)
simple_interest(1000,5,2)

#5

def palindrome(word):
  if word == word[::1]:
    print("Palindrome")
  else:
    print("Not Palindrome")

print("madam")

#6

def count_vowels(text):
  count = 0
  for ch in text:
    if ch.lower() in "aeiou":
      count = count + 1
    print("total vowels = ",ch)
count_vowels("Harshada")

#7

def merge_list(a,b):
  result = a + b
  print(result)
merge_list([1,2,3],[4,5,6])

#8

def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    print("GCD =", a)

gcd(12, 18)

#9

def rectangle(length, width):
    area = length * width
    print("Area of rectangle =", area)

rectangle(10, 5)

#10

def armstrong(num):
  original = num
  total = 0
  digits = len(str(num))

  while num > 0:
    digit = num % 10
    total = total + digit **digits
    num =  num // 10

    if total == original:
      print("Armstrong number..")
    else:
      print("Not Armstrong number..")

armstrong(153)
