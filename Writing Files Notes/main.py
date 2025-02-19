#Vincent Johnson writing files notes
'''
How do you find a file in a folder? 
    Open the folder? Is it that hard???
In a python project how do you open a file?
    with open("File Name", "Type of opening") as file:
What is the difference between writing, appending, and creation modes?
    Writing destroys previous file, appending adds to file, reading cannot affect it
'''
import csv
import random

# w (Replaces content), w+ (Read and write), a (Append), r (Read), x (Create file), a+ (Append and read)
with open("Writing Files Notes/example.txt", "w") as file:
    file.write("Blah, blah, blah!")

with open("Writing Files Notes/example.txt", "w+") as file:
    file.write("I don't like thisssssss")
    print(file.read())

with open("Writing Files Notes/example.txt", "a") as file:
    file.write("\nMaybe it's because I just don't")

with open("Writing Files Notes/example.txt", "a+") as file:
    file.write("\nBut I don't know")
    print(file.read())

#with open ("Writing Files Notes/new.txt", "x") as file:
    #Figure out how to make new file
    #pass

with open("Writing Files Notes/example.txt", "r") as file:
    print(file.read())





with open("Writing Files Notes/test.csv", "w+", newline="") as file:
    b = 50
    c = 50
    writer = csv.writer(file)
    reader = csv.reader(file)
    for i in range(100):
        a = []
        while b > 0:
            a.append("Blah")
            b -= 1
        d = random.randint(-99, 100)
        if d > 0:
            d = 1
        else:
            d = -1
        c += d
        b = c
        writer.writerow(a)
    for row in reader:
        print(row)