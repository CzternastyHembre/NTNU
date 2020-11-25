import pyautogui ,time
print('stating in: ', end='')

for i in range(3,0,-1):
    print(i,'', end='')
    time.sleep(1)


for i in range(100):
    for i in range(3):
        pyautogui.press('right')

