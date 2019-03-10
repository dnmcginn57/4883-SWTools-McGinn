"""
David McGinn
6 March 2019
4883 SWTools
This program converts an image to ASCII art, but in a creative manner
"""

import os
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

"""
returns the best character to use depending on the 
value of the color passed in,
lower value = a more full character
higher value = a less full character

depending on how this turns out perhaps tuning the character to the alpha channel could be good too
"""
def value_lookup(pColor):
    #ordered from darkest to lightest with respect to the "Sushi Sushi" font from dafont
    custom_chars = ['G', 'K', 'A', '.', 'M', 'u', '|', 's', 'Z', 'E', '$']
    r,g,b,a = pColor
    value = int((r+b+g)/3)
    c = custom_chars[value // 25]

    return c

"""
Creats & returns a list of ascii characters to represent the image
"""
def image_to_ascii(**kwargs):

    path = kwargs.get('path','./input_images/sock_cat.jpg')
    outPath = kwargs.get('outPath','./output_images/asciiimage.png')
    fntPath = kwargs.get('fntPath','/usr/share/fonts/truetype/SushiSushi.ttf')
    fntSize = int(kwargs.get('fntSize',12))


    im = Image.open(path)
    #a given image may not always be RGBA
    rgb_im = im.convert('RGBA')

    pixels = rgb_im.load()

    w,h = im.size

    newIm = Image.new('RGBA', im.size, (255,255,255,255))

    #font declaration
    fnt = ImageFont.truetype(fntPath, fntSize)

    drawOnMe = ImageDraw.Draw(newIm)

    for y in range(h):
        #spacing  between letters, no spacing creates a perfect image, and where's the fun in that?
        if(y % (fntSize - 2) == 0):
            for x in range(w):
                if(x % (fntSize - 2) == 0):
                    #faster than doing get pixel each time
                    pColor = pixels[x,y]
                    drawOnMe.text((x,y), value_lookup(pColor), font=fnt, fill=pColor)


    #save image to output folder
    newIm.save(outPath)




if(len(sys.argv) == 5):
    image_to_ascii(path=sys.argv[1],outPath=sys.argv[2],fntPath=sys.argv[3],fntSize=sys.argv[4])
else:
    print("\ninvalid number of arguments, running demonstration")
    image_to_ascii()
