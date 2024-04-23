from PIL import Image, ImageGrab
import pyautogui
import time

screenWidth, screenHeight = pyautogui.size()


def is_cactus(x, y):
    cactus_color = (83, 83, 83)
    pixel = pyautogui.pixel(x, y)
    return pixel == cactus_color


def jump():
    pyautogui.press('space')


def main():
    start_x = 160
    start_y = 710
    time.sleep(3)
    pyautogui.moveTo(start_x, start_y)
    if is_cactus(start_x, start_y):
        jump()
    start_x += 260
    pyautogui.moveTo(start_x, start_y)
    while True:
        if is_cactus(start_x + 10, start_y):
            print("cactus far")
            jump()
        elif is_cactus(start_x, start_y):
            print("cactus mid")
            jump()
        elif is_cactus(start_x - 10, start_y):
            print("cactus close")
            jump()


if __name__ == "__main__":
    main()
