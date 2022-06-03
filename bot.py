import pyautogui
import time
from sqlalchemy import true
import info as monekey
import keyboard
# pyautogui.mouseInfo()

# time.sleep(2)
# im = pyautogui.screenshot()
# om = im.crop((1127, 765, 1146, 775))
# om.save("img/123.png")

# time.sleep(2)


def play_marker():
    time.sleep(1)
    play_marker = pyautogui.locateOnScreen("img/play.png", confidence = 0.8)
    play_marker_center = pyautogui.center(play_marker)
    # play_marker = pyautogui.locateCenterOnScreen("img/play1.png")
    pyautogui.click(play_marker_center)


def expert_marker():
    time.sleep(1)
    expert_marker = pyautogui.locateOnScreen("img/expert.png", confidence = 0.8)
    expert_marker_center = pyautogui.center(expert_marker)
    # expert_marker = pyautogui.locateCenterOnScreen("img/expert.png")
    pyautogui.click(expert_marker_center)


def dark_castle_marker():
    time.sleep(1)
    dark_castle_marker = pyautogui.locateOnScreen("img/dark_castle.png", confidence = 0.8)
    dark_castle_marker_center = pyautogui.center(dark_castle_marker)
    pyautogui.click(dark_castle_marker_center)


def easy_mod():
    time.sleep(1)
    easy_mod_marker = pyautogui.locateOnScreen("img/easy_mod.png", confidence = 0.8)
    easy_mod_marker_center = pyautogui.center(easy_mod_marker)
    pyautogui.click(easy_mod_marker_center)


def standard_mod():
    time.sleep(1)
    standard_mod_marker = pyautogui.locateOnScreen("img/standard_mod.png", confidence = 0.8)
    standard_mod_marker_center = pyautogui.center(standard_mod_marker)
    pyautogui.click(standard_mod_marker_center)


def go_marker():
    go_marker_center = pyautogui.locateCenterOnScreen("img/go.png", confidence = 0.8)
    pyautogui.click(go_marker_center)


def double_go_marker():
    double_go_marker_center = pyautogui.locateCenterOnScreen("img/double_go.png", confidence = 0.8)
    pyautogui.click(double_go_marker_center)


def next_marker():
    next_marker = pyautogui.locateOnScreen("img/next.png", confidence = 0.95)
    next_marker_center = pyautogui.center(next_marker)
    pyautogui.click(next_marker_center)


def home_marker():
    home_marker = pyautogui.locateOnScreen("img/home.png", confidence = 0.95)
    home_marker_center = pyautogui.center(home_marker)
    pyautogui.click(home_marker_center)


def is_round(round):
    try:
        round = "img/round/round" + round + ".png"
        is_round = pyautogui.locateOnScreen(round, confidence = 0.99)
        pyautogui.center(is_round)
        # pyautogui.click(is_round5_center)
        return 1
    except TypeError:
        return -1


def level_up():
    level_up_marker = pyautogui.locateOnScreen("img/level_up.png", confidence = 0.9)
    level_up_marker_center = pyautogui.center(level_up_marker)
    pyautogui.click(level_up_marker_center, 2, 0.5)

######################################################################


while(true):
    while(true):
        try:
            play_marker()
            break
        except TypeError:
            time.sleep(.5)

    try:
        expert_marker()
    except TypeError:
        print("no marker2")

    i = 0
    while (i <= 3):
        try:
            dark_castle_marker()
            break
        except TypeError:
            expert_marker()
            i = i + 1

    try:
        easy_mod()
    except TypeError:
        print("")

    try:
        standard_mod()
    except TypeError:
        print("")

    while(true):
        try:
            quency_location = monekey.quency.place_monkey()
            sniper_monkey_position = monekey.sniper_monkey.place_monkey()
            go_marker()
            double_go_marker()
            break
        except TypeError:
            try:
                level_up()
            except TypeError:
                time.sleep(.5)

    while(true):
        i = is_round("5")
        if (i == 1):
            time.sleep(.1)
            bomb_shooter_position = monekey.bomb_shooter.place_monkey()
            break
        else:
            try:
                level_up()
            except TypeError:
                time.sleep(.5)

    while(true):
        i = is_round("14")
        if (i == 1):
            time.sleep(.1)
            pyautogui.click(bomb_shooter_position)
            time.sleep(.1)
            keyboard.press('f2')
            keyboard.release('f2')
            time.sleep(.1)
            keyboard.press('f2')
            keyboard.release('f2')
            time.sleep(.1)
            keyboard.press('f2')
            keyboard.release('f2')
            time.sleep(.1)
            keyboard.press('f3')
            keyboard.release('f3')
            time.sleep(.1)
            keyboard.press('f3')
            keyboard.release('f3')
            time.sleep(.1)
            keyboard.press('esc')
            keyboard.release('esc')
            break
        else:
            try:
                level_up()
            except TypeError:
                time.sleep(.5)

    while(true):
        i = is_round("22")
        if (i == 1):
            time.sleep(.1)
            pyautogui.click(sniper_monkey_position)
            time.sleep(.1)
            keyboard.press('f2')
            keyboard.release('f2')
            time.sleep(.1)
            keyboard.press('f2')
            keyboard.release('f2')
            time.sleep(.1)
            keyboard.press('f3')
            keyboard.release('f3')
            time.sleep(.1)
            keyboard.press('f3')
            keyboard.release('f3')
            time.sleep(.1)
            keyboard.press('esc')
            keyboard.release('esc')
            break
        else:
            try:
                level_up()
            except TypeError:
                time.sleep(.5)

    while(true):
        i = is_round("27")
        if (i == 1):
            time.sleep(.1)
            bomb_shooter_no2_position = monekey.bomb_shooter_no2.place_monkey()
            pyautogui.click(bomb_shooter_no2_position)
            time.sleep(.1)
            keyboard.press('f3')
            keyboard.release('f3')
            time.sleep(.1)
            keyboard.press('f3')
            keyboard.release('f3')
            time.sleep(.1)
            keyboard.press('f3')
            keyboard.release('f3')
            time.sleep(.1)
            keyboard.press('f1')
            keyboard.release('f1')
            time.sleep(.1)
            keyboard.press('f1')
            keyboard.release('f1')
            time.sleep(.1)
            keyboard.press('esc')
            keyboard.release('esc')
            break
        else:
            try:
                level_up()
            except TypeError:
                time.sleep(.5)

    while(true):
        i = is_round("33")
        if (i == 1):
            time.sleep(.1)
            pyautogui.click(sniper_monkey_position)
            time.sleep(.1)
            keyboard.press('f3')
            keyboard.release('f3')
            time.sleep(.1)
            keyboard.press('esc')
            keyboard.release('esc')
            break
        else:
            try:
                level_up()
            except TypeError:
                time.sleep(.5)

    while(true):
        i = is_round("39")
        if (i == 1):
            time.sleep(.1)
            pyautogui.click(sniper_monkey_position)
            time.sleep(.1)
            keyboard.press('f3')
            keyboard.release('f3')
            time.sleep(.1)
            keyboard.press('esc')
            keyboard.release('esc')
            break
        else:
            try:
                level_up()
            except TypeError:
                time.sleep(.5)

    while(true):
        try:
            next_marker()
            time.sleep(1)
            while(true):
                try:
                    home_marker()
                    break
                except TypeError:
                    try:
                        level_up()
                    except TypeError:
                        time.sleep(.5)
            break
        except TypeError:
            try:
                level_up()
            except TypeError:
                time.sleep(.5)
