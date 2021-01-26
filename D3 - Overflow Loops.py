# #Check if the number if odd or even
#
# number = int(input("Which number do you want to check?\n"))
# if number % 2 == 0:
#     print(f"{number} is an even number")
# else:
#     print(f"{number} is an odd number")


##RollerCoaster Check
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
#
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7.")
#     elif age >= 45 and age <= 55:
#         print("Everything is going to be ok. Have a free ride on us!")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")
#
#     wants_photo = input("Do you want a photo taken? Y or N. ")
#     if wants_photo == "Y":
#         bill += 3
#
#     print(f"Your final bill is ${bill}")
#
# else:
#     print("Sorry, you have to grow taller before you can ride.")


'''
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

    Under 18.5 they are underweight
    Over 18.5 but below 25 they have a normal weight
    Over 25 but below 30 they are slightly overweight
    Over 30 but below 35 they are obese
    Above 35 they are clinically obese.
'''
# height = float(input("enter your height in m: "))
# weight = int(input("enter your weight in kg: "))
# bmi = int(weight/(pow(height,2)))
#
# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you're underweight") #Interval Comparison
# elif 18.5 <= bmi < 25:
#     print(f"Your BMI is {bmi}, you have a normal weight")
# elif 25 <= bmi < 30:
#     print(f"Your BMI is {bmi}, you're slightly overweight")
# elif 30 <= bmi < 35:
#     print(f"Your BMI is {bmi}, you're obese")
# else:
#     print(f"Your BMI is {bmi}, you're clinically obese")


'''
Write a program that works out whether if a given year is a leap year. 
A normal year has 365 days, leap years have 366, with an extra day in February. 
The reason why we have leap years is really fascinating. 

On every year that is evenly divisible by 4 **except** every year 
that is evenly divisible by 100 **unless** the year is also evenly divisible by 400


1.   If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
2.    If the year is NOT divisible by 100, go to step 4. Otherwise, go to step 3.
3.    If the year is evenly divisible by 100 and also evenly divisible by 400 go to step 4. Otherwise, go to step 5.
4.    The year is a leap year (it has 366 days).
5.    The year is not a leap year (it has 365 days).

'''

# year = int(input("Which year do you want to check?\n"))
# if year % 4 == 0:
#     if year % 100 != 0:
#         print(f"{year} is a leap year")
#     elif (year % 100 == 0) and (year % 400 == 0):
#         print(f"{year} is a leap year.")
#     else:
#         print(f"{year} is not a leap year.")
# else:
#     print(f"{year} is not a leap year.")
#
'''
Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
Based on a user's order, work out their final bill.
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1
'''


# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L\n")
# add_pepperoni = input("Do you want pepperoni? Y or N\n")
# extra_cheese = input("Do you want extra cheese? Y or N\n")



#First Attempt Large Code Block

# small_pizza = 15 #Small Pizza
# medium_pizza = 20
# large_pizza = 25
# pepperoni_small = 2 #Pepperoni Small
# pepperoni_md_lg = 3 #Pepperoni Medium/Large
# cheese = 0
# if extra_cheese == 'Y':
#     cheese = 1
#
# if size == 'S':
#     if add_pepperoni == 'Y':
#         print("Your final bill is", small_pizza + cheese + pepperoni_small)
#     else:
#         print("Your final bill is", small_pizza + cheese)
# elif size == 'M':
#     if add_pepperoni == 'Y':
#         print("Your final bill is", medium_pizza + cheese + pepperoni_md_lg)
#     else:
#         print("Your final bill is", medium_pizza + cheese)
# elif size == 'L':
#     if add_pepperoni == 'Y':
#         print("Your final bill is", large_pizza + cheese + pepperoni_md_lg)
#     else:
#         print("Your final bill is", medium_pizza + cheese)
# else:
#     print("Sorry, no pizza for you!.")


#Refined

# bill = 0
#
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25
#
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
#
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"Your final bill is: ${bill}.")


#Logical Operators

# 'and' True if both the operands are true x and y
# 'or' True if either of the operands is true x or y
# 'not' True if operand is false (complements the operand) not x

''' 
Take both people's names and check for the number of times the letters in the word TRUE occurs. 
Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number. 
For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:
"Your score is **z**."
'''

# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# word1 = 'true'
# word2 = 'love'
# name3 = (name1 + name2)
# name3 = name3.lower()
# score = 0
# score1 = 0
# score2 = 0
# for x in name3:
#     if x in word1:
#         score1 += 1
# for t in name3:
#     if t in word2:
#         score2 += 1
#
# temp = str(score1) + str(score2)
# score = int(temp)
#
# if 10 >= score < 90:
#     print(f"Your score is {score}, you go together like coke and mentos.")
# elif 40 <= score <= 50:
#     print(f"Your score is {score}, you are alright together.")
# else:
#     print(f"Your score is {score}.")


# #Write your code below this line 👇
#
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# combined_names = name1 + name2
# lower_names = combined_names.lower()
# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")
# first_digit = t + r + u + e
#
# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# e = lower_names.count("e")
# second_digit = l + o + v + e
#
# score = int(str(first_digit) + str(second_digit))
#
# if (score < 10) or (score > 90):
#   print(f"Your score is {score}, you go together like coke and mentos.")
# elif (score >= 40) and (score <= 50):
#   print(f"Your score is {score}, you are alright together.")
# else:
#   print(f"Your score is {score}.")


print('''
*******************************************************************************
 _                        _ 
| |                      | |
| |__   ___  _ __ ___  __| |
| '_ \ / _ \| '__/ _ \/ _` |
| |_) | (_) | | |  __/ (_| |
|_.__/ \___/|_|  \___|\__,_|
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")