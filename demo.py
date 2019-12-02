from PIL import Image
import sys
import pyocr
import pyocr.builders
import argparse
import base64
from io import BytesIO

def pil_base64(image):    
    img_buffer = BytesIO()    
    image.save(img_buffer, format='JPEG')    
    byte_data = img_buffer.getvalue()    
    base64_str = base64.b64encode(byte_data)
    s = base64_str.decode()    
    return s  

def imgfilter(image):
    imcut = image.crop((args.n[0],args.n[1],args.n[2],args.n[3]))
    im = imcut.convert('L')

    threshold = 124
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    im2 = im.point(table, '1')
    return im2

def ocrec(image):
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        sys.exit(1)
    tool = tools[0]
    #print("Will use tool '%s'" % (tool.get_name()))
    langs = tool.get_available_languages()
    #print("Available languages: %s" % ", ".join(langs))
    lang = langs[0]
    #print("Will use lang '%s'" % (lang))
    rectxt = tool.image_to_string(
        image,
        lang=lang,
        builder=pyocr.builders.TextBuilder(tesseract_layout=6)
    )
    txt = rectxt.replace(" ", "")
    return txt


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='python demo.py -p PicturePath -s xleftup,yleftup,xrightdown,yrightdown')
    parser.add_argument("-p", type=str, default="test.jpg")
    parser.add_argument("-n", nargs='+', type=int,default=[150,240,1183,514] )
    args = parser.parse_args()

    imraw = Image.open(args.p)
    #imraw.show()
    im = imgfilter(imraw)
    im.show()
     
    imb64 = pil_base64(im)
    result = ocrec(im)
    print(result,imb64)
