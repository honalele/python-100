# Day #2 Challenge
# Author: Naren
# Date: 2022.9.13
print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
n_people = input("How many people to split the bill? ")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")

payment = format((float(total_bill) + float(tip))/int(n_people), '.2f')
print("Each person should pay: ${}".format(payment)) 