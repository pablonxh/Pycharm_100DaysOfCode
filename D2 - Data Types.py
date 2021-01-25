##String Chunk
#
# print('Hello'[0])
#
# print("124" + "124")
# print(124+124)
# mystery = 734_529.678
# print(mystery)
#
# #Type Check
# print(type(mystery))
#
##Type Casting - Comment out code Mac Cmd + /
# num = 45
# num_str = str(num)
# num1 = float(123)
# num2 = str(123)
# print(num1)
# print(num2)


#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# two_digit_number = input("Type a two digit number: ")
# t = int(two_digit_number[0]) + int(two_digit_number[1])
# print(t)

#Math Operations

# a = 7+3
# a = 7-3
# a = 7*3
# a = 8/4
# a = 8**2 #EXP 2
# a = 8%2 #MOD 2
#
# PEMDAS -
# parenthesis
# Exponential
# Multiplication - Same weight as division, calculated left to right
# Division
# Addition Same weight as substraction, calculated left to right
# Substraction

### += /= -= *= #Add to current variable

#BMI Calculation - Problem

# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
#
# Write your code below this line

# print("You BMI is: ", ((int(weight))/(pow(float(height),2))))
# print("You BMI is: ", ((int(weight))/(float(height)**2))) #Same without pow
# print("You BMI is: ", (int((int(weight))/(float(height)**2)))) #Same with integer result

#Round Function

# a = round(8/3)
# a = round(8/3,2) #Choose number of decimals
# a = round(2.6666666,2) #Round float
# a = round(8//3) #Floating division int type

## F-String - Print without casting variables

# age = 24.5
# score = 18
# name = "Pablo"
# print(f"{name}, you're {age} years old and this is your current score: {score}")


#Days in life remaining until 90 yo

# age = input("What is your current age?\n")
#
# #Write your code below this line 👇
# # 1 YEAR = 365 days, 52 weeks & 12 Months
#
# left_years = 90 - int(age)
# days = left_years * 365
# weeks = left_years * 52
# months = left_years * 12
# print(f"You have {days} days, {weeks} weeks, and {months} months left.")


#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

# print("Welcome to the tip calculator.")
# total = float(input("What was the total of the bill?\n"))
# tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15\n"))
# eaters = int(input("How many people to split the bill?\n"))
# percentage = round(((tip_percentage/100)+1),2)
# bill = round(((total * percentage)/eaters),2)
# print(f"Each person should pay: ${bill}")
