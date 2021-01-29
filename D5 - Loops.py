#For Loop

# bike_parts = ['chain','chainring','cassette','brake rotor']
# for part in bike_parts:
#     print(part)

'''
You are going to write a program that calculates the average student height from a List of heights.

The average height can be calculated by adding all the heights together and dividing by the total number of heights.
Average height rounded to the nearest whole number = 164

Important You should not use the sum() or len() functions in your answer. You should try to replicate
their functionality using what you have learnt about for loops.
'''

#Hello there!", end = '')

# student_heights = input("Input a list of student heights in cms separated with space:\n").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# counter = 0
# total = 0
# for x in student_heights:
#     counter += 1
#     total += x
# avg = round(total/counter)
# print(f'Average height for all the students is {avg}cms')

'''
You are going to write a program that calculates the highest score from a List of scores.
Important you are not allowed to use the max or min functions. The output words must match the example. i.e
The highest score in the class is: x
'''

# student_scores = input("Input a list of student scores separated with space:\n").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
#
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#        highest_score = score
#
# print(f"The highest score in the class is: {highest_score}")


#Ranges for item in range (start, final - 1)

# for x in range(0,11):
#     print(x)

# for x in range(0,11, 2): #STEP OF 2
#     print(x)

''' 
# Instructions
You are going to write a program that calculates the sum of all the even numbers from 1 to 100, including 2 and 100.
Important, there should only be 1 print statement in your console output. It should just print the final total and not every 
step of the calculation.
'''

#Option 1

# sum = 0
# for number in range(2,101,2):
#     sum += number
# print(sum)

#Option 2

# sum = 0
# for number in range(0, 101):
#     if number % 2 == 0:
#         sum += number
# print(sum)

'''
## FizzBuzz

# Instructions
You are going to write a program that automatically prints the solution to the FizzBuzz game. 
> `Your program should print each number from 1 to 100 in turn.` 
>   `When the number is divisible by 3 then instead of printing the number it should print "Fizz".` 
>     `When the number is divisible by 5, then instead of printing the number it should print "Buzz".` 
>       `And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`
e.g. it might start off like this:

# Hint
1. Remember your answer should start from 1 and go up to and including 100. 
2. Each number/text should be printed on a separate line.
'''

#
# for number in range(1,101):
#     if (number % 3) == 0 and (number % 5 == 0):
#         print("FizzBuzz")
#     elif number % 5 == 0:
#         print("Buzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     else:
#         print(number)


# #Password Generator Project
# import random
# import string
# letters = list(string.ascii_letters)
# numbers = list(string.digits)
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
#
# #Eazy Level - Order not randomised:
# #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#
# passwd1 = ''
# for x_char in range(0,nr_letters):
#     passwd1 += random.choice(letters)
# for x_symbol in range(0,nr_symbols):
#     passwd1 += random.choice(symbols)
# for x_digit in range(0,nr_numbers):
#     passwd1 += random.choice(numbers)
#
# print(f"Here is your password {passwd1}")
#
# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#
# temp = list(passwd1)
# random.shuffle(temp)
# passwd2 = ''.join(temp)
#
# print(f"Here is your strong password {passwd2}")