"""
@author: Francis | 韩 心 海
@contact: xinhai_han@icloud.com
@file: ct.py
@date: 2020/11/12 11:00 下午

# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
             ┏┓   ┏┓
            ┏┛┻━━━┛┻━━┓
            ┃    ☃    ┃
            ┃  ┳┛  ┗┳ ┃
            ┃     ┻   ┃
            ┗━┓     ┏━┛
              ┃     ┗━━━━━┓
              ┃  神兽保佑  ┣┓
              ┃　永无BUG！ ┏┛
              ┗━━━┓┓┏━━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import cv2
import numpy as np


def get_red(img):
    redImg = img[:, :, 2]
    return redImg


def get_green(img):
    greenImg = img[:, :, 1]
    return greenImg


def get_blue(img):
    blueImg = img[:, :, 0]
    return blueImg


if __name__ == '__main__':
    img = cv2.imread("data/pic2.jpg")
    b, g, r = cv2.split(img)
    zeros = np.zeros(img.shape[:2], dtype="uint8");  # 创建与image相同大小的零矩阵
    # cv2.imshow("Blue 1", b)
    # cv2.imshow("Green 1", g)
    # cv2.imshow("Red 1", r)
    b = get_blue(img)
    g = get_green(img)
    r = get_red(img)
    # cv2.imshow("Blue 2", cv2.merge([b, zeros, zeros]))
    # cv2.imshow("Green 2", g)
    # cv2.imshow("Red 2", r)
    # cv2.imshow("Back", cv2.merge([b, g, r]))
    cv2.imshow("Back", img)
    print(img[95])
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #
    # merged = cv2.merge([b, g, r])
    # print(merged)
