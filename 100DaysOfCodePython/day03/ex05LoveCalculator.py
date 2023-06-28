print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
n1 = name1.lower()
n2 = name2.lower()
t = n1.count("t")
r = n1.count("r")
u = n1.count("u")
e = n1.count("e")

t += n2.count("t")
r += n2.count("r")
u += n2.count("u")
e += n2.count("e")

l = n1.count("l")
o = n1.count("o")
v = n1.count("v")
e = n1.count("e")

l += n2.count("l")
o += n2.count("o")
v += n2.count("v")
e += n2.count("e")

true = t+r+u+e
love = l+o+v+e

true = str(true)
love = str(love)
love_score = true + love
love_score = int(love_score)
if love_score < 10 or love_score > 90:
    print("Your score is {}, you go together like coke and mentos.".format(love_score))
elif 40 < love_score < 50:
    print("Your score is {}, you are alright together.".format(love_score))
else:
    print("Your score is {}.".format(love_score))