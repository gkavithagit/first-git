# ----- Python set -----

# ----- Creating a set -----
numbers = {10,20,30,40}
print(numbers)

# ----- Duplicate values -----
numbers = {10,20,20,30,30}
print(numbers)

# ----- Adding an item -----
numbers.add(50)
print(numbers)

# ----- Removing an item -----
numbers.remove(20)
print(numbers)

# ----- Set operations -----
A = {1,2,3,4}
B = {3,4,5,6}

print("Union:", A|B)
print("Intersection:", A&B)
print("Difference:", A-B)

# ----- My practice ------
students = ["kavi", "anu", "kavi", "priya", "anu"]
unique_students = set(students)
print(unique_students)