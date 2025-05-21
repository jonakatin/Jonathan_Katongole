
# 1. Create a list with 5 names and output the 2nd item
people = ["Alice", "Bob", "Charlie", "David", "Eve"]
print(people)
print("2nd item:", people[1])

# 2. Change the first item
people[0] = "Amina"
print("Changed 1st item:", people)

# 3. Add a 6th item
people.append("Frank")
print("Added 6th item:", people)

# 4. Insert "Bathel" as the 3rd item
people.insert(2, "Bathel")
print("Inserted 'Bathel' as 3rd item:", people)

# 5. Remove the 4th item
people.pop(3)
print("Removed 4th item:", people)

# 6. Print last item using negative indexing
print("Last item (negative index):", people[-1])

# 7. Print a range of items
new_list = ["one", "two", "three", "four", "five", "six", "seven"]
print("3rd-5th items:", new_list[2:5])  # index 2 to 4

# 8. Make a copy of countries
countries = ["Uganda", "Kenya", "Tanzania", "Rwanda"]
countries_copy = countries.copy()
print("Copied countries list:", countries_copy)

# 9. Loop through countries
for country in countries:
    print("Country:", country)

# 10. Sort animal names
animals = ["elephant", "dog", "cat", "giraffe", "zebra"]
animals.sort()
print("Ascending:", animals)
animals.sort(reverse=True)
print("Descending:", animals)

# 11. Print animal names with 'a'
for animal in animals:
    if "a" in animal:
        print("Animal with 'a':", animal)

# 12. Join first and second name lists
first_names = ["John", "Jane"]
second_names = ["Doe", "Smith"]
full_names = first_names + second_names
print("Joined names:", full_names)
