#!/usr/bin/env python3

fullName = input("What is your first & last name?") # creates fullName variable, taking user input
full_Name = fullName.split() # creates full_Name list, from fullName variable split

firstName = str(full_Name[0]) # creates firstName variable of first element from full_Name
first_Name = firstName.capitalize() # creates first_Name, capitalizes variable

lastName = str(full_Name[1]) # creates lastName variable of first element from full_Name
last_Name = lastName.capitalize() # creates last_Name, capitalizes variable

# print response with first_Name and last_Name variables
print(f'Welcome to python, {first_Name}. {last_Name} is a really interesting surname! Are you related to the famous Seth Green?')

'''
2nd part 
'''

valid_Name_Check = False # creates valid_Name_Check boolean control variable with a value of false

while valid_Name_Check == False: # creates a conditional "check" statement with a value of false for the while loop
    
    name_Input = input("Enter your first and last name: ") # creates name_Input variable, taking user input
    
    full_Names = name_Input.split() # creates full_Names list from name_Input variable split
    
    if len(full_Names) == 2: # conditional "check" statement, if the number of words from full_Names list checks out to 2
        valid_Name_Check = True # then valid_Name_Check is now changed from false to true
        
    else:
        print(name_Input + ' is an invalid name, enter two names seperated by a space') # if doesnt check out to 2, remains false and prints the following message
        
# then while loop starts over again, while continue to loop, loop will break when valid_Name_Check is true

print(name_Input.capitalize() + ' is a valid name') 
# if conditional statement checks out and then true (valid_Name_Check), print this following message instead and end script