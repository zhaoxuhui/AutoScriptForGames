# coding=utf-8
import baseFunctions as bf
import cv2
import time
import numpy as np
from PIL import ImageGrab as ig


def openBh3Auto():
    img_start = cv2.imread("bh3/01.png", cv2.IMREAD_GRAYSCALE)
    img_mumu = cv2.imread("bh3/02.png", cv2.IMREAD_GRAYSCALE)
    img_beng = cv2.imread("bh3/03.png", cv2.IMREAD_GRAYSCALE)
    img_login = cv2.imread("bh3/04.png", cv2.IMREAD_GRAYSCALE)
    img_message = cv2.imread("bh3/09.png", cv2.IMREAD_GRAYSCALE)
    img_daily = cv2.imread("bh3/17.png", cv2.IMREAD_GRAYSCALE)
    img_confirm = cv2.imread("bh3/18.png", cv2.IMREAD_GRAYSCALE)

    print "opening application..."
    start_menu = bf.findLocWithKp(img_start)
    bf.animateMoveAndClick(bf.getCurPos(), start_menu)
    time.sleep(2)
    mumu = bf.findLocWithKp(img_mumu)
    bf.animateMoveAndClick(bf.getCurPos(), mumu)
    counter = 0
    while True:
        print "waiting..."
        counter += 1
        bengbengbeng = bf.findLocWithKp(img_beng)
        if bengbengbeng[0] != 0 and bengbengbeng[1] != 0:
            break
        if counter > 15:
            exit()
        time.sleep(5)
    print "opening game..."

    bf.animateMoveAndClick(bf.getCurPos(), bengbengbeng)
    counter = 0
    while True:
        print "waiting..."
        login = bf.findLocWithKp(img_login)
        if login[0] != 0 and login[1] != 0:
            break
        if counter > 15:
            exit()
        time.sleep(5)
    bf.animateMoveAndClick(bf.getCurPos(), (login[0] + 300, login[1]))
    time.sleep(8)

    message_box = bf.findLocWithKp(img_message)
    if message_box[0] != 0 and message_box[1] != 0:
        bf.animateMoveAndClick(bf.getCurPos(), message_box)
    time.sleep(2)

    daily = bf.findLocWithKp(img_daily)
    if daily[0] != 0 and daily[1] != 0:
        bf.animateMoveAndClick(bf.getCurPos(), daily)
        time.sleep(1)
        confirm = bf.findLocWithKp(img_confirm)
        bf.animateMoveAndClick(bf.getCurPos(), confirm)
    time.sleep(8)


def collectCoinsAuto():
    img_base = cv2.imread("bh3/05.png", cv2.IMREAD_GRAYSCALE)
    img_coin = cv2.imread("bh3/06.png", cv2.IMREAD_GRAYSCALE)
    img_confirm = cv2.imread("bh3/07.png", cv2.IMREAD_GRAYSCALE)
    img_back = cv2.imread("bh3/08.png", cv2.IMREAD_GRAYSCALE)

    counter = 0
    while True:
        print "waiting..."
        counter += 1
        base = bf.findLocWithKp(img_base)
        if base[0] != 0 and base[1] != 0:
            break
        if counter > 15:
            exit()
        time.sleep(5)
    bf.animateMoveAndClick(bf.getCurPos(), base)
    time.sleep(2)
    coins = bf.findLocWithKp(img_coin)
    bf.animateMoveAndClick(bf.getCurPos(), coins)
    time.sleep(2)
    confirm = bf.findLocWithKp(img_confirm)
    bf.animateMoveAndClick(bf.getCurPos(), confirm)
    time.sleep(2)
    back = bf.findLocWithKp(img_back)
    bf.animateMoveAndClick(bf.getCurPos(), back)
    time.sleep(2)


def adventureAuto():
    img_base = cv2.imread("bh3/05.png", cv2.IMREAD_GRAYSCALE)
    img_adventure = cv2.imread("bh3/14.png", cv2.IMREAD_GRAYSCALE)
    img_refresh = cv2.imread("bh3/11.png", cv2.IMREAD_GRAYSCALE)
    img_back = cv2.imread("bh3/08.png", cv2.IMREAD_GRAYSCALE)
    img_goto = cv2.imread("bh3/10.png", cv2.IMREAD_GRAYSCALE)
    img_onekey = cv2.imread("bh3/12.png", cv2.IMREAD_GRAYSCALE)
    img_confirm = cv2.imread("bh3/13.png", cv2.IMREAD_GRAYSCALE)
    img_home = cv2.imread("bh3/16.png", cv2.IMREAD_GRAYSCALE)

    base = bf.findLocWithKp(img_base)
    bf.animateMoveAndClick(bf.getCurPos(), base)
    time.sleep(2)

    venture = bf.findLocWithKp(img_adventure, numKps=5000)
    bf.animateMoveAndClick(bf.getCurPos(), venture)
    time.sleep(2)

    loc1 = bf.findLocWithKp(img_back)
    loc2 = bf.findLocWithKp(img_refresh)
    y_start = loc1[1]
    y_end = loc2[1]
    print y_start, y_end
    y_range = y_end - y_start

    task1_y_start = int(y_start + 0.194 * y_range)
    task1_y_end = int(y_start + (0.194 + 0.225) * y_range)
    task2_y_start = int(y_start + 0.434 * y_range)
    task3_y_start = int(y_start + 0.673 * y_range)

    screen = ig.grab()
    screen_cv = cv2.cvtColor(np.asarray(screen), cv2.COLOR_RGB2GRAY)
    task1_img = screen_cv[task1_y_start:task1_y_end, :]
    _, kp_task1 = bf.siftFlannMatch(img_goto, task1_img)
    mean_x_task = 0
    mean_y_task = 0
    for i in range(kp_task1.__len__()):
        mean_x_task += kp_task1[i][0]
        mean_y_task += kp_task1[i][1]
    mean_x_task = mean_x_task / kp_task1.__len__()
    mean_y_task = mean_y_task / kp_task1.__len__()

    target1 = (int(mean_x_task), int(task1_y_start + mean_y_task))
    target2 = (int(mean_x_task), int(task2_y_start + mean_y_task))
    target3 = (int(mean_x_task), int(task3_y_start + mean_y_task))

    bf.animateMoveAndClick(bf.getCurPos(), target1)
    time.sleep(2)
    onekey = bf.findLocWithKp(img_onekey)
    bf.animateMoveAndClick(bf.getCurPos(), onekey)
    time.sleep(2)
    confirm = bf.findLocWithKp(img_confirm)
    bf.animateMoveAndClick(bf.getCurPos(), confirm)
    time.sleep(2)

    bf.animateMoveAndClick(bf.getCurPos(), target2)
    time.sleep(2)
    bf.animateMoveAndClick(bf.getCurPos(), onekey)
    time.sleep(2)
    bf.animateMoveAndClick(bf.getCurPos(), confirm)
    time.sleep(2)

    bf.animateMoveAndClick(bf.getCurPos(), target3)
    time.sleep(2)
    bf.animateMoveAndClick(bf.getCurPos(), onekey)
    time.sleep(2)
    bf.animateMoveAndClick(bf.getCurPos(), confirm)
    time.sleep(2)
    home = bf.findLocWithKp(img_home)
    bf.animateMoveAndClick(bf.getCurPos(), home)
    time.sleep(2)


if __name__ == '__main__':
    openBh3Auto()
    collectCoinsAuto()
    adventureAuto()
