#-*- coding:utf-8 -*-

import os
import re
from PIL import Image

def get_imlist(path):
    """返回目录中所有png图像的文件名列表"""
    return [os.path.join(path,f) for f in os.listdir(path) if (f.endswith(".PNG") | f.endswith(".JPG"))]

def save_change(save_dir,n,x1,y1,x2,y2):
    box = (x1,y1,x2,y2)
    region = pil_im.crop(box)

    out = region.resize((1125,4000))
    save_dir = save_dir + str(n) + ".PNG"
    print save_dir
    out.save(save_dir)


if __name__ == "__main__":

    path = "./images/original/"
    listdir = get_imlist(path)

    Image.MAX_IMAGE_PIXELS = 2300000000

    for dir in listdir:
        infile = os.path.splitext(dir)[0]
        infile = infile.replace("original","result")
        save_dir = infile + "_"
        print save_dir

        pil_im = Image.open(dir)
        maxcount = pil_im.height / 4000

        for x in xrange(0, maxcount+1):
            save_change(save_dir,x+1, 0, 4000*x, 1125, 4000*(x+1))
            pass
