# ----- append() -----
fruits = ["apple","banana"]
fruits.append("mango")
print(fruits)

# ----- insert() -----
numbers = [10,20,40]
numbers.insert(2,30)
print(numbers)

# ----- extend() -----
a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)

# ------ remove() -----
numbers = [10,20,30,40]
numbers.pop(2)
print(numbers)

# ------ clear() ------
numbers = [10,20,30]
numbers.clear()
print(numbers)

# ------ index() -----
fruits = ["apple", "banana", "mango"]
print(fruits.index("banana"))

# ------ count() ------
numbers = [10,20,10,30,10]
print(numbers.count(10))

# ----- sort() -----
numbers = [5,2,1,3,4]
numbers.sort()
print(numbers)

# ----- reverse() -----
numbers = [3,1,5,2]
numbers.reverse()

# ----- len() -----
numbers = [10,20,30,40]
print(len(numbers))

# ----- sorted() -----
numbers = [5,2,8,1]
new_numbers = sorted(numbers)
print(numbers)
print(new_numbers)
