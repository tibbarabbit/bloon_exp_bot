import pyautogui
import time
import keyboard


class Monkey:
    def __init__(self, name, hotkey, place_img_path):
        self.name = name
        self.hotkey = hotkey
        self.place_img_path = place_img_path

    def place_monkey(self):
        place_monkey = pyautogui.locateOnScreen(self.place_img_path, confidence = 0.75)
        place_monkey_center = pyautogui.center(place_monkey)
        # pyautogui.move(place_monkey_center)
        # time.sleep(.5)
        keyboard.press(self.hotkey)
        time.sleep(.5)
        keyboard.release(self.hotkey)
        time.sleep(.5)
        # print(self.hotkey)
        pyautogui.click(place_monkey_center)
        time.sleep(.5)
        return place_monkey_center

    def upgrade():
        top_path = "f1"
        middle_path = "f2"
        bottom_path = "f3"


dart_monkey = Monkey('dart monkey', 'q', 'img/place_boomer.png')
# boomerang_monkey = Monkey('boomerang monkey', 'w')
sniper_monkey = Monkey('sniper monkey', 'z', 'img/place_sniper.png')
bomb_shooter = Monkey('bomb_shooter', 'e', 'img/place_boomer.png')
bomb_shooter_no2 = Monkey('bomb_shooter_no2', 'e', 'img/place_boomer_no2.png')
quency = Monkey('quency', 'u', 'img/place_hero.png')
