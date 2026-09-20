# ----- OOP(Object-oriented programming) -----

class student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def study(self):
        print(self.name, "is studying")

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

student1 = student("Kavi", 19, "BSc Computer Science")

student1.display_info()
student1.study()