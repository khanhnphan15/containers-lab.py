# Exercise 1
# Create a list named students containing some student names (strings).
# Print out the second student's name.
# Print out the last student's name.

students = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Print the second student's name
print("Second student:", students[1])

# Print the last student's name
print("Last student:", students[-1])

# Exercise 2
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Use a for loop to print out the string "[food goes here] is a good food".

foods = ("Pizza", "Burger", "Sushi", "Pasta", "Ice Cream")

for food in foods:
    print(f"{food} is a good food")

# Exercise 3
# Using a for loop, print just the last two food strings from foods.

# Hint: Use the slice operator to select the last two foods

foods = ("Pizza", "Burger", "Sushi", "Pasta", "Ice Cream")

# Print the last two food strings using slicing
for food in foods[-2:]:
    print(food)

# Exercise 4
# Create a dictionary named home_town containing the keys of city, state and population.
# Print a string with this format:
# "I was born in city, state - population of population"

home_town = {
    "city": "New York",
    "state": "NY",
    "population": 8500000
}

# Print the formatted string
print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")

# Exercise 5
# Iterate over the key: value pairs in home_town and print a string for each item, for example:
# "city = Arcadia"
# "state = California"
# "population = 58000"

home_town = {
    "city": "Arcadia",
    "state": "California",
    "population": 58000
}

# Iterate over key-value pairs and print formatted strings
for key, value in home_town.items():
    print(f"{key} = {value}")

# Exercise 6
# Create an empty list named cohort.

# Using a for loop to iterate over the students list.

# Hint: Use the enumerate function to provide both the index & student

# Within the for loop, add a dictionary to the cohort list that combines the student's name and the food in the foods list at the same index. Each dictionary will have this shape:

#  {
#    'student': 'Tina',
#    'fav_food': 'Cheeseburger'
#  }
# Iterate over the cohort list, printing out each item (it's not necessary to format the dictionaries).

students = ["Alice", "Bob", "Charlie", "David", "Eve"]
foods = ("Pizza", "Burger", "Sushi", "Pasta", "Ice Cream")

cohort = []

# Populate the cohort list using a for loop with enumerate
for index, student in enumerate(students):
    cohort.append({'student': student, 'fav_food': foods[index]})

# Print the items in the cohort list
for item in cohort:
    print(item)

# Exercise 7
# Using the list of students and a list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
# Iterate over the awesome_students list, printing out each string.

students = ["Tina", "Fred", "Wilma"]

# Create the awesome_students list using a list comprehension
awesome_students = [f"{student} is awesome!" for student in students]

# Print the strings in the awesome_students list
for item in awesome_students:
    print(item)

# Exercise 8
# Use a for loop to iterate over a list comprehension that filters the foods tuple to only include food strings that contains the letter a.
# Within the for loop, print each food string.

foods = ("Pizza", "Burger", "Sushi", "Pasta", "Ice Cream")

# Filter the foods tuple to only include food strings with the letter 'a'
filtered_foods = [food for food in foods if 'a' in food.lower()]

# Print the filtered food strings
for food in filtered_foods:
    print(food)

foods = ("Pizza", "Burger", "Sushi", "Pasta", "Ice Cream")

# Iterate over the foods tuple and print food strings containing the letter 'a'
for food in foods:
    if 'a' in food.lower():
        print(food)

