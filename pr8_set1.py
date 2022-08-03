#A new empty set
color_set = set()
color_set.add("Red")
print(color_set)
#Add multiple items
color_set.update(["Blue", "Green", "Black"])
print(color_set)
#remove item
color_set.discard("Black")
print(color_set)
