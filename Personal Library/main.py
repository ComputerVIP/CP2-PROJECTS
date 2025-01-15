#Vincent Johnson personal library
#ms larse did a thing
#-Ms. Larose

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

#Cat is my list, inspired by my friend Zoe who sent me a photo of her cat recently
cat = []
def start(cat):

    #This function just finds the index of the item, and adds one to show what position it is in a list to a normal person, it then prints the list
    def srch(cat):
        ans = input("What would you like to search for?\n")
        res = (cat.index(ans)) + 1
        print(f"{cat}\n{ans} is {res} in the list")
        return cat
    
    #This function just repeats for how many things you need to get rid of, the .pop's them, tried eror handling, I don't know why it didn't work
    def remove(cat):
        rpt = int(input("How many things do you want to remove from your list?\n"))
        print(f"rpt: {rpt}\n")
        shw = 0
        while shw < rpt:
            shw += 1
            ad = input(f"What item do you want to remove?\n({shw}/{rpt})\n")
            try:
                cat.pop(ad)
            except:
                print("exception\n")
                return ("Error occurred")
        print(f"\n\n{cat}")
        return cat
        
    #This function just asks for how many times to repeat, then adds you input to the list and prints it
    def add(cat):
        rpt = int(input("How many things do you want to add to your list?\n"))
        shw = 0
        while shw < rpt:
            shw += 1
            ad = input(f"What item do you want to add?\n({shw}/{rpt})\n")
            cat.append(ad)
        print(f"\n\n{cat}")
        return cat
    
    #This is the new and improved selection menu!
    #This is inside the big main function, and will ALWAYS start a new big main function, stopping any weird errors with that
    #It also allows for easier exiting, and allows me to export my variables seamlessly
    #It just has a list of options and whichever you pick, it runs that function
    ans = int(input("\nWhat would you like to do?\n 1 for add to list\n 2 for remove items\n 3 for search\n 4 for exit\n"))
    if ans == 1:
        add(cat)
        return start(cat)
    elif ans == 2:
        remove(cat)
        return start(cat)
    elif ans == 3:
        srch(cat)
        return start(cat)
    else:
        return ("Goodbye!")
#Starts the program
start(cat)