#Vincent Johnson, To Do List

'''
Create a to do list (Kept on a txt file)
Add items to the to do list
Mark item as complete
Delete item from to do list
'''

repeat = 1
#res = {}

def add():
    with open('To Do list/List.txt', 'r') as file:
        res = {}
        for line in file:
            res[line.strip().split(':', 0)] = line.strip().split(':', 1)
        try:
            res = dict(line.strip().split(':', 1) for line in file)
            pass
        except:
            try: 
                res = dict(line.strip().split(':', 1) for line in file)
                pass
            except:
                pass
    with open("To Do list/List.txt", "w") as file:
        try:
            for key, values in res.items():
                print(f"{key}: {values}")
        except:
            pass
        ad = input("What would you like to add?\n").upper()
        if ad in res:
            print("You can't add an item that already exists!")
            pass
        else:
            res[ad] = 'TODO'
        for key, value in res.items():
                file.write(f"\n{key}:{value}\n")
        for key, values in res.items():
            print(f"{key}: {values}")
    return

def mark():
    with open('To Do list/List.txt', 'r') as file:
        try:
            res = dict(line.strip().split(':', 1) for line in file)
            pass
        except:
            try: 
                res = dict(line.strip().split(':', 1) for line in file)
                pass
            except:
                pass
    with open("To Do list/List.txt", "w") as file:
        try:
            for key, values in res.items():
                print(f"{key}: {values}")
        except:
            pass
        ad = input("What would you like to mark as completed?\n").upper()
        if ad in res:
            res[ad] = 'COMPLETED'
        for key, value in res.items():
            file.write(f"\n{key}:{value}")
        for key, values in res.items():
            print(f"{key}: {values}")
    return

def delete():
    with open('To Do list/List.txt', 'r') as file:
        try:
            res = dict(line.strip().split(':', 1) for line in file)
            pass
        except:
            try: 
                res = dict(line.strip().split(':', 1) for line in file)
            except:
                pass
    with open("To Do list/List.txt", "w") as file:
        try:
            for key, values in res.items():
                print(f"{key}: {values}")
        except:
            pass
        ad = input("What would you like to delete?\n").upper()
        try:
            del res[ad]
        except:
            pass

        for key, value in res.items():
            file.write(f"\n{key}:{value}")
        for key, values in res.items():
            print(f"{key}: {values}")
    return

def main(repeat):
    ans = input("What would you like to do?\n    1 for adding items\n    2 for marking items as completed\n    3 for deleting items\n    4 for exit\n")
    if ans == "1":
        add()
    elif ans == "2":
        mark()
    elif ans == "3":
        delete()
    else:
        repeat = 0
    return repeat
while repeat > 0:
    main(repeat)
print("Goodbye")