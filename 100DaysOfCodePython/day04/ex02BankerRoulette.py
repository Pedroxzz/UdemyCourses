# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num_names = len(names)
random_choice = random.randint(0,num_names-1)
random_person = names[random_choice]
print(f'{random_person} is going to buy the meal today!')