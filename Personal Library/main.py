#Vincent Johnson personal library
#ms larse did a thing
'''
Stores all items in a list
Function to add a new item
Function to search the items
Function to remove an item
Function that runs the code (displays the menu options inside and calls the functions inside of a while True loop)
Project must include
easy to understand variable and function names
Pseudocode comments explaining what the code is doing
Good use of white space to keep items separate and easy to read/find
Have at least 2 people test your code before submission!
'''
def main():
    cat = []
    title = input("What kind of thing is going to be stored in this library?")
    rpt = int(input("How many things do you want to add?"))
    while rpt > 0:
        ad = input("What")