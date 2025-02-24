#Vincent Johnson, Multiple Pages Notes

'''
How do you make multiple files in python?
    Explorer > New File > .py
How do you get a function from another file
    from <file name> import <function name>
    import * imports everything
How do you get variables from another file?
    import <variable name>
How do you have a function with multiple returns?
    return __, ___
Why would you use multiple pages for a python project?
    Less data to manage, smoother, better practice
'''

from calc import add as ad, division as div
from calc import minus
from calc import multiply as mul
#Aliasing is where you import a cuntion and give it a new keyword


print(ad(int(input("What number would you like to add?\n")), int(input("What number would you like to add?\n"))))
print(minus(int(input("What number would you like to subtract something by?\n")), int(input("What number would you like to subtract it by?\n"))))
print(div(int(input("What number would you like to divide something by?\n")), int(input("What number would you like to divide it by?\n"))))
print(mul(int(input("What number would you like to multiply?\n")), int(input("What number would you like to multiply it by?\n"))))