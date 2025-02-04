import keyboard
import time
cnt = 0
cnt2 = []
time.sleep(4.5)

while cnt < 100:
    time.sleep(0.5)
    nm = 48 + cnt
    for x in cnt2:
        #keyboard.write("    ")
        time.sleep(0.5)
    keyboard.write(f'''"lst{nm}": {{}}''')
    time.sleep(0.5)
    keyboard.send("left_arrow")
    time.sleep(1)
    keyboard.send("enter")
    cnt2.append(cnt)
    print(cnt)
    cnt += 1