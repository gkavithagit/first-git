# ---- LIST ----
persons = ["kavi", "priya", "ravi"]

# -----EMPTY LIST -----
shopping = []
shopping.append("milk")
shopping.append("curd")
shopping.append("brush")
print(shopping)

# ----- LIST INDEXING -----
person = ["kavi", "priya", "ravi", "deva"]
print(person[3])

# ----- NEGATIVE INDEXING -----
fruits = ["apple", "banana", "mango"]
print(fruits[-1])

# -----CHANGING AN ITEM -----
notes = ["ruled", "unruled", "four lines"]
notes[2] = "two lines"
print(notes)

# ----- REMOVING ITEMS -----
person = ["kavi", "priya", "madhu"]
person.remove("priya")
print(person)

person = ["kavi", "priya", "ravi"]
person.pop(2)
print(person)

# ----- FINDING LENGTH -----
fruits = ["apple", "orange", "mango"]
print(len(fruits))

# ----- LOOPING THROUGH A LIST -----
school = ["teacher", "student", "classes"]
for school in fruits:
    print(school)

# ----- SORTING A LIST -----
numbers = [50,20,30,10,40]
numbers.sort()
print(numbers)

# ----- REVERSING A LIST -----
numbers = [10,20,30,40,50]
numbers.reverse()
print(numbers)

# ----- SLICING A LIST -----
numbers =[10,20,30,40,50]
print(numbers[1:3])

# ----- NESTED LISTS -----
students = [
    ["kavi", 20],
    ["priya", 19],
    ["ravi", 18]
]

