""" 
    Lambda Function declaration with single argument
    The job of this function is find square of any
    given number
"""
square = lambda x: x * x
# Funtion call
print("Square : " + str(square(8)))

""" Lambda Function declaration with multiple arguments """
add = lambda a, b: a + b
# Funtion call
print("Addition : " + str(add(3, 8)))
