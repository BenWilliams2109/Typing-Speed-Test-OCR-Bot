import pyautogui
import pytesseract
import time
from pynput.keyboard import Key, Controller
import keyboard as kb

keyboard = Controller()
width, height = pyautogui.size()
x = width + 16
y = height - 33

p1 = int(0.0827 * x)
p2 = int(0.1818 * y)
p3 = int(0.3081 * x)
p4 = int(0.0753 * y)

print(str(0.0827 * x) + "\n" + str(0.1818 * y) + "\n" + str(0.3081 * x) + "\n" + str(0.0753 * y))
pytesseract.pytesseract.tesseract_cmd = "Insert file location of tesseract.exe here e.g. (r'C:\Program Files\Tesseract-OCR\tesseract.exe')
time.sleep(4)


while True:
    if kb.is_pressed('ENTER'):
        break
    time.sleep(0.5)
    # im = pyautogui.screenshot(region=(480, 284, 465, 185)) #typingtest.com
    # im = pyautogui.screenshot(region=(286, 256, 1065, 106)) #10fastfingers.com
    im = pyautogui.screenshot(region=(p1, p2, p3, p4)) #10fastfingers.com
    # im = pyautogui.screenshot(region=(368, 254, 969, 604)) #typing.com 3-page Character Recognition
    # im = pyautogui.screenshot(region=(30, 462, 933, 90)) #10fast fingers multiplayer
    # im = pyautogui.screenshot(region=(294, 214, 933, 100)) #10 fast fingers competition

    text = pytesseract.image_to_string(im)
    time.sleep(0.01)
    print(text)
    print(type(text))

    text = text.replace("\n", " ")

    list_of_text = list(text)
    print(list_of_text)

    for char in list_of_text:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.04) #Time between each key press, note setting to 0 works but it can be a bit buggy sometimes so i recommend having at least 0.001 seconds delay
