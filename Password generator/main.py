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
def start():

    #This function is uppercase and lowercase
    def upp():
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
        return
    
    #This function is lowercase only
    def low():
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
        return
    
    #This function is uppercase, lowercase, and special characters
    def spcl():
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
        return
    
    #This function is uppercase, lowercase, and numbers
    def numb():
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
        return
    
    #This function adds numbers, uppercase, lowercase, and special characters
    def all():
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
        return
    
    #This is to run menus
    print("\nWhat would you like to do?\n 1 for lowercase only\n 2 for uppercase and lowercase")
    ans = int(input(" 3 for special characters\n 4 for numbers and letters\n 5 for all\n"))
    if ans == 1:
        low()
        return start()
    elif ans == 2:
        upp()
        return start()
    elif ans == 3:
        spcl()
        return start()
    elif ans == 4:
        numb()
        return start()
    elif ans == 5:
        all()
        return start()
    else:
        return ("Goodbye!")
start()