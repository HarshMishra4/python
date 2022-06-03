# ===========================================
# importing our custom module defined module
# ===========================================
# import helper                      # 1 way of import
# import helper as h                 # 2nd way of import by setting an alias
from helper import isNegetive, User  # 3rd way importin only required functions & classes
# ==========================
# importing Built-in module
# ==========================
from math import sqrt

# Check's whether the is given number is +ve or -ve
print(isNegetive(-90))

# User class belongs to helper module
user = User("Rohan", 21)
user.detail()

# sqrt function belongs to python's [ math ] module
print(sqrt(4096))
print(sqrt(25))