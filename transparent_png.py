#!/usr/bin/env python
import sys
from os import path
from PIL import Image, ImageDraw

def createTransparentImage():
    """Creates a transparent image of the size given by two command line arguments."""
    if (len(sys.argv) != 3):
        print("X and Y must be specified as arguments. Example: python transparent_png 100 70")
        return 1
    
    blank_image = Image.new('RGBA', (int(sys.argv[1]), int(sys.argv[2])), (255,255,255,0))
    ImageDraw.Draw(blank_image)
    imagePath = path.abspath(sys.argv[1] + "x" + sys.argv[2] + ".png")
    blank_image.save(imagePath)
    print("Created " + imagePath)
    return 0

createTransparentImage()