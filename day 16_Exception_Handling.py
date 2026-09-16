# ----- Python - Exception Handling -----
# ----- Exception -----

age = int(input("Enter your age:"))
print(age)
try:
    age = int(input("Enter your age:"))
    print("Your age:", age)
except ValueError:
    print("Please enter a valid number.")

# ----- try and except -----

try:
    number = int(input("Enter a number:"))
except ValueError:
    print("Invalid input!")

# ----- Another example - Division -----

try:
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Please enter numbers only.")

# ----- Practice -----

try:
    number = int(input("Enter a number:"))
    print("You entered:", number)
except ValueError:
    print("Invalid input. Please enter a number.")

# ----- try + except + else -----

try:
    number = int(input("Enter a number:"))
except ValueError:
    print("Invalid input.")
else:
    print("valid number:", number)

# ----- else logic -----

try:
    number = int(input("Enter a number:"))
except ValueError:
    print("Invalid input.")
else:
    square = number * number
    print("Square:", square)

# ----- finally -----

try:
    number = int(input("Enter a number:"))
except ValueError:
    print("Invalid input.")
finally:
    print("Program completed.")

# ----- Complete simple code -----

try:
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    result = a / b
except ValueError:
    print("Please enter numbers only.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Result:", result)
finally:
    print("Calculation completed.")


