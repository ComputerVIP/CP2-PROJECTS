import csv
def profiles():
    ans = input('What is the name of your character?\n')
    with open('Battle Simulator/profiles.csv', 'r') as file:
        read = csv.reader(file)
        next(read)
        valid_prfl = 'None'
        for row in read:
            if ans.lower() == 'legend':
                print('You cannot  pick this character!')
                pass
            elif ans.lower() == row[0].lower():
                for item in row:
                    print(item)
                    valid_prfl = row
    return valid_prfl