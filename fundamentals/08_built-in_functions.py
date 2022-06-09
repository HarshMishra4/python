# 1 Print
print("Hello world", end=', ')
print("2 Hello world ")

# 2. Type
a = ['2', 'A']
print(type(a))

# # 3. Input
number = int(input("Enter a number : "))
print("OP: ", (number * 2))

# 4.Round
num = 89.48902
print(round(num))

# 5. pow
num = 2
print(pow(num, 3))

# 6. Dir
data = [1, 'A', 'Milk', 4.9]
print(dir(data))

# 7. Sorted
numbers = [3, 54, 6, 8, 99, 98]
print(sorted(numbers, reverse=True))

# 8. max and min
numbers = [3, 54, 6, 8, 99, 98]
print(f"Maximum : {max(numbers)}")
print(f"Minimum : {min(numbers)}")

# 9. Divmod
print(divmod(24, 2))

# 10. len
numbers = [3, 54, 6, 8, 99, 98]
a = "dwjekhrfwejrfew"
print(len(a))

# 11. Sum
numbers = [1, 2, 3, 4, 5, 6]
print(sum(numbers))

# 12. help
help(print)

# 13. Range
for number in range(2, 11, 2):
    print(number)
