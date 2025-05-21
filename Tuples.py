
# 1. Output your favorite phone
x = ("samsung", "iphone", "tecno", "redmi")
print(x)
print("Favourite phone brand:", x[0])

# 2. Print 2nd last item
print("2nd last item:", x[-2])

# 3 & 4. Update and add to tuple (tuples are immutable, so convert to list)
x_list = list(x)
x_list[1] = "itel"
x_list.append("Huawei")
x = tuple(x_list)
print("Updated and added:", x)

# 5. Loop through tuple
for phone in x:
    print("Phone:", phone)

# 6. Remove first item
x_list.pop(0)
x = tuple(x_list)
print("Removed first item:", x)

# 7. Create a tuple using constructor
cities = tuple(("Kampala", "Jinja", "Mbale", "Gulu", "Arua"))
print("Cities tuple:", cities)

# 8. Unpack tuple
(a, b, c, d, e) = cities
print("Unpacked cities:", a, b, c, d, e)

# 9. Range of cities
print("2nd-4th cities:", cities[1:4])

# 10. Join tuples
firsts = ("Jonathan", "Jane")
seconds = ("Katongole", "Smith")
full = firsts + seconds
print("Full names:", full)

# 11. Multiply colors tuple
colors = ("red", "blue", "green")
print("Colors * 3:", colors * 3)

# 12. Count 8s
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print("Count of 8:", thistuple.count(8))
