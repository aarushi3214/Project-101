import random

min = 1
max = 6

response = "yes"

while response == "yes" or response == "y":
    print("Now Rolling the dice...")
    print ("Number on the dice is: ")
    print(random.randint(min, max))
    response = input("Are you interested to Roll the dice again? ")
