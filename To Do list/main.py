#Vincent Johnson, To Do List

'''
Create a to do list (Kept on a txt file)
Add items to the to do list
Mark item as complete
Delete item from to do list
'''

repeat = 1 #Repeat variable, as long as it's above 1, the program runs

def add():
    with open('To Do list/List.txt', 'r') as file: #Opens in read mode
        res = {}
        for line in file: #Makes a dictionary, key is item name, value is it's status, to-do, or completed
            a = line.strip().split(':', 1)
            try:
                res[a[0]] = a[1]
            except:
                pass
    with open("To Do list/List.txt", "w") as file:
        try:
            for key, values in res.items(): #Prints the dictionary nicely
                print(f"{key}: {values}")
        except:
            pass
        ad = input("What would you like to add?\n").upper()
        if ad in res: #Makes sure they're not adding an item that already exists
            print("You can't add an item that already exists!")
            pass
        else:
            res[ad] = 'TODO'
        for key, value in res.items(): #Writes to the file
                file.write(f"\n{key}:{value}\n")
        for key, values in res.items(): #Prints the dictionary again
            print(f"{key}: {values}")
    return

def mark():
    with open('To Do list/List.txt', 'r') as file:
        res = {}
        for line in file: #Makes a dictionary, key is item name, value is it's status, to-do, or completed
            a = line.strip().split(':', 1)
            try:
                res[a[0]] = a[1]
            except:
                pass
    ans = input("What would you like to do?\n    1 mark as completed\n    2 mark as to-do\n")
    if ans == "1": #If they want to mark as completed
        with open("To Do list/List.txt", "w") as file:
            try: #Prints dictionary nicely
                for key, values in res.items():
                    print(f"{key}: {values}")
            except:
                pass
            ad = input("What would you like to mark as completed?\n").upper()
            if ad in res: #Sets value to completed
                res[ad] = 'COMPLETED'
            else: #Makes sure the item is there
                return ("You can't mark something that isn't there!")
            for key, value in res.items(): #Writes dictionary to file
                file.write(f"\n{key}:{value}")
            for key, values in res.items(): #Prints dictionary again
                print(f"{key}: {values}")
        pass
    elif ans == "2":
        with open("To Do list/List.txt", "w") as file:
            try: #Prints dictionary
                for key, values in res.items():
                    print(f"{key}: {values}")
            except:
                pass
            ad = input("What would you like to mark as to-do?\n").upper()
            if ad in res: #Sets value to-do
                res[ad] = 'TODO'
            else: #Makes sure it is in the list
                print("You can't mark something that isn't there!") #I know, bad practice, but if I put a print on there, it just prints 'None' if it works right
                return
            for key, value in res.items(): #Writes to the file
                file.write(f"\n{key}:{value}")
            for key, values in res.items(): #Shows dictionary nicely
                print(f"{key}: {values}")
        pass
    else:
        pass   
    return

def delete():
    with open('To Do list/List.txt', 'r') as file:
        res = {}
        for line in file: #Makes a dictionary, key is item name, value is it's status, to-do, or completed
            a = line.strip().split(':', 1)
            try:
                res[a[0]] = a[1]
            except:
                pass
    with open("To Do list/List.txt", "w") as file:
        try: #Prints the dictionary
            for key, values in res.items():
                print(f"{key}: {values}")
        except:
            pass
        ad = input("What would you like to delete?\nNOTE! THIS WILL PERMANENTLY DELETE THE ITEM\n").upper()
        try: #Deletes the item
            if ad in key:
                del res[ad]
            else:
                pass
        except:
            pass

        for key, value in res.items(): #Writes to file
            file.write(f"\n{key}:{value}")
        for key, values in res.items(): #Shows dictionary nicely
            print(f"{key}: {values}")
    return

def show():
    with open('To Do list/List.txt', 'r') as file:
        res = {}
        for line in file: #Makes a dictionary, key is item name, value is it's status, to-do, or completed
            a = line.strip().split(':', 1)
            try:
                res[a[0]] = a[1]
            except:
                pass
        ans = input('''What would you like to do?
    1 show to-do
    2 show completed
    3 show whole list
''')
    try:
        ans = int(ans)
        if ans == 1:
            try:
                for key, values in res.items(): #Prints entire list nicely
                    if values == "TODO":
                        print(f"{key}: {values}")
                    else:
                        pass
            except:
                pass
        elif ans == 2:
            try:
                for key, values in res.items(): #Prints entire list nicely
                    if values == "COMPLETED":
                        print(f"{key}: {values}")
                    else:
                        pass
            except:
                pass
        elif ans == 3:
            try:
                for key, values in res.items(): #Prints entire list nicely
                    print(f"{key}: {values}")
            except:
                pass
    except:
        print("Not a valid input!")
    return

def search():
    with open('To Do list/List.txt', 'r') as file:
        res = {}
        for line in file: #Makes a dictionary, key is item name, value is it's status, to-do, or completed
            a = line.strip().split(':', 1)
            try:
                res[a[0]] = a[1]
            except:
                pass
        ans = input("What do you want to search for?\n").upper() #Asks for you want to search for
        try:
            for key, values in res.items(): #Checks to see if it is in either part of the item
                if ans in key: 
                    print(f"{key}: {values}")
                elif ans in values:
                    print(f"{key}: {values}")
                else:
                    pass
        except:
            pass
    return

def main(repeat):
    ans = input('''What would you like to do?
    1 for adding items
    2 for marking items as completed
    3 for deleting items
    4 for showing list
    5 for search
    6 for exit
''')
    try:
        ans = int(ans)
        if ans == 1:
            add()
        elif ans == 2:
            print(mark())
        elif ans == 3:
            delete()
        elif ans == 4:
            show()
        elif ans == 5:
            search()
        elif ans == 6:
            repeat = 0
            return repeat
        pass
    except:
        print("Not a valid answer!")
    repeat = 1
    return repeat

while repeat > 0:
    repeat = main(repeat)
print("Goodbye")