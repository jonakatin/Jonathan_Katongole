
# 1. Create set of beverages
beverages = set(("coffee", "juice", "tea"))
print("Beverages set:", beverages)

# 2. Add more items
beverages.update(["water", "milk"])
print("Updated beverages:", beverages)

# 3. Check if microwave is in the set
mySet = {"oven", "kettle", "microwave", "refrigerator"}
print("Is microwave in set?", "microwave" in mySet)

# 4. Remove kettle
mySet.remove("kettle")
print("After removing kettle:", mySet)

# 5. Loop through set
for item in mySet:
    print("Item:", item)

# 6. Add list to set
set_items = {"pen", "book", "ruler", "pencil"}
list_items = ["eraser", "marker"]
set_items.update(list_items)
print("Set after adding list items:", set_items)

# 7. Join two sets
ages = {20, 22, 25}
names = {"Jonathan", "Sarah"}
combined = ages.union(names)
print("Combined set:", combined)
