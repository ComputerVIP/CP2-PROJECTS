import csv
import random

def profiles():
    with open('Battle Simulator/profiles.csv', 'r') as file: #Gives a list of every character to choose from
        read = csv.reader(file)
        next(read)
        print('List of characters:')
        for row in read:
            print('    ' + row[0])
    ans = input('What is the name of your character?\n')
    with open('Battle Simulator/profiles.csv', 'r') as file: #This allows you to pick a character
        read = csv.reader(file)
        next(read)
        valid_prfl = 'Inval'
        for row in read:
            if ans.lower() == 'legend':
                print('You cannot  pick this character!')
                valid_prfl = 'None'
                break
            elif ans.lower() == row[0].lower():
                valid_prfl = row
                print(f'''
Stats:
    Name -- {valid_prfl[0]}
    Class -- {valid_prfl[1]}
    Damage -- {valid_prfl[2]}
    Armour -- {valid_prfl[3]}
    Dodge -- {valid_prfl[4]}
    Health -- {valid_prfl[5]}
    Regen -- {valid_prfl[6]}''')
                    
        if valid_prfl == 'Inval':
            valid_prfl = mke_prfl(ans)
    
    enmy_prfl = []
    with open('Battle Simulator/profiles.csv', 'r') as file:
        read = csv.reader(file)
        next(read)
        for row in read:
            if row[0].upper() == valid_prfl[0].upper():
                continue
            enmy_prfl.append(row)
        enmy_prfl = random.choice(enmy_prfl)

    for i in range(len(enmy_prfl)):
        try:
            enmy_prfl[i] = int(enmy_prfl[i])
        except ValueError:
            pass
    for i in range(len(valid_prfl)):
        try:
            valid_prfl[i] = int(valid_prfl[i])
        except ValueError:
            pass
    base_prfl = valid_prfl.copy()
    enmy_base_prfl = enmy_prfl.copy()
    return valid_prfl, enmy_prfl, base_prfl, enmy_base_prfl



def mke_prfl(name):
    with open('Battle Simulator/profiles.csv', 'r') as file:
        read = csv.reader(file)
        next(read)
        for row in read:
            if row[0] == name.upper():
                print('You cannot create a profile that already exists!')
                return

    clss = ''
    while not isinstance(clss, int):
        clss = input('''Choose your class:
    (1) Warrior -- High armour and health, low dodge and decent damage, no regen
    (2) Scout -- High damage and dodge, low health, armour, and regen
    (3) Medic -- Highest regen and health, decent dodge, low damage and armour
    (4) Demoman -- Highest damage and armour, lowest health, no dodge or regen
    (5) Kid -- Middle of the road character with random chances for dodge, regen, and damage
''')
        try:
            if int(clss) > 5:
                clss = 'Inv'
            clss = int(clss)
        except:
            print('Invalid input!')

    if clss == 1:
        clss, damage, armour, dodge, health, regen = 'Warrior', 14, 24, 1, 34, 0
    elif clss == 2:
        clss, damage, armour, dodge, health, regen = 'Scout', 18, 0, 34, 14, 5
    elif clss == 3:
        clss, damage, armour, dodge, health, regen = 'Medic', 10, 4, 10, 40, 21
    elif clss == 4:
        clss, damage, armour, dodge, health, regen = 'Demoman', 32, 32, 0, 4, 0
    elif clss == 5:
        clss, damage, armour, dodge, health, regen = 'Kid', 20, 20, 0, 20, 0

    prfl = [name.upper(), clss.upper(), damage, armour, dodge, health, regen]
    print(f'''
Stats:
    Name -- {prfl[0]}
    Class -- {prfl[1]}
    Damage -- {prfl[2]}
    Armour -- {prfl[3]}
    Dodge -- {prfl[4]}
    Health -- {prfl[5]}
    Regen -- {prfl[6]}''')
    with open('Battle Simulator/profiles.csv', 'a', newline='') as file:
        write = csv.writer(file, lineterminator='\n')
        try:
            write.writerow(prfl)
            print('Character created sucsessfully!')
        except:
            print('Error creating profile')
            return mke_prfl(name)
    return
    