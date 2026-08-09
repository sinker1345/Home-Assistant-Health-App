import json
import os

FILENAME = "people_answers.json"

# 1. Load existing data
if os.path.exists(FILENAME):
    with open(FILENAME, "r") as file:
        try:
            all_people_data = json.load(file)
        except json.JSONDecodeError:
            all_people_data = {}
else:
    all_people_data = {}

# Ask for the name and protect against overwriting and integar input
while True:
    person_name = input("Enter the person's name: ")
    
    # Check if name is blank
    if not person_name:
        print("Name cannot be empty. Please try again.")
        continue  
    # Check if the name already exists as a section key
    if person_name in all_people_data:
        print(f"⚠️ Error: A section for '{person_name}' already exists! Choose a unique name or add a last name.")
    else:
    # Check if name field is an integer, sorry all you people who are named using numbers. 
        if person_name.isdigit():
            print(f"Name cannot be a number. Please try again.")
        else:
            person_name = person_name.strip().lower()
            break
# Ask for Age and protect against invalid input
while True:
    try:
        user_input = input("1. How old are you? ")
        age = int(user_input)
        break # Exit only when a valid integer is provided
    except ValueError:
        print("Error: That was not a whole number. Please try again.\n Input your age as a whole number round up or down if needed. For example, if you are 39.5 years old, input 40 or 39.\n")
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
    # Convert to m/f because im lazy and dont want to adress the whole name


# 3. Gather the answers for this unique person
person_answers = {
    "age": age,
    "bio_sex": bio_sex,
    "color": input("3. What is your favorite color? ").lower(),
    "hobby": input("4. What is your favorite hobby? ").lower(),
    "food": input("5. What is your favorite food? ").lower()
}

# 4. Nest and save the data
all_people_data[person_name] = person_answers

with open(FILENAME, "w") as file:
    json.dump(all_people_data, file, indent=4)

print(f"\nSuccessfully saved data for '{person_name}' to {FILENAME}!")
