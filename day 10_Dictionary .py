# ----- Dictionary basics -----
student = {
    "name" : "kavi",
    "age" : 20,
    "course" : "Bsc cs"
}

# ----- Different from list -----
marks = {
    "python" : 80,
    "DBMS" : 75,
    "CN" : 90,
}
print(marks["CN"])

# -----Adding new data -----
student = {
    "name" : "kavi",
    "age" : 20,
}
student["college"] = "ABC College"
print(student)

# ----- Chaning exiting data -----
student = {
    "name" : "kavi",
    "age" : 20
}
student["age"] = 21

# ----- Deleting data -----
student = {
    "name" : "kavi",
    "age" : 20,
    "course" : "Bsc CS"
}
del student["course"]

# ----- Dictionary methods -----
# ----- 1 Keys() -----
print(student.keys())

# ----- 2 Values() -----
print(student.values())

# ----- 3 Items() -----
print(student.items())

# ----- Dictionary with for loop -----
marks = {
    "python" : 85,
    "DBMS" : 78,
    "CN" : 80
}
for subject in marks:
    print(subject)

# ----- Dictionary inside dictionary -----
student = {
    "student1" :{
        "name" : "kavi",
        "age" : 20
    },
    "student2" :{
        "name" : "anu",
        "age" : 21
    }
}
