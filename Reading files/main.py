#Vincent Johnson Movie reccomender assignment
'''
Uses the provided Movies list
User is able to choose at least 2 filters for the program to search through
User can get recommendations based on genre, directors, length and/or actors 
User is able to print the whole list
'''
import csv

rpt = 1

def fltrsrch(rpt):
    with open("Reading files\Movies list.csv", "r") as file:
        cnt = csv.reader(file)
        next(cnt)
        rept = input("One or two filters?\n").lower()
        rept = rept.replace("two", "2").replace("one", "1")
        try:
            rept = int(rept)
        except:
            return rpt, ("You have inputted a non-number, please enter a number")
        if rept == 1:
            ans = input("What do you want to filter by?\n").lower()
            for row in cnt:
                if ans in str(row).lower():
                    row = str(row).replace("[", "").replace("]", "").replace("'", "")
                    print(row)
        elif rept == 2:
            ans = input("What do you want to filter by?\n").lower()
            ask = input("What else do you want to filter by?\n").lower()
            for row in cnt:
                if ans in str(row).lower():
                    if ask in str(row).lower():
                        row = str(row).replace("[", "").replace("]", "").replace("'", "")
                        print(row)
        else:
            print("You have inputted a number higher than allowed")
    return rpt
def typsrch(rpt):
    with open("Reading files\Movies list.csv", "r") as file:
        cnt = csv.reader(file)
        next(cnt)
        ans = input("Show names(1)\nShow directors(2)\nShow genres(3)\nShow rating(4)\nShow length(5)\n Show notable actors(6)\n").lower()
        ans = ans.replace("one", "1").replace("two", "2").replace("three", "3").replace("four", "4").replace("five", "5").replace("six", "6")
        try:
            ans = int(ans)
        except:
            return rpt, ("You have inputted a non-number, please enter a number")
        ans -= 1
        for row in cnt:
            try:
                print(row[ans])
            except:
                print("Not valid/error ocurred")
    return rpt
def recco(rpt):
    with open("Reading files\Movies list.csv", "r") as file:
        cnt = csv.reader(file)
        next(cnt)
        ans = input("What genre, director, rating, length, actors, or names do you want to get reccomendations for?\n").lower()
        for row in cnt:
            if ans in str(row).lower():
                row = str(row).replace("[", "")
                row = row.replace("]", "")
                row = row.replace("'", "")
                print(row)
    return rpt
def whole(rpt):
    with open("Reading files\Movies list.csv", "r") as file:
        cnt = csv.reader(file)
        for row in cnt:
            row = str(row).replace("[", "")
            row = row.replace("]", "")
            row = row.replace("'", "")
            print(row)
    return rpt
def main(rpt):
    ask = input("What do you want to do?\n    1 for flitered search\n    2 for type search\n    3 for recommendations\n    4 for whole list\n    5 for exit\n")
    if ask == "1":
        rpt = fltrsrch(rpt)
    elif ask == "2":
        rpt = typsrch(rpt)
    elif ask == "3":
        rpt = recco(rpt)
    elif ask == "4":
        rpt = whole(rpt)
    else:
        rpt = 0
    return rpt

while rpt > 0:
    main(rpt)