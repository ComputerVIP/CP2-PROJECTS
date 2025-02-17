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
        #Asks for amount of filters wanted, cleanses inputs to be integers, then goes down either path
        rept = input("How many filters?\n    1\n    2\n").lower()
        rept = rept.replace("two", "2").replace("one", "1")
        try:
            rept = int(rept)
        except:
            return rpt, ("You have inputted a non-number, please enter a number")
        #Filters by one guideline of text inputted
        if rept == 1:
            ans = input("What text you would like to filter by?\n").lower()
            for row in cnt:
                if ans in str(row).lower():
                    #Makes output look fancy
                    row = str(row)
                    row = row.replace("[", "").replace("]", "").replace("'", "")
                    print(row)

        elif rept == 2:
            ans = input("What text you would like to filter by?\n").lower()
            ask = input(f"What other text you would like to filter by?\n(BOTH filters will be used! Only movies containing {ans} and your input here will show)\n").lower()
            #Filters by two guidelines of text inputted
            for row in cnt:
                if ans in str(row).lower():
                    if ask in str(row).lower():
                        #Makes output look fancy
                        row = str(row)
                        row = row.replace("[", "").replace("]", "").replace("'", "")
                        print(row)
        #Error handling
        else:
            print("You have inputted a number that is not allowed")
    #Back to menu
    return rpt

def typsrch(rpt):
    with open("Reading files\Movies list.csv", "r") as file:
        cnt = csv.reader(file)
        next(cnt)
        #Asks for what they want from movies, cleanses input to integers, then prints the index of that item for each row
        ans = input("What would you like to do?\n    Show names(1)\n    Show directors(2)\n    Show genres(3)\n    Show rating(4)\n    Show length(5)\n    Show notable actors(6)\n").lower()
        ans = ans.replace("one", "1").replace("two", "2").replace("three", "3").replace("four", "4").replace("five", "5").replace("six", "6")
        try:
            ans = int(ans)
        except:
            return rpt, ("You have inputted a non-number, please enter a number")
        ans -= 1
        for row in cnt:
            try:
                print(row[ans])
            #Error handling
            except:
                print("Not valid/error ocurred")
    #Back to menu
    return rpt

def recco(rpt):
    with open("Reading files\Movies list.csv", "r") as file:
        cnt = csv.reader(file)
        next(cnt)
        #Asks for input on what they want
        ans = input("What genre, director, rating, length, actors, or names do you want to get reccomendations for?\n").lower()
        #Doing what you asked, range from time! Not just 200 minutes, but could be 178, or 226! :)
        try:
            #This is specifically just for times, will search for times next to time specified by user, leniency specified by user too
            ans = int(ans)
            ask = input(f"Within what range should you get reccomended from {ans}?\n")
            try:
                ask = int(ask)
            except:
                print("That is an invalid input!")
                return rpt
            stp = ans + ask
            ans -= ask
            for row in cnt:
                while ans < stp:
                    #Ms. Larose, I am SO proud of this, I got it to only reccomend times, not the ratings! Even if you input 13, PG-13 movies don't show!
                    #May be an issue, but they have to put in PG-13
                    if (f"{ans},") in str(row).lower():
                        #Makes output look fancy
                        row = str(row)
                        row = row.replace("[", "").replace("]", "").replace("'", "")
                        print(row)
                    ans += 1
                ans = stp - (2*ask)
            #Back to menu
            return rpt
        
        except:
            #Prints row if it contains the thing they want reccomendations for
            for row in cnt:
                if ans in str(row).lower():
                    #Makes output look fancy
                    row = str(row)
                    row = row.replace("[", "").replace("]", "").replace("'", "")
                    print(row)
    #Back to menu
    return rpt

def whole(rpt):
    #Prints entire list
    with open("Reading files\Movies list.csv", "r") as file:
        cnt = csv.reader(file)
        for row in cnt:
            #Makes output look fancy
            row = str(row)
            row = row.replace("[", "").replace("]", "").replace("'", "")
            print(row)
    #Back to menu
    return rpt

def main(rpt):
    #Menu, will run the respective function asked for
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

#Makes sure menu is running at all times, unless specified not to
while rpt > 0:
    main(rpt)