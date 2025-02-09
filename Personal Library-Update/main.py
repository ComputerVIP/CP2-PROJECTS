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

lst = {
    
}

cnt = 1

# This function just finds the index of the item and adds one to show what position it is in a list to a normal person, then it prints the list
def srch(lst, cnt):
    ans = input("What would you like to search for?\n").upper()
    for key, values in lst.items():
        if ans in values:
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
    rpt = int(input("How many things do you want to remove from your list?\n"))
    shw = 0
    while shw < rpt:
        print(lst)
        shw += 1
        key1 = input(f"What kind of item is going to be removed?\n({shw}/{rpt})\n").upper()
        inpt = input(f"What would you like to remove?\n").upper()
        lst[key1] = [x for x in lst[key1] if x != inpt]  

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
    rpt = int(input("How many things do you want to add to your list?\n"))
    shw = 0
    while shw < rpt:
        shw += 1
        lst.setdefault((input(f"What kind of item is going to be added?\n({shw}/{rpt})\n").upper()), []).append(input(f"What item do you want to add?\n").upper())
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
    print(lst)
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
            cnt, lst = add(lst, cnt)
        elif ans == 2:
            cnt, lst = remove(lst, cnt)
        elif ans == 3:
            cnt, lst = srch(lst, cnt)
        elif ans == 4:
            cnt, lst = view(lst, cnt)
        elif ans == 5:
            print("Goodbye!")
            cnt = 0
        else:
            print("Invalid option. Please choose a valid option.")
    return cnt, lst

#This ensures that a function will always be running unless it is told not to
while cnt > 0:
    cnt, lst = main(lst, cnt)