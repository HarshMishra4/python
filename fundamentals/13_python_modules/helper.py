class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def detail(self):
        # Display's the stored user details
        print("===========================")
        print(f'Username : {self.name}')
        print(f'Age : {self.age}')
        print("===========================")

# This function returns True if given number is a -ve number
# else it will return a False is number is +ve
def isNegetive(number):
    if number < 0:
        return True
    return False