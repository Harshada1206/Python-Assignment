#1

number = (1,2,3,4,5)
print(number)

#2

numbers = (5,10,15,20,25)
print(numbers[2])

#3

student = ("Harshada",20,"Valsad")
name , age , city = student
print(name)
print(age)
print(city)


#4

fruits = {"mango" , "grapes" , "watermelon" , "apple" , "orange"}
print(fruits)


#5

fruits = {"mango" , "grapes" , "apple"}
fruits.add("watermelon")
print(fruits)


#6

fruits = {"mango" , "grapes" , "apple"}
fruits.remove("grapes")
print(fruits)


#7

A = {10, 20 , 30}
B = {30, 40, 50}
print(A.union(B))


#8

A = {10, 20 , 30}
B = {30, 40, 50}
print(A.intersection(B))


#9

A= {1,2,3,4,5}
B={1,2,3,4,5,6,7,8,9,10}
print(A.issubset(B))


#10

numbers = [10,20,30,10,40,20,50,30]
unique_numbers = set(numbers)
print(unique_numbers)


#11

students = {
    "Harshada" : 75,
    "Riya" : 80,
    "mahi" : 90
}
print(students)


#12

student = {
    "name": "Harshada",
    "marks": 85
}

student["city"] = "Valsad"

print(student)

#13

student = {
    "name" : "harshada",
    "age" : 20 ,
    "city " : "valsad"
}
del student["city "]
print(student)

#14

A = {"name": "Harshada", "age": 20}
B = {"city": "valsad", "marks": 85}

A.update(B)

print(A)


#15

student = {
    "name": "Harshada",
    "marks": 85
}

if "name" in student:
    print("Key exists")
else:
    print("Key does not exist")

#16

sentence = "apple banana apple mango banana apple"

words = sentence.split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)

#17

marks = {
    "Harshada": 85,
    "Riya": 90,
    "liya": 78
}

maximum = max(marks, key=marks.get)

print(maximum)


#18

student = {
    "name": "Harshada",
    "city": "valsad"
}

reversed_dict = {value: key for key, value in student.items()}

print(reversed_dict)


#19

student = {
    "name": "Harshada",
    "marks": 75
}

student["marks"] = 90

print(student)


#20

students = [
    ("Harshada", 85),
    ("Riya", 90),
    ("Mahi", 77)
]

student_dict = dict(students)

print(student_dict)