from PIL import Image
import sys

import pyocr
from pyocr.builders import DigitBuilder,TextBuilder

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
# The tools are returned in the recommended order of usage
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))
# Ex: Will use tool 'libtesseract'

langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
lang = langs[0]
# print("Will use lang '%s'" % (lang))
# Ex: Will use lang 'fra'
# Note that languages are NOT sorted in any way. Please refer
# to the system locale settings for the default language
# to use.

import numpy as np

from PIL import Image, ImageDraw, ImageFont

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
def get_img(n, img_sz):
  im = np.ones(img_sz)
  im[:,:]=255
  pil_im = Image.fromarray(im)
  draw = ImageDraw.Draw(pil_im)
  font = ImageFont.truetype("DejaVuSans.ttf", size=12)
  sz = font.getsize(str(n))
  draw.text((img_sz[1]-sz[0], 2), str(n), font=font,fill=0)
  im = np.asarray(pil_im)
  return im

import cv2
count = 0
with open('a.txt','w') as  f:
    for i in range(10000):
        text = np.random.randint(0, 4999999, dtype=np.int)
        im = get_img(text, (15,60))
        # im.show()
        im = cv2.resize(im,(120,40)) #调整分辨率，直到将字符都识别对
        i_n = str(i)+'.jpg'
        # plt.imsave(i_n,np.array(im))
        cv2.imwrite(i_n,im)
        f.write(i_n)
        f.write('\n')   
        digits = tool.image_to_string(
            Image.fromarray(im),
            lang='eng',
            builder=DigitBuilder(tesseract_layout=3),
        )
        print(str(text),'---', digits)
        if str(text) in digits:
            count+=1
print(count)
#
# print(digits)

 # tesseract a.txt ./ --oem 0 -l eng -c tessedit_char_whitelist=0123456789
