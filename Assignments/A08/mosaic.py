"""
David McGinn
4883-Software-Tools
4-1-19

This program turns a given image into a mosaic of emojis
picture_rgb.json MUST exist to use this file
run dominant.py to create picture_rgb.json
"""

import cv2
import numpy as np
from sklearn.cluster import KMeans
from PIL import Image, ImageDraw,ImageFilter
import sys, os
import pprint
import requests
from math import sqrt
import json


def place_images(impath,outpath,tiles,sub_size):
    """
    function loops through all pixels, and place the emoji with the closest color
    Accepts:
        impath: str
        tiles: dictionary
    Returns:
        
    """
    
    #original image
    im = Image.open(impath)
    im = im.convert('RGBA')

    pixels = im.load()

    w,h = im.size


    #new image will be size of original image * sub image size
    #CHANGE THIS TO A COMMAND LINE ARGUMENT LATER
    new_w = w * sub_size
    new_h = h * sub_size
    newIm = Image.new('RGBA',im.size,(255,255,255,255))

    draw_on_me = ImageDraw.Draw(newIm)

    #done with ranges to allow for spacing
    #each pixel color will be compared to colors stored in the json
    #each pixel is replaced by the closest colored image returned by compare_pixel
    for y in range(h):
        if(y%sub_size == 0):
            for x in range(w):
                if(x%sub_size == 0):
                    p_color = pixels[x,y]
                    matched_tile = compare_pixel(p_color,tiles)
                    matched_tile = matched_tile.resize((sub_size,sub_size), Image.ANTIALIAS)
                    newIm.paste(matched_tile,(x,y))
    #save mosaic
    newIm.save(outpath)


def compare_pixel(color, cand_tiles):
    """
    compares images in a given folder to pixel color
    Accepts:
        color: tuple
        cand_tiles: dictionary

    Returns:
        tile_path: string
    """
    closest = 1.0
    for tile,rgb in cand_tiles.items():
        #open image
        im = Image.open(tile)
        #percent distance
        dist = sqrt( pow((rgb[0]-color[0]),2) + pow((rgb[1]-color[1]),2) + pow((rgb[2]-color[2]),2) )
        dist = dist / sqrt( pow(225,2) + pow(225,2) + pow(225,2) )
        #check to see if new winner
        if(closest > dist):
            closest = dist
            winner = im

    return winner

def open_tile_json():
    """
    opens the json WHICH MUST BE IN THE SAME DIRECTORY
    Returns:
        tiles: dictionary
    """
    try:
        f = open('./picture_rgb.json', "r")
        data = f.read()
        return json.loads(data)
    except IOError:
        print ("can't find json. be sure to run dominant.py first")
        return{}

def process_argv(args):
    """
    returns a dictionary containing processed command line input

    """
    argd = {}
    for arg in args[1:]:
        k,v = arg.split('=')
        argd[k] = v
    return argd

if __name__=='__main__':
    tiles = open_tile_json()
    args = process_argv(sys.argv)
    #change to be from argsv
    #main_image = "../A05/input_images/sock_cat.jpg"
    #output_path = "./output_images/soc_cat_mosaic.png"
    
    main_image = args['input_file']
    if('output_folder' in args):
        output_path = args['output_folder']
    else:
        filename = os.path.basename(main_image)
        name,ext = filename.split('.')
        newname = name + '_mosaic' + '.' + ext
        output_path = './'+newname


    #maybe do this too if you have time
    size = int(args['SubImagesSize'])

    place_images(main_image,output_path,tiles,size)



