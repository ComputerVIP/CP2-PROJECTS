#Vincent Johnson financial calculator
#ms larse did a thing
'''
How long it will take to save for a goal based on a weekly or monthly deposit
Compound Interest Calculator 
Budget Allocator (use set percentages to divide an income into spending categories like savings, entertainment, and food)
Sale Price Calculator (apply discounts to prices)
Tip Calculator
'''

def add():
    ans = float(input("What's your goal?\n"))
    ans2 = float(input("How much money depositted per week?\n"))
    print("This is how many weeks you need to save:", round((ans/ans2), 1))
def interest():
    ans = int(input("How much interest? (3% is 3)"))
    ans2 = float(input("How much do you have in your account?"))
def budget():
    pass
def sale():
    pass
def tip():
    pass
def main():
    ans = int(input("What would you like to do?\n1 for time to goal\n2 for interest\n3 for budget allocator\n4 for sale price\n5 for tip calculator\n"))
    if ans == 1:
        add()
    elif ans == 2:
        interest()
    elif ans == 3:
        budget()
    elif ans == 4:
        sale()
    elif ans == 5:
        tip()
    else:
        return
    
main()