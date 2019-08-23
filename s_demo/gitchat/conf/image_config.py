# -*- coding:utf-8 -*-

IMAGES_STORE = '../statics/images'

"""
图片存储
文件系统是当前官方唯一支持的存储系统，但也支持（非公开的） Amazon S3 链接: https://s3.amazonaws.com/ 。
"""

# 图像管道避免下载最近已经下载的图片。使用 IMAGES_EXPIRES 设置可以调整失效期限，可以用天数来指定:
# 90天的图片失效期限
IMAGES_EXPIRES = 90

# 缩略图生成
IMAGES_THUMBS = {
    'small': (100, 100),
    'big': (300, 300),
}

# 滤出小图片, 丢掉那些过小的图片
# 注意：这些尺寸一点也不影响缩略图的生成。
IMAGES_MIN_HEIGHT = 2
IMAGES_MIN_WIDTH = 2