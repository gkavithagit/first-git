# ----- Python File handlings ----- 
# ----- Create and write to a file -----

file = open("student.txt", "w")
file.write("Name: Kavi\n")
file.write("Course: Bsc CS\n")
file.write("Skill: Python")

file.close()

print("Data written successfully")

# ----- Read the file -----

file = open("student.txt", "r")
data = file.read()
print(data)
file.close()

# ----- Append new information ------

file = open("student.txt", "a")
file.write("\nGoal: Placement")
file.close()
print("Data added successfully")

# ----- Read line by line -----

file = open("student.txt", "r")

print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

file.close()

# ----- with open() -----

with open("student.txt", "r") as file:
    data = file.read()
    print(data)



