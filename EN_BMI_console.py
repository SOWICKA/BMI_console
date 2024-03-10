# PROJECT: BMI CALCULATOR
# DATE: 16.11.2023
# CODED BY: Kamil Sulewski

import datetime
x = datetime.datetime.now()

print("WELCOME TO THE BMI CALCULATOR")
greet = "Hello"
name = input("Enter your name: ")
print(greet + " " + name + ", it's currently: " + x.strftime("%H:%M"))
weight = input("Enter your weight in kg: ")
height = input("Alright, now enter your height in cm: ")
print()
bmi = "Your BMI is: "

weight2 = weight.replace(",", ".")
height2 = height.replace(",", ".")

width = 44

try:
    if 0 < float(weight2) and 0 < float(height2):
        calculation = float(weight2) / ((float(height2) * 0.01) ** 2)
        print(bmi, round(calculation, 2))
    if 0 < calculation < 16:
        print()
        print("OH NO! Your BMI indicates severe underweight :(")
        print("We recommend seeking medical help quickly!")
    elif 16 <= calculation <= 16.99:
        print("Oops... Your BMI suggests underweight :(")
        print("Consider seeking help.")
    elif 17 <= calculation <= 18.49:
        print()
        print("UNDERWEIGHT")
        print("Change your eating habits and take care of your health.")
    elif 18.5 <= calculation <= 22.99:
        print()
        print("WELL DONE! IT'S GOOD :)")
        print("Remember to have regular meals to maintain a good index ;)")
    elif 23 <= calculation <= 24.99:
        print()
        print("WELL DONE! IT'S GOOD :)")
        print("Watch your calorie intake to maintain a good index ;)")
    elif 25 <= calculation <= 27.49:
        print()
        print("Slight overweight")
        print("Change your eating habits and take care of your health.")
    elif 27.5 <= calculation <= 29.99:
        print()
        print("Significant OVERWEIGHT")
        print("Change your eating habits, incorporate some exercise, and take care of your health.")
    elif 30 <= calculation <= 34.99:
        print()
        print("Oops... Your BMI indicates Obesity I")
        print("Consider seeking help.")
    elif 35 <= calculation <= 39.99:
        print()
        print("NOT GOOD!")
        print("Your BMI indicates Obesity II")
        print("You need a doctor :(")
    elif calculation >= 40:
        print()
        print(":( OH NO! You suffer from Obesity III! ")
        print("Urgent medical help needed! :(")
    if 0 < calculation:
        print("-" * width)
        print("|  BMI     |     Person       |    Date    |")
        print("*" * width)
        print("|{:6.2f}    | {:16s} | {:10s} |".format(round(calculation, 2), name, x.strftime("%d.%m.%Y")))
        print("-" * width)
except ValueError:
    print()
    print("You entered the data incorrectly!")
    print("You entered weight as: " + weight)
    print("You entered height as: " + height)
    print("Start over!")
except:
    print()
    print("Weight and height values must be positive!")
    print("Start over!")

input()

