# Day 9 Mini Project
# Personal Expense Tracker
expenses = []
n = int(input("How many expenses do you want to enter?"))
for i in range(n):
    expense = float(input(f"Enter expense {i + 1}: Rs"))
    expenses.append(expense)
def calculate_total(expenses):
    return sum(expenses)
def find_highest(expenses):
    return max(expenses)
def find_lowest(expenses):
    return min(expenses)
def calculate_average(expenses):
    return sum(expenses) / len(expenses)
total = calculate_total(expenses)
highest = find_highest(expenses)
lowest = find_lowest(expenses)
average = calculate_average(expenses)
print("\n----- EXPENSE REPORT -----")
print("Expenses:", expenses)
print("Total expenses: Rs", total)
print("Highest expense: Rs", highest)
print("Lowest expenses: Rs", lowest)
print("Average expense: Rs", round(average, 2))

