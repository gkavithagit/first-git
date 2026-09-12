# ----- Sets part 2 -----
# ----- Update() -----

numbers = {10,20,30}
numbers.update([40,50,60])
print(numbers)

# ----- Remove() -----

numbers = {10,20,30,40}
numbers.remove(20)
print(numbers)

# ----- Clear() -----

numbers = {10,20,30}
numbers.clear()
print(numbers)

# ----- Len() -----

numbers = {10,20,30,40}
print(len(numbers))

# ----- Set Operations part 2 -----
# ----- Subset -----

A= {1,2}
B = {1,2,3,4,}
print(A.issubset(B))

# ----- superset -----

A = {1,2}
B = {1,2,3,4}
print(B.issuperset(A))

# ----- 'In' check if an item exists -----

numbers = {10,20,30,40}
print( 20 in numbers )

# ----- 'Not in' -----

numbers = {10,20,30,40}
print(50 not in numbers)

# ----- Common coding pattern -----

numbers = [10,20,10,30,20,40]
unique_numbers = set(numbers)
print(unique_numbers)

