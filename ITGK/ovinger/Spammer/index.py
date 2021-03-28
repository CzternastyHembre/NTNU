import pyautogui ,time



def aa():

    for i in range(20):
        pyautogui.click()
        time.sleep(0.6)

    for i in range(1000):
        pyautogui.click()
        pyautogui.click()
        pyautogui.click()
        pyautogui.click()
        pyautogui.click()
        pyautogui.click()
        pyautogui.click()
        pyautogui.click()
        time.sleep(7)
        print(i, end= " ")

    for i in range(1000):
        pyautogui.click()
        time.sleep(0.6)


print('stating in: ', end='')
for i in range(5,0,-1):
    print(i,'', end='')
    time.sleep(1)

#aa()
def bb() :

    for i in range(3000):
        pyautogui.click()
        pyautogui.click()
        pyautogui.click()
        pyautogui.click()
        time.sleep(3)
        if i % 10 == 0:
            print(i)
    for i in range(100):
        for i in range(100):
            pyautogui.click()
            if i % 10 == 0:
                print(i)
        for i in range(100):
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            time.sleep(3)
            if i % 10 == 0:
                print(i)
#bb()
a = int(30)
for i in range(a):
    pyautogui.click()
    time.sleep(0.2)
    if i % 10 == 0:
        print(i)

#x, y = 740, 1045

#for i in range(1):
 #   f = open('textfil', 'r')
  #  for line in f.readlines():
   #     pyautogui.moveTo(x, y, duration=2, tween=pyautogui.easeInOutQuad)
    #    pyautogui.click()

#        pyautogui.write(line, interval=0.1)

 #       pyautogui.moveTo(x, y, tween=pyautogui.easeInOutQuad)
  #      pyautogui.click()

   #     pyautogui.press('enter')
   # f.close()
screenWidth, screenHeight = pyautogui.size()  # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)
currentMouseX, currentMouseY = pyautogui.position()  # Returns two integers, the x and y of the mouse cursor's current position.
print(currentMouseX, currentMouseY)

