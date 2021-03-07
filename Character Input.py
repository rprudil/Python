# Character Input

# Exercise 1
# Create a program that asks the user to input their name and their age. Print out a message addressed to them that says the year that they will turn 100 years old.

name = input("Please print your name ")
age = input("Please print your age ")
current = int(age)
year = str((100 - current) + 2021)

print("Dear " + name + ", the year of " + year + " will be the year you turn 100 years old.")
