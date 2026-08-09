import json
import os

FILENAME = "people.json"

# 1. Load existing data
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
        print(f"⚠️ Error: A section for '{name}' already exists! Choose a unique name or add a last name.")
    else:
        # Check if name field is an integer, sorry all you people who are named using numbers. 
        if name.isdigit():
            print(f"Name cannot be a number. Please try again.")
        else:
            name = name.strip().lower()
            break

# Ask for Age and protect against invalid input
while True:
    try:
        user_input = input("1. How old are you? ")
        age = int(user_input)
        break
    except ValueError:
        print("Error: That was not a whole number. Please try again.\n Input your age as a whole number round up or down if needed. For example, if you are 39.5 years old, input 40 or 39.\n")

# Parse the biological sex input and protect against invalid input, while formatting it to letters because  I am lazy and dont want to address the whole name.
while True:
    try:
        user_input = input("2. What is your biological sex? (male/female): ")
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
        
    except ValueError:
        print("Error: Please enter a valid option.")

# Place Questions into JSON format to be stored in the file.
person_answers = {
    "age": age,
    "bio_sex": bio_sex,
    "weight": float(input("3. What is your weight? ")),
    "height": float(input("4. What is your height? ")),
}

# Nest and Save the data to the JSON file
people_file[name] = person_answers
with open(FILENAME, "w") as file:
    json.dump(people_file, file, indent=4)

print(f"\nSuccessfully saved data for '{name}' to {FILENAME}!")
