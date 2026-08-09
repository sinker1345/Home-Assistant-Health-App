import json
import math
import os

FILENAME = "people.json"

# Load existing data
if os.path.exists(FILENAME):
    with open(FILENAME, "r") as file:
        try:
            people_file = json.load(file)
        except json.JSONDecodeError:
            people_file = {}
else:
    people_file = {}

# Ask for the name and protect against overwriting and integar input
while True:
    name = input("Enter the your name: ")
    # Check if name is blank
    if not name:
        print("Name cannot be empty. Please try again.")
        continue  
    # Check if the name already exists as a section key
    if name in people_file:
        print(f"Error: A section for '{name}' already exists! Choose a unique name or add a last name.")
        continue
    else:
        # Check if name field is an integer, sorry all you people who are named using numbers. 
        if name.isdigit():
            print("Name cannot be a number. Please try again.")
            continue
        else:
            name = name.strip().lower()
            break

# Ask for Age and protect against invalid input
while True:
    try:
        user_input = input("How old are you? ")
        age = int(user_input)
        break
    except ValueError:
        print("Error: That was not a whole number. Please try again.\n Input your age as a whole number round up or down if needed. For example, if you are 39.5 years old, input 40 or 39.")
        continue

# Parse the biological sex input and protect against invalid input, while formatting it to letters because  I am lazy and dont want to address the whole name.
while True:
    try:
        user_input = input("What is your biological sex? (male/female): ")
        bio_sex = user_input.lower()
        if bio_sex in ["male", "female",]:
            if bio_sex == "male":
                bio_sex = "m"
                break
            elif bio_sex == "female":
                bio_sex = "f"
                break
        else:
            print("Error: Please enter 'male' or 'female'.")
            continue
    except ValueError:
        print("Error: Please enter a valid option.")

# Metric?
while True:
    try:
        user_input = input("Would you like to use metric units? (yes/no): ")
        metric = user_input.lower()
        if metric in ["yes", "no"]:
            if metric == "yes":
                metric = True
                break
            elif metric == "no":
                metric = False
                break
        else:
            print("Error: Please enter 'yes' or 'no'.")
            continue
    except ValueError:
        print("Error: Please enter a valid option.")

# Ask Ideal Weight and protect against invalid input
while True:
    if metric:
        try:
            user_input = input("What is your ideal weight in kilograms? ")
            wanted_weight = float(user_input)  # Ideal weight in kilograms
            break
        except ValueError:
            print("Error: Please enter a valid number for ideal weight.")
    try:
        user_input = input("What is your ideal weight in pounds? ")
        wanted_weight = float(user_input)*0.453592  # Convert pounds to kilograms
        break
    except ValueError:
        print("Error: Please enter a valid number for ideal weight.")

# Parse and handle weight input
while True:
    if metric:
        try:
            user_input = input("What is your weight in kilograms? ")
            weight = float(user_input)  # Weight in kilograms
            break
        except ValueError:
            print("Error: Please enter a valid number for weight.")
    try:
        user_input = input("What is your weight in pounds? ")
        weight = float(user_input)*0.453592  # Convert pounds to kilograms
        break
    except ValueError:
        print("Error: Please enter a valid number for weight.")

# Parse and handle height input
while True:
    if metric:
        try:
            user_input = input("What is your height in centimeters? ")
            height = float(user_input)  # Height in centimeters
            break
        except ValueError:
            print("Error: Please enter a valid number for height.")
    try:
        user_input = input("What is your height in inches? ")
        height = float(user_input)*2.54  # Convert inches to centimeters
        break
    except ValueError:
        print("Error: Please enter a valid number for height.")

# Parse and handle activity level input
while True:
    try:
        user_input = input("What is your activity level? (Sedentary, Light, Moderate, Active, Very Active): ")
        activity_level = user_input.lower()
        if activity_level == "sedentary":
            activity_level = 1.2
            break
        elif activity_level == "light":
            activity_level = 1.375
            break
        elif activity_level == "moderate":
            activity_level = 1.55
            break
        elif activity_level == "active":
            activity_level = 1.725
            break
        elif activity_level == "very active":
            activity_level = 1.9
            break
        else:
            print("Error: Please enter a valid activity level from the provided options.")
    except ValueError:
        print("Error: Please enter a valid number for activity level.")

# Calculate BMR and save it to the JSON file
if bio_sex == "m":
    bmr = math.floor(((10*weight) + (6.25*height) - (5*age) + 5)*activity_level)
    diet_calories = math.floor(bmr * 0.8)
elif bio_sex == "f":
    bmr = math.floor(((10*weight) + (6.25*height) - (5*age) - 161)*activity_level)
    diet_calories = math.floor(bmr * 0.8)

# Place Questions into JSON format to be stored in the file.
person_answers = {
    "age": age,
    "bio_sex": bio_sex,
    "wanted_weight": wanted_weight,
    "bmr": bmr,
    "weight": weight,
    "height": height,
    "activity_level": activity_level,
    "diet_calories": diet_calories,
}

# Nest and Save the data to the JSON file
people_file[name] = person_answers
with open(FILENAME, "w") as file:
    json.dump(people_file, file, indent=4)

print(f"\nSuccessfully saved data for '{name}' to {FILENAME}! your Daily Calorie intake is: {bmr} calories/day at your activity level, reduce to {diet_calories} calories/day to lose weight.")