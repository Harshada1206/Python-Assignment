
#1

with open(r"C:\Users\Harshada bagul\sample.txt", "r") as file:
    content = file.read()

    print(content)


#2

with open(r"C:\Users\Harshada bagul\sample.txt", "r") as file:
    lines = file.readlines()

    print("Total lines =", len(lines))


#3

with open(r"C:\Users\Harshada bagul\sample.txt", "r") as file:
    content = file.read()

    words = content.split()

    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    print(frequency)


#4

with open(r"C:\Users\Harshada bagul\sentence,txt", "w") as file:

    for i in range(5):
        sentence = input("Enter a sentence: ")
        file.write(sentence + "\n")

print("Sentences saved successfully!")

#5

sentences = [
    "I love Python",
    "Python is easy",
    "I am learning coding"
]

with open(r"C:\Users\Harshada bagul\sample.txt", "a") as file:

    for sentence in sentences:
        file.write(sentence + "\n")

print("Data added successfully!")

#6

word = input("Enter a word to search: ")

with open(r"C:\Users\Harshada bagul\sample.txt", "r") as file:

    for line in file:
        if word in line:
            print(line, end="")


#7

with open(r"C:\Users\Harshada bagul\sample.txt", "r") as file:
    content = file.read()

content = content.replace("Python", "Java")

with open(r"C:\Users\Harshada bagul\sample.txtt", "w") as file:
    file.write(content)

print("Word replaced successfully!")

#8

with open(r"C:\Users\Harshada bagul\file1.txt", "r") as file1:
    data1 = file1.read()

with open(r"C:\Users\Harshada bagul\file2.txt", "r") as file2:
    data2 = file2.read()

with open(r"C:\Users\Harshada bagul\file3.txt", "w") as file3:
    file3.write(data1 + "\n" + data2)

print("Files merged successfully!")

#9

import csv

with open(r"C:\Users\Harshada bagul\students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:
        print(" | ".join(row))


#10

with open(r"C:\Users\Harshada bagul\sample.txt", "r") as file:
    content = file.read()

with open(r"C:\Users\Harshada bagul\backup.txt", "w") as file:
    file.write(content)

print("Backup created successfully!")
