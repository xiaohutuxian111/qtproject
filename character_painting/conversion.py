# -*- coding: utf-8 -*-
# @Time    : 2023/9/18 9:34
# @Author  : stone
# @File    : conversion.py
# @desc    :
import string

from PIL import Image, ImageDraw, ImageFont
import numpy

# 生成图片的缩放比
scale = 1

default_char = string.ascii_letters


def picture_conversion(image_img, export_img=None, input_char='', pix_distance=''):
    """
    :param image_img: 原始图片的路径
    :param export_img: 转换后图片的路径
    :param input_char: 转换的字符
    :param pix_distance: 字符画图片的字符密度 3为清晰，4为一般，5为字符
    :return:
    """
    # 导入图片
    img = Image.open(image_img)
    img_pix = img.load()
    img_width, img_height = img.size[0], img.size[1]
    # 创建画布对象
    canvas_array = numpy.ndarray((img_height * scale, img_width * scale, 3), numpy.uint8)
    # 设置三原色的画布为白色
    canvas_array[:, :, :] = 255
    # 根据画布重新绘制图像
    new_image = Image.fromarray(canvas_array)
    img_draw = ImageDraw.Draw(new_image)
    font = ImageFont.truetype('simsun.ttc', 10)
    # 判断字符使用的类型
    if input_char == '':
        char_list = list(default_char)
    else:
        char_list = list(input_char)
    #  判断窗体的清晰度
    if pix_distance == '清晰':
        pix_distance = 3
    elif pix_distance == '一般':
        pix_distance = 4
    elif pix_distance == '字符':
        pix_distance = 5

    # 开始绘制
    pix_count = 0
    table_len = len(char_list)
    for y in range(len(char_list)):
        for x in range(img_height):
            if x % pix_distance == 0 and y % pix_distance == 0:
                # 实现根据图片像素绘制字符
                img_draw.text((x * scale, y * scale), char_list[pix_count % table_len], img_pix[x, y], font)
                pix_count += 1
    if export_img is not None:
        new_image.save(export_img)
    return False
