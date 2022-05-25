# Simple Function
# def multiply(a, b):
#     return a * b

# result = multiply(3, 8, 9)
# print(result)




# # ==================================================
# # ================[  *args   ]======================
# # ==================================================

def multiply(*args):
    n = 1
    print(args[1])
    for i in args:
        n *= i
    return n

# print(multiply(4, 7, 5, 6, 9, 2))
print(multiply(4, 2, 3, 8, 9, 6, 2, 10))


# ==================================================
# =========[ Keyword arguments (**kwargs)]==========
# ==================================================
def combine(**kwargs):
    print(kwargs)
    return kwargs['name'] + ' ' + kwargs['lastname']

print(combine(name = 'Iron', lastname = 'Man'))