#1

text = input("Enter your string:")
print("Length= ",len(text))

#2

text = input("Enter your text:")
print(text.lower())

#3

text = input("Enter your text:")
print(text.replace(" ","_"))

#4

text = input("Enter a word:")

print("First character: ",text[0])
print("Last character: ",text[-1])

#5

text = input("Enter your string:")
print("Reverse: ", text[::-1])

#6

text = input("Enter your word: ")
letter = input("Enter your letter: ")
print("Count: ", text.count(letter))

#7

sentence = input("Enter your sentence: ")
word = input("Enter your word: ")
if word in sentence:
    print("word is present..")
else:
    print("word is not present..")

#8

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f" my name is {name} and my age is {age}")

#9

text = input("Enter your sentence: ")
print(text.strip())

#10

words = ["hello","python","world"]
result = "-".join(words)
print(result)

#part-2

#11

movies = ["ddlj","student of the year","chennai express","kkkg","tmkoc"]
print(movies)

#12

movies=["kkkg","chennai express","tmkoc"]
movies.append("dangal")
print(movies)

#13

movies = ["ddlj","student of the year","chennai express","kkkg","tmkoc"]
movies.pop(0)
print(movies)

#14

numbers = [40, 50, 67, 30, 23,90]
numbers.sort()
print(numbers)

#15

numbers = [10,30,58,1,24,23,2]
numbers.reverse()
print(numbers)

#16

numbers = [10, 20, 90, 87, 67, 50, 98, 21]
print("Largest numbers: ", max(numbers))

#17

list1 = [10,20,30]
list2 = [30,40,50]
list3 = list1 + list2
print(list3)

#18
numbers = [10,20,40,30,50]
print(numbers[-1])

#19

numbers = [[10, 20], [30, 40], [50, 60]]
print(numbers[1][0])

#20

numbers = [10, 20, 10, 30, 10, 40]
print("Count:", numbers.count(10))


