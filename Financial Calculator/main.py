#Vincent Johnson financial calculator
#ms larse did a thing
#-Ms. Larose

#By the way, I'm keeping that and adding it to every assignment.
'''
How long it will take to save for a goal based on a weekly or monthly deposit
Compound Interest Calculator 
Budget Allocator (use set percentages to divide an income into spending categories like savings, entertainment, and food)
Sale Price Calculator (apply discounts to prices)
Tip Calculator
'''
rerun = 1


#This is for time to goal, will round for weeks to goal
def add(rerun):
    ans = float(input("What's your goal?\n"))
    ans2 = float(input("How much money depositted per week?\n"))
    print("You need to save", ans2, "per week for", round((ans/ans2), 1), "weeks to get to", ans)
    tlk = int(input("\n1 for menu\n2 for end\n"))
    if tlk == 1:
        rerun = 1
    elif tlk == 2:
        rerun = 0
    else
    return rerun

#This is for interest, the if statements are to convert the number to a decimal
def interest(rerun):
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
    print(f"You will have {ans2} after {ans3} weeks")
    tlk = int(input("\n1 for menu\n2 for end\n"))
    if tlk == 1:
        rerun +=1
    else:
        rerun = 0
    return rerun

#This is for budget allocator, the if statements are to convert the numbers to decimals
def budget(rerun):
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
    print(f"The amount of your budget for your second allocation is {ans3}")
    tlk = int(input("\n1 for menu\n2 for end\n"))
    if tlk == 1:
        rerun +=1
    else:
        rerun = 0
    return rerun

#This is for sale price, the if statements are to convert the number to decimal
def sale(rerun):
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
    print(f"For {ans3}% profit, the price should be {ans2}")
    tlk = int(input("\n1 for menu\n2 for end\n"))
    if tlk == 1:
        rerun +=1
    else:
        rerun = 0
    return rerun

#This is for tip, the if statements are to convert the number to a decimal
def tip(rerun):
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
    print((f"For {ans3}% tip, the price should be {ans2}"))
    tlk = int(input("\n1 for menu\n2 for end\n"))
    if tlk == 1:
        rerun +=1
    else:
        rerun = 0
    return rerun

#The main function to choose which function to do
def main(rerun):
    if rerun < 1:
        return("Goodbye")
    ans = int(input("\n\nWhat would you like to do?\n1 for time to goal\n2 for interest\n3 for budget allocator\n4 for sale price\n5 for tip calculator\n"))
    if ans == 1:
        return add(rerun)
    elif ans == 2:
        return interest(rerun)
    elif ans == 3:
        return budget(rerun)
    elif ans == 4:
        return sale(rerun)
    elif ans == 5:
        return tip(rerun)
    else:
        return("Invalid number.")
while True:
    if rerun > 0:
        main(rerun)
    else:
        break