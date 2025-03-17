from profile import profiles
import csv
import random
import time

def game():
    valid_prfl, enmy_prfl, base_prfl, enmy_base_prfl = profiles()
    input('Press anything to continue...\n')
    win = 1
    if valid_prfl == 'None':
        game()
    turn = random.randint(1,2)

    def cmbt(win, turn):

        def combat_you(win, turn):
            print('\n\nYour turn\n')
            input('Press anything to continue...\n')
            time.sleep(1)
            if random.randint(0,100) <= valid_prfl[6]:
                heal = random.randint(4,10)
                valid_prfl[5] += heal
                if valid_prfl[5] > base_prfl[5]:
                    valid_prfl[5] = base_prfl[5]
                print(f'You healed {heal} HP, your health is now {valid_prfl[5]}')
            
            time.sleep(1)
            damage = valid_prfl[2]
            chnce = random.randint(1,5)
            if chnce <= 2:
                damage = round(damage * 0.25)
                print('Indirect hit, damage reduced')
            
            time.sleep(1)
            if random.randint(0,100) <= int(enmy_prfl[4]):
                print('The enemy dodged the attack!')
                damage = 0
            else:
                print('The enemy did not dodge the attack')
            
            time.sleep(1)
            if random.randint(0,100) <= (enmy_prfl[3]):
                print('Enemy armour negated some damage!')
                damage = damage * random.uniform(0,0.8)
                damage = round(damage)
            else:
                print('Enemy armour did not negate damage')
            time.sleep(1)
            
            enmy_prfl[5] = enmy_prfl[5] - damage

            if damage < valid_prfl[2]:
                print('\n\n')
            print(f'They took {damage} damage!\nEnemy is currently at {enmy_prfl[5]} health!')
            turn = 1
            time.sleep(1)
            if enmy_prfl[5] <= 0:
                print('You won!')
                ans = ''
                while not isinstance(ans, int):
                    ans = input('''What stat would you like to improve?
    Damage (1)
    Armour (2)
    Dodge (3)
    Health (4)
    Regen (5)
''')
                    try:
                        if int(ans) > 5:
                            ans = 'Inv'
                        ans = int(ans)
                    except:
                        print('Invalid input!')

                if ans == 1:
                    base_prfl[2] += 3
                    print(f'Damage improved to {base_prfl[2]}')
                elif ans == 2:
                    base_prfl[3] += 3
                    print(f'Armour improved to {base_prfl[3]}')
                elif ans == 3:
                    base_prfl[4] += 3
                    print(f'Dodge improved to {base_prfl[4]}')
                elif ans == 4:
                    base_prfl[5] += 3
                    print(f'Health improved to {base_prfl[5]}')
                elif ans == 5:
                    base_prfl[6] += 3
                    print(f'Regen improved to {base_prfl[6]}')

                existing_data = [['NAME','CLASS','DAMAGE','ARMOUR','DODGE','HEALTH','REGEN']]
                with open('Battle Simulator/profiles.csv', 'r') as file:
                    read = csv.reader(file)
                    next(read)
                    for row in read:
                        if row[0].upper() == base_prfl[0].upper():
                            row = base_prfl
                        existing_data.append(row)

                with open('Battle Simulator/profiles.csv', 'w', newline='') as file:
                    write = csv.writer(file)
                    write.writerows(existing_data)
                
                win = 0
            turn = 2
            return win, turn

        def combat_enemy(win, turn):
            print('\n\nEnemy turn\n')
            input('Press anything to continue...\n')
            time.sleep(1)
            if random.randint(0,100) <= enmy_prfl[6]:
                heal = random.randint(4,10)
                enmy_prfl[5] += heal
                if enmy_prfl[5] > enmy_base_prfl[5]:
                    enmy_prfl[5] = enmy_base_prfl[5]
                print(f'Enemy healed {heal} HP, their health is now {valid_prfl[5]}')
            time.sleep(1)
            damage = enmy_prfl[2]
            chnce = random.randint(1,5)
            if chnce == 2:
                damage = round(damage * 0.75)
                print('Indirect hit, damage reduced')
            elif chnce == 3:
                damage = round(damage * 0.5)
                print('Indirect hit, damage reduced')
            elif chnce >= 4:
                damage = round(damage * 0.25)
                print('Indirect hit, damage reduced')
            
            if random.randint(0,100) <= valid_prfl[4]:
                print('You dodged the attack!')
                damage = 0
            else:
                print('You did not dodge the attack')
            time.sleep(1)
            if random.randint(0,100) <= valid_prfl[3]:
                print('Your armour negated some damage!')
                damage = damage * random.uniform(0,0.8)
                damage = round(damage)
            else:
                print('Your armour did not negate damage')
            time.sleep(1)
            valid_prfl[5] = valid_prfl[5] - damage

            if damage < enmy_prfl[2]:
                print('\n\n')
            print(f'You took {damage} damage!\nYou are currently at {valid_prfl[5]} health!')
            turn = 1

            if valid_prfl[5] <= 0:
                print('You lost')
                win = 0
            return win, turn
        

        
        if turn == 1:
            win, turn = combat_you(win, turn)
        else:
            win, turn = combat_enemy(win, turn)
        return win, turn
    print(f'You are facing {enmy_prfl[0]}!')
    while win > 0:
        win, turn = cmbt(win, turn)
    return ('Thanks for playing!')