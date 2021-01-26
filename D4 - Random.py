import random

# #Creat random int
#
# rand = random.randint(1,100)
# print(rand)
#
# #Random 0.0000000 - 0.999999 excluding 1
# random_float = random.random()
# print(random_float*4)
#
# #Random float in range
# random_float2 = random.uniform(14,20)
# print(random_float2)
#

#write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

coin = random.randint(0,1)
if coin == 0:
    print("Tails")
else:
    print("Heads")