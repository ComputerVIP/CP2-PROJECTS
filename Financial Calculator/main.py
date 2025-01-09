#Vincent Johnson financial calculator
#ms larse did a thing
'''
How long it will take to save for a goal based on a weekly or monthly deposit
Compound Interest Calculator 
Budget Allocator (use set percentages to divide an income into spending categories like savings, entertainment, and food)
Sale Price Calculator (apply discounts to prices)
Tip Calculator
'''
#This is for time to goal, will round for weeks to goal
def add():
    ans = float(input("What's your goal?\n"))
    ans2 = float(input("How much money depositted per week?\n"))
    return ("This is how many weeks you need to save:", round((ans/ans2), 1))
#This is for interest, the if statements are to convert the number to a decimal
def interest():
    ans = input("How much interest? (3% is 3)\n")
    if len(ans) >2:
        ans = float(ans)
    elif len(ans) >1:
        ans = float(f"1.{ans}")
    else:
        ans = float(f"1.0{ans}")
    ans2 = float(input("How much do you have in your account?\n"))
    ans3 = int(input("How many months?\n"))
    while ans3 > 0:
        ans2 = ans2 * ans
        ans3 -= 1
    return (f"You will have {ans2} after {ans3} weeks")
#This is for budget allocator, the if statements are to convert the numbers to decimals
def budget():
    ans = float(input("How much it your weekly income?\n"))
    ans2 = input("What percent of your income is your first type of allocation? (3% is 3)\n")
    ans3 = input("What percent of your income is your second type of allocation? (3% is 3)\n")
    if len(ans2) >1:
        ans2 = float(f"0.{ans2}")
    else:
        ans2 = float(f"0.0{ans2}")
    ans2 = ans*ans2
    print(f"The amount of your budget for your first allocation is {ans2}")
    if len(ans3) >1:
        ans3 = float(f"0.{ans3}")
    else:
        ans3 = float(f"0.0{ans3}")
    ans3 = ans*ans3
    print(f"The amount of your budget for your first allocation is {ans2}")
    return (f"The amount of your budget for your second allocation is {ans3}")
#This is for sale price, the if statements are to convert the number to decimal
def sale():
    ans = float(input("What is the manufacturing price?\n"))
    ans2 = input("What percent profit would you like to make? (3 is 3%)\n")
    ans3 = ans2
    if len(ans2) > 2:
        ans2 = float(f"{ans2}")
    elif len(ans2) >1:
        ans2 = float(f"1.{ans2}")
    else:
        ans2 = float(f"1.0{ans2}")
    ans2 = ans*ans2
    return (f"For {ans3}% profit, the price should be {ans2}")
#This is for tip, the if statements are to convert the number to a decimal
def tip():
    ans = float(input("What is the price of the object?\n"))
    ans2 = input("How much percent tip? (3 is 3%)\n")
    ans3 = ans2
    if len(ans2) > 2:
        ans2 = float(f"{ans2}")
    elif len(ans2) >1:
        ans2 = float(f"1.{ans2}")
    else:
        ans2 = float(f"1.0{ans2}")
    ans2 = ans*ans2
    return (f"For {ans3}% tip, the price should be {ans2}")
def main():
    ans = int(input("What would you like to do?\n1 for time to goal\n2 for interest\n3 for budget allocator\n4 for sale price\n5 for tip calculator\n"))
    if ans == 1:
        return add()
    elif ans == 2:
        return interest()
    elif ans == 3:
        return budget()
    elif ans == 4:
        return sale()
    elif ans == 5:
        return tip()
    else:
        print("Invalid number.")
        return
    
main()