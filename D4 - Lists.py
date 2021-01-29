#https://docs.python.org/3/tutorial/datastructures.html
import random

#https://railsware.com/blog/python-for-machine-learning-indexing-and-slicing-for-lists-tuples-strings-and-other-sequential-types/#Negative_indexes
# >>> basket = ['bread', 'butter', 'milk']
# >>> basket[0] = 'cake'
# >>> basket
# ['cake', 'butter', 'milk']
#
# >>> basket = ['bread', 'butter', 'milk']
# >>> del basket[0]
# ['butter', 'milk']
#
# >>> nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# >>> some_nums = nums[2:7]
# >>> some_nums
# [30, 40, 50, 60, 70]
#
# >>> nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# >>> nums[:5]
# [10, 20, 30, 40, 50]
#
# >>> nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# >>> nums[-3:]
# [70, 80, 90]
#
# >>> nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# >>> nums[1:-1]
# [20, 30, 40, 50, 60, 70, 80]
# >>> nums[-3:8]
# [70, 80]
# >>> nums[-5:-1]
# [50, 60, 70, 80]
#
# >>> nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# >>> nums[:-2]
# [10, 20, 30, 40, 50, 60, 70]
#
# #STEPS
# >>> nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# >>> nums[:-2]
# [10, 20, 30, 40, 50, 60, 70]
#
# #Negative Steps
# >>> nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# >>> nums[::-1]
# [90, 80, 70, 60, 50, 40, 30, 20, 10]
#
# >>> nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# >>> nums[-2::-1]
# [80, 70, 60, 50, 40, 30, 20, 10]
#
# >>> nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# >>> nums[-2:1:-1]
# [80, 70, 60, 50, 40, 30]
#
# >>> nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# >>> nums[-2:1:-3]
# [80, 50]
#
# >>> nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# >>> first_five = nums[0:5]
# >>> first_five[2] = 3
# >>> first_five
# [10, 20, 3, 40, 50]
# >>> nums
# [10, 20, 30, 40, 50, 60, 70, 80, 90]
#
# #It creates a shallow copy of the whole list and is a good shorthand when you need a copy of the original list.
#
# >>> nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# >>> nums_copy = nums[:]
# >>> nums_copy[0] = 33
# >>> nums_copy
# [33, 20, 30, 40, 50, 60, 70, 80, 90]
# >>> nums
# [10, 20, 30, 40, 50, 60, 70, 80, 90]
#
# >>> nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# >>> nums[:4] = [1,2,3,4]
# >>> nums
# [1, 2, 3, 4, 50, 60, 70, 80, 90]


'''
You are going to write a program which will select a random name from a list of names.
The person selected will have to pay for everybody's food bill.
Important: You are not allowed to use the choice() function. '''


# Split string method
# names_string = input("Give me everybody's names, separated by a comma.\n")
# names = names_string.split(", ")
# #Write your code below this line
# list_lenght = (len(names)-1)
# rand = random.randint(0,list_lenght)
# payer = names[rand]
# print(f"{payer} is going to buy the meal today!")
#
# #Alternative
#
# #payer = random.choice(names)

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
#
# dirty_dozen = [fruits, vegetables]
# List 1 position 1
# print(dirty_dozen[1][1])
'''
In the starting code, you will find a variable called map.

This map contains a nested list

In the starting code, we have used new lines (\n) to format the three rows into a square, like this:

['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']

Your job is to write a program that allows you to mark a square on the map using a two-digit system. 
The first digit is the vertical column number and the second digit is the horizontal row number. e.g.:

x = map[2][3]  2 = Column // 3 = Row 
'''

# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# mark = input("Where do you want to put the treasure? ")
# row = int(mark[1])-1
# colum = int(mark[0])-1
# map[row][colum] = 'X'
#
# #Write your code above this row 👆
#
# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")

# #ROCK - PAPER - SCISSORS
#
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
#
# print("Welcome to the Rock, Paper, Scissors Tournament")
# human = int(input("Make a selection (0, 1 or 2):\n\n0. Rock\n1. Paper\n2. Scissors\n"))
# while huma
# computer = random.randint(0, 2)
# game = [rock,paper,scissors]
# print(f"{game[human]}")
# print(f"\nComputer chose:\n{game[computer]}")
#
# if human == computer:
#     print("It's a Draw")
# elif human == 0 and computer == 1:
#     print("You lose")
# elif human == 0 and computer == 2:
#     print("You Win")
# elif human < computer:
#     print("You lose")
# elif human > computer:
#     print("You Win")

