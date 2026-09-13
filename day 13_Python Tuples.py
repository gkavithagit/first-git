# ----- Python Tuples -----

# ----- Example -----
numbers = (10,20,30,40)
students = ("kavi", 20, 7.5, True)

# ----- Tuple indexing -----

fruits = ("apple", "banana", "mango")
print(fruits[0])

# ----- Tuple slicing -----

numbers = (10,20,30,40,50)
print(numbers[1:4])

# ----- Creating an empty tuple ----- 

empty = ()
print(empty)

# ----- Tuples allow duplicates -----

numbers = (10,20,20,30,10)
print(numbers)

# ----- Tuple store different datatypes -----

student = (
    "kavi",
    20,
    7.5,
    True
)

# ----- Tuple methods -----
# ----- Count() -----

numbers = (10,20,20,30,20)
print(numbers.count(20))

# ----- Index() -----

numbers = (10,20,30,40)
print(numbers.index(30))

# ----- Len() -----

students = ("Kavi", "Anu", "Priya")
print(len(students))

# ----- Looping through a tuple -----

fruits = ("apple", "banana", "mango")
for fruit in fruits:
    print(fruits)

# ----- Checking an item exists -----
# ----- Use in -----

fruits = ("apple", "banana", "mango")
print("banana" in fruits)

# ----- Converting list to tuple -----

numbers = [10,20,30,40]
numbers_tuple = tuple(numbers)
print(numbers_tuple)

# ----- Common coding patterns -----

numbers = [10,20,20,30,30,40]
unique_numbers = tuple(set(numbers))
print(unique_numbers)
