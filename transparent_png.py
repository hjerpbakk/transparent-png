#!/usr/bin/env python
import sys
from os import path
from PIL import Image, ImageDraw
import subprocess
from shutil import which

def createTransparentImage():
    """Creates a transparent image of the size given by two command line arguments."""
    x = 1
    y = 2
    if (len(sys.argv) < 3 or (len(sys.argv) == 4 and sys.argv[1] != "-o") or len(sys.argv) > 4):
        print("transparent_png creates a transparent PNG of the given size.")
        print()
        print("Usage:")
        print("  python transparent_png.py [OPTION] [X] [Y]")
        print()
        print("Options:")
        print("  -o Optimizes the created image using ImageOptim if available or PNGOUT")
        print()
        print("Example:")
        print("  python transparent_png.py -o 70 50")
        return 1
    
    if (sys.argv[1] == "-o"):
        x = 2
        y = 3

    blank_image = Image.new('RGBA', (int(sys.argv[x]), int(sys.argv[y])), (255,255,255,0))
    ImageDraw.Draw(blank_image)
    imagePath = sys.argv[x] + "x" + sys.argv[y] + ".png"
    blank_image.save(imagePath)
    print("Created " + imagePath)

    if (len(sys.argv) == 4):
        # Tries to use ImageOptim on macOS and falls back to PNGOUT on other OSes
        if (which("open") is not None):
            print("Minifiying image using ImageOptim...")
            worked = subprocess.call(["open", "-a", "ImageOptim", imagePath])
            if (worked != 0):
                optimizeUsingPNGOUT(imagePath)
        else:        
            optimizeUsingPNGOUT(imagePath)
    return 0

def optimizeUsingPNGOUT(imagePath):
    print("Optimizing image using PNGOUT...")
    subprocess.call(["pngout", "-r", imagePath])

createTransparentImage()