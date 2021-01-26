#https://docs.python.org/3/tutorial/datastructures.html

'''
You are going to write a program which will select a random name from a list of names.
The person selected will have to pay for everybody's food bill.
Important: You are not allowed to use the choice() function. '''


# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

#Write your code below this line
print(names)
