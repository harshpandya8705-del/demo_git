# Interactive Personal Data Collector

print("Welcome to the Interactive Personal Data Collector!")
print("This program collects your personal information and shows details about variables.\n")

# Collect Information
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
fav_number = int(input("Please enter your favourite number: "))

print("\nThank you! Here is the information we collected:\n")

# Display variable information
print("Name:", name)
print("Type:", type(name))
print("Memory Address:", id(name))
print()

print("Age:", age)
print("Type:", type(age))
print("Memory Address:", id(age))
print()

print("Height:", height)
print("Type:", type(height))
print("Memory Address:", id(height))
print()

print("Favourite Number:", fav_number)
print("Type:", type(fav_number))
print("Memory Address:", id(fav_number))
print()

# Data Processing
current_year = 2026
birth_year = current_year - age

# Display calculation
print("Your birth year is approximately:", birth_year)

# Example of type casting
height_int = int(height)
print("\nType Casting Example:")
print("Height converted from float to integer:", height_int)

# Final Summary
print("\n------ SUMMARY ------")
print("Name:", name)
print("Age:", age)
print("Height:", height, "meters")
print("Favourite Number:", fav_number)
print("Approximate Birth Year:", birth_year)

print("\nThank you for using the Personal Data Collector. Goodbye!")