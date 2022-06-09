# Looping Statements
# 1) FOR LOOP
# 2) WHILE LOOP
# [0-9]

for i in range(10):
    print("Welcome to my channel")

# Syntax
# while condition:
#       statement

number = 1
while number <= 10:
    print(f"3 X {number} = {number * 3}")
    number += 1
else:
    print("Number value is ", number)

print("Terminated")


# For loop example
shopping_list = ["Milk", "Bread", "Apple", "Jam"]

for item in shopping_list:
    if item == "Honey":
        print("Honey is available")
