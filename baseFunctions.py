# coding=utf-8
import win32api, win32gui, win32con
from ctypes import *
import time
from PIL import ImageGrab as ig
import cv2
import numpy as np

SCREEN_SCALE_FACTOR = 1.25


def getCurPos():
    return win32gui.GetCursorPos()


def getPos():
    while True:
        res = getCurPos()
        print res
        time.sleep(1)


def clickLeft():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def movePos(x, y):
    windll.user32.SetCursorPos(x, y)


def animateMove(curPos, targetPos, durTime=1, fps=60):
    x1 = curPos[0]
    y1 = curPos[1]
    x2 = targetPos[0]
    y2 = targetPos[1]
    dx = x2 - x1
    dy = y2 - y1
    times = int(fps * durTime)
    dx_ = dx * 1.0 / times
    dy_ = dy * 1.0 / times
    sleep_time = durTime * 1.0 / times
    for i in range(times):
        int_temp_x = int(round(x1 + (i + 1) * dx_))
        int_temp_y = int(round(y1 + (i + 1) * dy_))
        windll.user32.SetCursorPos(int_temp_x, int_temp_y)
        time.sleep(sleep_time)
    windll.user32.SetCursorPos(x2, y2)


def animateMoveAndClick(curPos, targetPos, durTime=1, fps=60, waitTime=1):
    x1 = curPos[0]
    y1 = curPos[1]
    x2 = targetPos[0]
    y2 = targetPos[1]
    dx = x2 - x1
    dy = y2 - y1
    times = int(fps * durTime)
    dx_ = dx * 1.0 / times
    dy_ = dy * 1.0 / times
    sleep_time = durTime * 1.0 / times

    for i in range(times):
        int_temp_x = int(round(x1 + (i + 1) * dx_))
        int_temp_y = int(round(y1 + (i + 1) * dy_))
        windll.user32.SetCursorPos(int_temp_x, int_temp_y)
        time.sleep(sleep_time)
    windll.user32.SetCursorPos(x2, y2)
    time.sleep(waitTime)
    clickLeft()


def getSiftKps(img, numKps=2000):
    """
    获取SIFT特征点和描述子

    :param img: 读取的输入影像
    :param numKps:期望提取的特征点个数，默认2000
    :return:特征点和对应的描述子
    """
    sift = cv2.xfeatures2d_SIFT.create(nfeatures=numKps)
    kp, des = cv2.xfeatures2d_SIFT.detectAndCompute(sift, img, None)
    return kp, des


def flannMatch(kp1, des1, kp2, des2):
    """
    基于FLANN算法的匹配

    :param kp1: 特征点列表1
    :param des1: 特征点描述列表1
    :param kp2: 特征点列表2
    :param des2: 特征点描述列表2
    :return: 匹配的特征点对
    """

    good_matches = []
    good_kps1 = []
    good_kps2 = []

    print("kp1 num:" + len(kp1).__str__() + "," + "kp2 num:" + len(kp2).__str__())

    # FLANN parameters
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)  # or pass empty dictionary

    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)

    # 筛选
    for i, (m, n) in enumerate(matches):
        if m.distance < 0.5 * n.distance:
            good_matches.append(matches[i])
            good_kps1.append([kp1[matches[i][0].queryIdx].pt[0], kp1[matches[i][0].queryIdx].pt[1]])
            good_kps2.append([kp2[matches[i][0].trainIdx].pt[0], kp2[matches[i][0].trainIdx].pt[1]])

    if good_matches.__len__() == 0:
        print("No enough good matches.")
        return good_kps1, good_kps2
    else:
        print("good matches:" + good_matches.__len__().__str__())
        return good_kps1, good_kps2


def siftFlannMatch(img1, img2, numKps=2000):
    """
    包装的函数，直接用于sift匹配，方便使用

    :param img1: 输入影像1
    :param img2: 输入影像2
    :param numKps: 每张影像上期望提取的特征点数量，默认为2000
    :return: 匹配好的特征点列表
    """
    kp1, des1 = getSiftKps(img1, numKps=numKps)
    kp2, des2 = getSiftKps(img2, numKps=numKps)
    good_kp1, good_kp2 = flannMatch(kp1, des1, kp2, des2)
    return good_kp1, good_kp2


def findLocWithTemplate(img):
    h = img.shape[0]
    w = img.shape[1]
    screen = ig.grab()
    print "finding location..."
    screen_cv = cv2.cvtColor(np.asarray(screen), cv2.COLOR_RGB2GRAY)
    res = cv2.matchTemplate(screen_cv, img, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    target = (int((max_loc[0] + w / 2) / SCREEN_SCALE_FACTOR), int((max_loc[1] + h / 2) / SCREEN_SCALE_FACTOR))
    return target


def findLocWithKp(img, numKps=4000):
    screen = ig.grab()
    screen_cv = cv2.cvtColor(np.asarray(screen), cv2.COLOR_RGB2GRAY)
    kp1, kp2 = siftFlannMatch(img, screen_cv, numKps=numKps)
    if kp1.__len__() == 0 or kp2.__len__() == 0:
        return (0, 0)
    mean_x = 0
    mean_y = 0
    for i in range(kp2.__len__()):
        mean_x += kp2[i][0]
        mean_y += kp2[i][1]
    mean_x = int(mean_x / kp2.__len__())
    mean_y = int(mean_y / kp2.__len__())
    return (mean_x, mean_y)
