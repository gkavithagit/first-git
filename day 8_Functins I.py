def greet():
    print("Hello kavi!")
greet()

def welcome(name):
    print("welcome", name)
welcome("kavi")
welcome("arun")
welcome("priya")

# ----- return -----
def add(a,b):
    return a + b
result = add(10,20)
print(result)

# ----- finding the square -----
def square(a):
    return a * a
result = square(2)
print(result)

# ----- finding even/odd -----
def is_even(a):
    return a % 2 == 0
result = is_even(10)
print(result)

# ----- Multiple parameters -----
def student(name, age, course):
    print(name)
    print(age)
    print(course)
student("kavi", 20, "BSc CS")

# ----- Default Arguments -----
def greet(name = "student"):
    print("hello", name)
greet("kavi")
greet()

# ----- Function + if/else -----
def check_age(age):
    if age >= 18:
        return "Eligible"
    else:
        return "Not eligible"
result = check_age(20)
print(result)

# ----- function calling another fuction -----
def square(number):
    return number * number
def double(number):
    return number * 2
result = double(square(3))
print(result)

# ----- Local variable -----
def test():
    x = 10
    print(x)
test()