users = {
    '101': "John",
    '102': "Larry",
    '103': "Ben",
    '104': "Lisa",
}
numbers = [1, 2, 3, 4, 5, 6]
print('\n')

try:
    print(users['104'])
    print(numbers[7])
except (KeyError, IndexError):
    print("Error")
finally:
    print("HI!!!")

print("Program Executed\n")
