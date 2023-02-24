import pyautogui
import time
text = 0
my_text = ""
while text < 10 :
    time.sleep(2)
    if text <5:
        my_text = "I Love You"
    else:
        my_text = "I Missing You"
    pyautogui.typewrite(my_text)
    pyautogui.press("enter")
    text += 1