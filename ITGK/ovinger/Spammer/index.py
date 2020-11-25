import pyautogui ,time
print('stating in: ', end='')

for i in range(3,0,-1):
    print(i,'', end='')
    time.sleep(1)

x, y = 740, 1045

for i in range(1):
    f = open('textfil', 'r')
    for line in f.readlines():
        pyautogui.moveTo(x, y, duration=2, tween=pyautogui.easeInOutQuad)
        pyautogui.click()

        pyautogui.write(line, interval=0.1)

        pyautogui.moveTo(x, y, tween=pyautogui.easeInOutQuad)
        pyautogui.click()

        pyautogui.press('enter')
    f.close()
screenWidth, screenHeight = pyautogui.size()  # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)
currentMouseX, currentMouseY = pyautogui.position()  # Returns two integers, the x and y of the mouse cursor's current position.
print(currentMouseX, currentMouseY)

