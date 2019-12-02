from PIL import Image
from numpy import *
import cv2 as cv

im = array(Image.open('test.jpg').convert('L'))


im2 = 255 - im # 对图像进行反相处理
pil_im = Image.fromarray(im2)
pil_im.save('convertest.png')
pil_im.show()

# im3 = (100.0/255) * im + 100 # 将图像像素值变换到100...200 区间
# pil_im = Image.fromarray(im3)
# pil_im.show()

# im4 = 255.0 * (im/255.0)**2 # 对图像像素值求平方后得到的图像
# pil_im = Image.fromarray(im4)
# pil_im.show()

# imageL = imageraw.convert('L')

# # print('图像的宽：{}'.format(image.size[0]))
# # print('图像的高：{}'.format(image.size[1]))

# width = imageL.size[0]
# height = imageL.size[1]
# image_array = [0] * width * height

# # image_array = np.array(image)
# # print(image_array)

# for h in range(height):
#     for w in range(width):
#         if imageL.getpixel((w,h)) >230:
#             image_array[w+h*width] = 0
#         else:
#             image_array[w+h*width] = 1