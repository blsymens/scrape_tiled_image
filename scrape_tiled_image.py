from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt
url_base = 'https://search.arch.be/imageserver/getpic.php?550/550_0001_000/550_0001_000_02888_000/550_0001_000_02888_000_0_0003.jp2&'

def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

start = 218
length = 31
width = 20

for col in range(0,width):
    start = 218+length*col
    stop = start+length
    response = requests.get(url_base + str(start))
    img_first = Image.open(BytesIO(response.content))
    dst_temp = img_first
    print('Row: '+str(start)+' Col: '+str(col))

    for index in range(start+1, stop):
        response = requests.get(url_base + str(index))
        img_tile = Image.open(BytesIO(response.content))
        dst_temp = get_concat_h(dst_temp,img_tile)
        print('Row: '+str(index)+' Col: '+str(col))
    
    if col ==0:
        dst = dst_temp

    elif col>0:
        dst = get_concat_v(dst,dst_temp)


# dst.save('pillow_essen.jpg',quality=100, subsampling=0)