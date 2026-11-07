# Q31. Dictionary Access

student = {
    "name": "Ali",
    "age": 22,
    "course": "Python",
    "marks": 85
}

name = student["name"]
marks = student["marks"]
city = student.get("city", "Karachi")

print("Q31 Name:", name)
print("Marks:", marks)
print("City:", city)


# Q32. Update Dictionary

employee = {
    "name": "Sara",
    "salary": 100000,
    "department": "IT"
}

employee["salary"] = employee["salary"] * 1.20
employee["bonus"] = 15000
employee["department"] = "Data Engineering"

print("Q32:", employee)


# Q33. Dictionary Methods

product = {
    "id": 101,
    "name": "Laptop",
    "price": 120000,
    "stock": 5
}

keys = product.keys()
values = product.values()
items = product.items()
removed_stock = product.pop("stock")

print("Q33 Keys:", keys)
print("Values:", values)
print("Items:", items)
print("Removed Stock:", removed_stock)
print("Updated Product:", product)


# Q34. Merge Dictionaries

dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 50, "d": 40}

merged = dict1 | dict2

print("Q34:", merged)


# Q35. Student Marks

marks = {
    "Ali": 85,
    "Sara": 92,
    "Ahmed": 78,
    "Zain": 88
}

highest = max(marks.values())
lowest = min(marks.values())
average = sum(marks.values()) / len(marks)
top_student = max(marks, key=marks.get)

print("Q35 Highest:", highest)
print("Lowest:", lowest)
print("Average:", average)
print("Top Student:", top_student)


# Q36. Nested Employee Records

employees = {
    "E101": {"name": "Ali", "salary": 80000},
    "E102": {"name": "Sara", "salary": 120000},
    "E103": {"name": "Ahmed", "salary": 95000}
}

sara_salary = employees["E102"]["salary"]

employees["E101"]["salary"] = employees["E101"]["salary"] * 1.15

total_payroll = (
    employees["E101"]["salary"]
    + employees["E102"]["salary"]
    + employees["E103"]["salary"]
)

print("Q36 Sara Salary:", sara_salary)
print("Ali Updated Salary:", employees["E101"]["salary"])
print("Total Payroll:", total_payroll)


# Q37. Dictionary Inversion

data = {
    "Python": "Ali",
    "SQL": "Sara",
    "AWS": "Ahmed"
}

inverse = {
    data["Python"]: "Python",
    data["SQL"]: "SQL",
    data["AWS"]: "AWS"
}

print("Q37:", inverse)


# Q38. Order Calculation

order = {
    "laptop": {"price": 120000, "quantity": 2},
    "mouse": {"price": 1500, "quantity": 5},
    "keyboard": {"price": 3500, "quantity": 3}
}

laptop_total = order["laptop"]["price"] * order["laptop"]["quantity"]
mouse_total = order["mouse"]["price"] * order["mouse"]["quantity"]
keyboard_total = order["keyboard"]["price"] * order["keyboard"]["quantity"]

grand_total = laptop_total + mouse_total + keyboard_total
discount = grand_total * 0.10
final_amount = grand_total - discount

print("Q38 Laptop Subtotal:", laptop_total)
print("Mouse Subtotal:", mouse_total)
print("Keyboard Subtotal:", keyboard_total)
print("Grand Total:", grand_total)
print("After 10% Discount:", final_amount)


# Q39. Employee Performance

employees = {
    "Ali": {"python": 90, "sql": 85, "aws": 88},
    "Sara": {"python": 95, "sql": 92, "aws": 90},
    "Ahmed": {"python": 80, "sql": 87, "aws": 84}
}

ali_average = (
    employees["Ali"]["python"]
    + employees["Ali"]["sql"]
    + employees["Ali"]["aws"]
) / 3

sara_average = (
    employees["Sara"]["python"]
    + employees["Sara"]["sql"]
    + employees["Sara"]["aws"]
) / 3

ahmed_average = (
    employees["Ahmed"]["python"]
    + employees["Ahmed"]["sql"]
    + employees["Ahmed"]["aws"]
) / 3

averages = {
    "Ali": ali_average,
    "Sara": sara_average,
    "Ahmed": ahmed_average
}

top_performer = max(averages, key=averages.get)

highest_sql = max(
    employees["Ali"]["sql"],
    employees["Sara"]["sql"],
    employees["Ahmed"]["sql"]
)

print("Q39 Ali Average:", ali_average)
print("Sara Average:", sara_average)
print("Ahmed Average:", ahmed_average)
print("Top Performer:", top_performer)
print("Highest SQL Score:", highest_sql)


# Q40. Inventory Management

inventory = {
    "P101": {"name": "Laptop", "price": 120000, "stock": 5},
    "P102": {"name": "Mouse", "price": 1500, "stock": 20},
    "P103": {"name": "Keyboard", "price": 3500, "stock": 10}
}

total_value = (
    inventory["P101"]["price"] * inventory["P101"]["stock"]
    + inventory["P102"]["price"] * inventory["P102"]["stock"]
    + inventory["P103"]["price"] * inventory["P103"]["stock"]
)

laptop_value = inventory["P101"]["price"] * inventory["P101"]["stock"]
mouse_value = inventory["P102"]["price"] * inventory["P102"]["stock"]
keyboard_value = inventory["P103"]["price"] * inventory["P103"]["stock"]

most_valuable = max(laptop_value, mouse_value, keyboard_value)

inventory["P101"]["stock"] -= 2
inventory["P102"]["stock"] -= 5

print("Q40 Total Inventory Value:", total_value)
print("Most Valuable Item Value:", most_valuable)
print("Updated Inventory:", inventory)
