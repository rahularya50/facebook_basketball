# coding=utf-8

from pyautogui import *

time.sleep(0.5)

START_COORDS = (635, 1152)

INITIAL_HOOP_COORDS = (635, 721)
INITIAL_END_COORD = locateOnScreen('img/end.PNG')
HOOP_DELTA = (INITIAL_HOOP_COORDS[0] - INITIAL_END_COORD[0], INITIAL_HOOP_COORDS[1] - INITIAL_END_COORD[1])


def find_hoop_coords():
    x, y, _, _ = locateOnScreen('img/end.PNG')
    return x + HOOP_DELTA[0], y + HOOP_DELTA[1]


def get_target_pos(d):
    x, y = find_hoop_coords()
    return x + d * 2.5, y - 150


def direction():
    try:
        x, y = find_hoop_coords()
        time.sleep(0.1)
        x2, y2 = find_hoop_coords()
        if x2 - x:
            print(x2 - x)
        return x2 - x
    except TypeError:
        print("err")
        return -1


while True:
    a = direction()
    if a:
        b = a
        while a / b > 0 or 0 < abs(a) < 60:
            a = direction()
    moveTo(*START_COORDS)
    dragTo(*get_target_pos(a), duration=0.3)
    time.sleep(3)
    moveTo(*START_COORDS)
