import pickle

import cv2
import numpy as np


def extract_colored_pixels(image_path):
    # 读取图像,PNG格式
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    # 创建空列表来存储像素坐标
    colored_pixels = []

    # 遍历每一行和每一列
    for row in range(image.shape[0]):
        for col in range(image.shape[1]):
            # 获取像素值
            r, g, b, a = image[row, col]

            # 如果至少有一个颜色通道有值，就将像素坐标添加到列表中
            if a > 0:
                colored_pixels.append((col, row))

    return colored_pixels


r = extract_colored_pixels("mark.png")
with open("mark.pkl", "wb") as f:
    pickle.dump(r, f)
