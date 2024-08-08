import sys

age = int(input("What is your age?"))

if age >= 21:
    drinkingage = True 
else: 
    print("You can not be drinking please call a local help line!")
    sys.exit() 

gender = input("What is your gender?") 
weight = int(input("What is your weight in lbs?"))
hours = int(input("How long ago was your last drink?"))
ounces = int(input("How many ounces have you drank?"))

bac = (ounces * 5.14 / (weight * (0.68 if gender.lower() == 'male' else 0.155))) - 0.015 * hours 

if bac >= 0.08: 
    print("You are not able to drive! your bac is around " + str(round, 2(bac)))
else: 
    print("You are good to drive but ask a friend, your bac is around " + str(round, 2(bac)))  



