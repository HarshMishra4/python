# Python List Comprehension
# Manual way 
mylist = [1, 2, 3, 4, 5]
print("Old List", mylist)

# =================================================
# ====[ General Approch for creating new List ]====
# =================================================
new_list = []
for i in range(1, 6):
  new_list.append(i)

# =================================================
# ==[ List Comprehension to generate a new List ]===
# =================================================
new_list = [i for i in mylist if (i % 2) != 0]
print("New List", new_list)

