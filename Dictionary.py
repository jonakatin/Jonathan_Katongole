
Shoes = {
    "brand": "Nike",
    "color": "black",
    "size": 40
}
print(Shoes)

# 1. Print size
print("Shoe size:", Shoes["size"])

# 2. Update brand
Shoes["brand"] = "Adidas"
print("Updated brand:", Shoes)

# 3. Add new key
Shoes["type"] = "sneakers"
print("Added type:", Shoes)

# 4. List keys
print("Keys:", list(Shoes.keys()))

# 5. List values
print("Values:", list(Shoes.values()))

# 6. Check if key exists
print("Is 'size' a key?", "size" in Shoes)

# 7. Loop through
for key, value in Shoes.items():
    print(key, ":", value)

# 8. Remove color
Shoes.pop("color")
print("Removed color:", Shoes)

# 9. Empty dictionary
Shoes.clear()
print("Cleared dictionary:", Shoes)

# 10. Copy dictionary
my_dict = {"language": "Python", "version": 3.11}
copy_dict = my_dict.copy()
print("Copied dictionary:", copy_dict)

# 11. Nested dictionaries
family = {
    "child1": {"name": "Alice", "age": 10},
    "child2": {"name": "Bob", "age": 8}
}
print("Nested dictionary:", family)
