import pyautogui, time
time.sleep(5)
f = open("spamtxt.txt", "r")
for word in f:
    pyautogui.typewrite(word)
