#!/usr/bin/env python3

# ask for user input, store that input as varName
varName = input("Enter your first name:")
# ask for more user input, store this input as ageVar
ageVar = input("Enter your age:")
# create new variable called ageInt that casts the variable "ageVar" as integer data type 
ageInt = int(ageVar)
# create new variable called numString that combines the value of ageInt and adds 5 to it
numString = ageInt + 5
# print out user name, current age, and the age they will be in 5 years
print(f' Hello {varName}. Your current age is {ageVar}. In five years, you will be {numString} years old!')