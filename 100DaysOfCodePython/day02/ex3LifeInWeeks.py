age = input("What is your current age?")
age = int(age)
age_left = 90 - age
days = age_left * 365
months = age_left * 12
weeks = age_left * 52
print(" You have {} days, {} weeks, and {} months left.".format(days,weeks,months))