def total(a,b,c):
    return a + b + c

def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    return "Fail"

a = int(input("python: "))
b = int(input("DBMS: "))
c = int(input("Networking: "))

t = total(a,b,c)
avg = t / 3

print("Total:", t)
print("Average:", avg)
print("Grade:", grade(avg))
print("Result:", "Pass" if a >= 40 and b >= 40 and c >= 40 else "Fail")