#Vincent Johnson, personal library update
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

lst = []

cnt = 1

# This function just finds the index of the item and adds one to show what position it is in a list to a normal person, then it prints the list
def srch(lst, cnt):
    ans = input("What would you like to search for?\n").upper()
    for i in lst:
        if ans in i:
            print(f"{ans} is in the list")
    ans = int(input(" 1 for menu\n 2 for end\n"))
    if ans == 1:
        cnt = 1
        return cnt, lst
    else:
        cnt = 0
        return cnt, lst

# This function just repeats for how many things you need to get rid of, and removes them from the list
def remove(lst, cnt):
    ans = input("What would you like to remove?\n")
    for i in lst:
        if ans in i:
            lst = lst.remove(i)
    print(lst)

    print(f"\n\n{lst}")
    ans = int(input(" 1 for menu\n 2 for end\n"))
    if ans == 1:
        cnt = 1
        return cnt, lst
    else:
        cnt = 0
        return cnt, lst

# This function asks for how many times to repeat, then adds your input to the list and prints it
def add(lst, cnt):
    rpt = 4
    shw = 0
    lst.append({(input("What is the name of the item?\n").upper): [(input("What is one thing you would like to mention about it?\n").upper()), (input("What is a second thing you would like to mention about it?\n").upper()), (input("What is a third thing you would like to mention about it?\n").upper()), (input("What is a fourth thing you would like to mention about it?\n").upper())]})
    #lst.setdefault((input(f"What kind of item is going to be added?\n({shw}/{rpt})\n").upper()), []).append(input(f"What item do you want to add?\n").upper())
    print(f"\n\n{lst}")
    ans = int(input(" 1 for menu\n 2 for end\n"))
    if ans == 1:
        cnt = 1
        return cnt, lst
    elif ans == 2:
        cnt = 0
        return cnt, lst

#Shows you the list
def view(lst, cnt):
    ans = int(input(" 1 show whole list\n 2 just name of items\n"))
    if ans == 1:
        print(lst)
    elif ans == 2:
        for i in lst:
            for key in i.keys():
                print(key)
    ans = int(input(" 1 for menu\n 2 for end\n"))
    if ans == 1:
        cnt = 1
        return cnt, lst
    elif ans == 2:
        cnt = 0
        return cnt, lst

#This function is the menu and will keep running unless the variable is 0
def main(lst, cnt):
    while cnt > 0:  # Ensure the main loop only runs if cnt > 0
        ans = int(input("\nWhat would you like to do?\n 1 for add to list\n 2 for remove items\n 3 for search\n 4 view list\n 5 for exit\n"))
        if ans == 1:
            try:
                cnt, lst = add(lst, cnt)
            except:
                lst = []
                print("Error occurred, list reset")
        elif ans == 2:
            try:
                cnt, lst = remove(lst, cnt)
            except:
                lst = []
                print("Error occurred, list reset")
        elif ans == 3:
            try:
                cnt, lst = srch(lst, cnt)
            except:
                lst = []
                print("Error occurred, list reset")
        elif ans == 4:
            try:
                cnt, lst = view(lst, cnt)
            except:
                lst = []
                print("Error occurred, list reset")
        elif ans == 5:
            print("Goodbye!")
            cnt = 0
        else:
            print("Invalid option. Please choose a valid option.")
    return cnt, lst

#This ensures that a function will always be running unless it is told not to
while cnt > 0:
    cnt, lst = main(lst, cnt)