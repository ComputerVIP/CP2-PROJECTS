#Vincent Johnson
#ms larse did a thing
#-Ms. Larose

'''
A main function that runs the code
Functions for the different password requirements
A function that assembles that password once it is the correct length
Users should be able to specify length and if they want to include
uppercase letters
lowercase letters
numbers
special characters
'''
import random
import string

#This starts the program
cnt2 = 1

#This function is uppercase and lowercase
def upp(cnt2):
    cnt = 5
    lst = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    al = ""
    ans = int(input("How long do you want your password?\n"))
    while cnt > 1:
        while len(al) < ans:
            al = al + lst[(random.randint(0, (len(lst)-1)))]
        print("Possible password:", al)
        al = ""
        cnt -= 1
    ans = int(input(" 1 for menu\n 2 for end\n"))
    if ans == 1:
        cnt2 = 1
        return cnt2
    elif ans == 2:
        cnt2 = 0
        return cnt2

#This function is lowercase only
def low(cnt2):
    cnt = 5
    lst = list(string.ascii_lowercase)
    al = ""
    ans = int(input("How long do you want your password?\n"))
    while cnt > 1:
        while len(al) < ans:
            al = al + lst[(random.randint(0, (len(lst)-1)))]
        print("Possible password:", al)
        al = ""
        cnt -= 1
    ans = int(input(" 1 for menu\n 2 for end\n"))
    if ans == 1:
        cnt2 = 1
        return cnt2
    elif ans == 2:
        cnt2 = 0
        return cnt2

#This function is uppercase, lowercase, and special characters
def spcl(cnt2):
    cnt = 5
    lst = list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.punctuation)
    al = ""
    ans = int(input("How long do you want your password?\n"))
    while cnt > 1:
        while len(al) < ans:
            al = al + lst[(random.randint(0, (len(lst)-1)))]
        print("Possible password:", al)
        al = ""
        cnt -= 1
    ans = int(input(" 1 for menu\n 2 for end\n"))
    if ans == 1:
        cnt2 = 1
        return cnt2
    elif ans == 2:
        cnt2 = 0
        return cnt2

#This function is uppercase, lowercase, and numbers
def numb(cnt2):
    cnt = 5
    lst = list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.digits)
    al = ""
    ans = int(input("How long do you want your password?\n"))
    while cnt > 1:
        while len(al) < ans:
            al = al + lst[(random.randint(0, (len(lst)-1)))]
        print("Possible password:", al)
        al = ""
        cnt -= 1
    ans = int(input(" 1 for menu\n 2 for end\n"))
    if ans == 1:
        cnt2 = 1
        return cnt2
    elif ans == 2:
        cnt2 = 0
        return cnt2

#This function adds numbers, uppercase, lowercase, and special characters
def all(cnt2):
    cnt = 5
    lst = list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.digits) + list(string.punctuation)
    al = ""
    ans = int(input("How long do you want your password?\n(Longer passwords work better)\n"))
    while cnt > 1:
        while len(al) < ans:
            al = al + lst[(random.randint(0, (len(lst)-1)))]
        print("Possible password:", al)
        al = ""
        cnt -= 1
    ans = int(input(" 1 for menu\n 2 for end\n"))
    if ans == 1:
        cnt2 = 1
        return cnt2
    elif ans == 2:
        cnt2 = 0
        return cnt2
    

def start(cnt2):   
    #This is to run menus
    while cnt2 > 0:
        print("\nWhat would you like to do?\n 1 for lowercase only\n 2 for uppercase and lowercase")
        ans = int(input(" 3 for special characters\n 4 for numbers and letters\n 5 for all\n 6 for end\n"))
        if ans == 1:
            cnt2 = low(cnt2)
        elif ans == 2:
            cnt2 = upp(cnt2)
        elif ans == 3:
            cnt2 = spcl(cnt2)
        elif ans == 4:
            cnt2 = numb(cnt2)
        elif ans == 5:
            cnt2 = all(cnt2)
        else:
            print("Goodbye!")
            cnt2 = 0
            return cnt2
    print("Goodbye!")
    return cnt2
while cnt2 > 0:
    cnt2 = start(cnt2)