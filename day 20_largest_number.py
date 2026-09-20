# ----- Problem Solving Practice -----
# ---- Largest number problem -----

numbers = [10,25,7,42,18]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number
print(largest)

# ----- Smallest number problem -----

numbers = [10,25,7,42,18]

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print(smallest)