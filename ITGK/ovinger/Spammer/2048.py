import pyautogui ,time
print('stating in: ', end='')

for i in range(3,0,-1):
    print(i,'', end='')
    time.sleep(1)


for i in range(50):
    for i in range(5):
        pyautogui.press('right')
        pyautogui.press('right')
        pyautogui.press('down')
    pyautogui.press('up')


