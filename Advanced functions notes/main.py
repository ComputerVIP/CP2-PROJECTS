#Vincent Johnson, advanced functions notes
'''
What is a helper function?
    A function that can't do anything itself, but instead has to help others out, usually a 3rd wheel.
    A function to call another function
What is the purpose of a helper function?
    To get others drinks, jobs, and anything else they might ask for, like a helpless butler that has no will besides their master's
    To make the functions less bulky
What is an inner function?
    A 20 year old child living in their parent's basement
    Function inside function
What is the scope of a variable in a function WITH an inner function?
    Can use all the utinsils in their parent's house
    Can use all vriables in outer function
Why do we use inner functions?
    To help with degubbing
What is a closure function?
    Allows variables to travel very wide lands, hitchhiking on functions
    Variables can move from place to place
Why do we write closure functions?
    Talk to the girl in person about how you can't be with her, functions in math was too complicated and it was too much
    To remember values
What is recursion?
    When you look in a mirror
    Functions calling functions
How does recursion work?
    The reflection of your image is reflected off the mirror behind you, back to the front, then back to the back, and continues infinitely
    It calls the function it is using
'''

#Helper function
def help(number):
    try:
        float(number)
    except:
        return help(input('Number?\n'))
    return number

#Regular function
def main_1():
    print('Cool, you are', help(input('Number?\n')), 'year(s) old')


#Inner function
def add(a):
    b = int(input('Number?\n'))

    def addition():
        print(a+b)
    addition()
add(3)


#Closure function
def ad(a):
    b = int(input('Number?\n'))

    def additio(b):
        return a+b
    return additio
base = ad(10)
print(base(5))
base 