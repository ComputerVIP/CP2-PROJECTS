from profile import profiles
import csv
import random

def game():
    input()
    cnt = 0
    enmy_prfl = []
    valid_prfl = profiles()
    win = 1
    if valid_prfl == "None":
        game()
    with open('Battle Simulator/profiles.csv', 'r') as file:
        read = csv.reader(file)
        next(read)
        for row in read:
            if enmy_prfl == valid_prfl:
                pass
            else:
                enmy_prfl.append(row)
                cnt += 1
        enmy_prfl = enmy_prfl[random.randint(0,cnt)]
        def cmbt(win):
            def combat_t():
                pass
            def combat_u():
                pass
            print(f'You are facing {enmy_prfl[0]}!')
            turn = random.randint(1,2)
            if turn == 1:
                turn = combat_u()
            else:
                turn = combat_t()
            return win
        while win > 1:
            cmbt(win)
        print('You won!')
game()

    