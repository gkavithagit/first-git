# ----- Function with NO parameters -----
def welcome():
    print("Welcome to python")
welcome()

# ----- Function with parameters -----
def welcome(name):
    print("welcome", name)
welcome("kavi")

# ----- Function withh parametes + return -----
def multiply(a,b):
    return a * b
result = multiply(5,4)
print(result)

# ----- Multiple return values -----
def calculator(a,b):
    return a + b, a - b
result1, result2 = calculator(10, 5)
print(result1)
print(result2)

# ----- Key arguments -----
def student(name, age):
    print(name, age)
student("kavi", 20)

# ----- Global variables -----
x = 10
def test():
    print(x)
test()



