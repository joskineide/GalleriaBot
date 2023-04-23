import pydirectinput
from time import sleep
from macro import BaseMenuMacro
from PIL import Image, ImageGrab
import numpy as np
import pyautogui
import cv2

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # sleep(3)
    # print(pyautogui.position())
    # sleep(3)
    # print(pyautogui.position())
    # print("asd")

    base_menu_macro = BaseMenuMacro()

    while True:
        screen = np.array(ImageGrab.grab(bbox=(1975, 135, 2105, 265)))
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

        # print(screen)
        cv2.imshow("", screen)
        if cv2.waitKey(1) == 27:
            break


    # base_menu_macro.reborn_all()
    #
    # base_menu_macro.setup_skill_all()


