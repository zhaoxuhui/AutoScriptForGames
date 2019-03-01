# coding=utf-8
import baseFunctions as bf
import cv2
import time


def openYysAuto():
    img_start = cv2.imread("yys/01.png", cv2.IMREAD_GRAYSCALE)
    img_mumu = cv2.imread("yys/02.png", cv2.IMREAD_GRAYSCALE)
    img_yys = cv2.imread("yys/03.png", cv2.IMREAD_GRAYSCALE)
    img_announce = cv2.imread("yys/04.png", cv2.IMREAD_GRAYSCALE)
    img_enter = cv2.imread("yys/05.png", cv2.IMREAD_GRAYSCALE)

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
        yys = bf.findLocWithKp(img_yys)
        if yys[0] != 0 and yys[1] != 0:
            break
        if counter > 15:
            exit()
        time.sleep(5)
    print "opening game..."

    bf.animateMoveAndClick(bf.getCurPos(), yys)
    time.sleep(15)
    bf.animateMoveAndClick(bf.getCurPos(), yys)
    time.sleep(10)
    announce = bf.findLocWithKp(img_announce)
    bf.animateMoveAndClick(bf.getCurPos(), (announce[0], announce[1] - 80))
    time.sleep(1)
    enter = bf.findLocWithKp(img_enter)
    bf.animateMoveAndClick(bf.getCurPos(), enter)
    time.sleep(5)
    bf.animateMoveAndClick(bf.getCurPos(), enter)
    time.sleep(8)


def juexingAuto(type, times=5):
    img_explore = cv2.imread("yys/06.png", cv2.IMREAD_GRAYSCALE)
    img_juexing = cv2.imread("yys/07.png", cv2.IMREAD_GRAYSCALE)
    img_huo = cv2.imread("yys/08.png", cv2.IMREAD_GRAYSCALE)
    img_feng = cv2.imread("yys/09.png", cv2.IMREAD_GRAYSCALE)
    img_shui = cv2.imread("yys/10.png", cv2.IMREAD_GRAYSCALE)
    img_lei = cv2.imread("yys/11.png", cv2.IMREAD_GRAYSCALE)
    img_challenge = cv2.imread("yys/12.png", cv2.IMREAD_GRAYSCALE)
    img_prepare = cv2.imread("yys/13.png", cv2.IMREAD_GRAYSCALE)
    img_confirm = cv2.imread("yys/14.png", cv2.IMREAD_GRAYSCALE)
    img_close = cv2.imread("yys/15.png", cv2.IMREAD_GRAYSCALE)
    img_back = cv2.imread("yys/16.png", cv2.IMREAD_GRAYSCALE)

    time.sleep(4)
    explore = bf.findLocWithKp(img_explore)
    bf.animateMoveAndClick(bf.getCurPos(), explore)
    time.sleep(5)
    juexing = bf.findLocWithKp(img_juexing)
    bf.animateMoveAndClick(bf.getCurPos(), juexing)
    time.sleep(3)

    if type == 1:
        exe_type = bf.findLocWithKp(img_huo)
    elif type == 2:
        exe_type = bf.findLocWithKp(img_feng)
    elif type == 3:
        exe_type = bf.findLocWithKp(img_shui)
    elif type == 4:
        exe_type = bf.findLocWithKp(img_lei)

    bf.animateMoveAndClick(bf.getCurPos(), exe_type)
    time.sleep(2)

    for i in range(times):
        print i + 1, '/', times
        challenge = bf.findLocWithKp(img_challenge)
        bf.animateMoveAndClick(bf.getCurPos(), challenge)
        time.sleep(10)
        prepare = bf.findLocWithKp(img_prepare)
        bf.animateMoveAndClick(bf.getCurPos(), prepare)
        time.sleep(50)

        counter = 0
        while True:
            print "waiting..."
            counter += 1
            confirm = bf.findLocWithKp(img_confirm)
            if confirm[0] != 0 and confirm[1] != 0:
                break
            if counter > 15:
                exit()
            time.sleep(5)
        bf.animateMoveAndClick(bf.getCurPos(), confirm)
        time.sleep(3)
    close = bf.findLocWithKp(img_close)
    bf.animateMoveAndClick(bf.getCurPos(), close)
    time.sleep(2)
    back = bf.findLocWithKp(img_back)
    bf.animateMoveAndClick(bf.getCurPos(), back)


if __name__ == '__main__':
    openYysAuto()
    juexingAuto(1, 2)
    juexingAuto(2, 1)
    juexingAuto(3, 1)
    juexingAuto(4, 1)
