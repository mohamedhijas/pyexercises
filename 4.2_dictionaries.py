"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:The data is written in the code: five facts
#    about me (name, age, city, studies, language), stored in a dictionary
# 2. Process:the program prints the dictionary, adds a new key "occupation" with the value "Student", prints it again, then removes the key "city".
# 3. Out:the dictionary after adding the occupation, the dictionary after removing the city, and the removedcity (Polonnaruwa).
# 4. My object, my five fields, and why those:Learned  a remove and a value in a  dictionary to show that a dictionary can change after it is created


# Your code below
name = "Hijas"
age = 25
city = "Polonnaruwa"
studies ="Business Administration"
lang = "Tamil"



person = { "name":"Hijas",
           "age": 25, 
           "city": "Polonnaruwa",
           "studies": "Business Administration",
           "lang": "Tamil"}

# printing the dictionary
print("The dictionary is :", person)

# adding a value inside the dictionary
person["occupation"] = "Student"

# the dictionary after adding the value or item
print("The dictionary after adding the occupation:", person)

# removing the city from the dictionary
city = person.pop("city")

print("The dictionary after removing the city:", person)
print("The city removed is", city)