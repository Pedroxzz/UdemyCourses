programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

#Retriving items from dictionary
#print(programming_dictionary["Function"])

#Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

#Creating an empty dictionary
empty_dictionary = {}

#Wipe and dictionary
#programming_dictionary = {}
#print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
#print(programming_dictionary)

#loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

############################

#Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin","Hamburg","Stuttgart"]
}

#Nesting a Dictionary in a Dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visited":7},
    "Germany": {"cities_visited":["Berlin","Hamburg","Stuttgart"], "total_visited":8}
}