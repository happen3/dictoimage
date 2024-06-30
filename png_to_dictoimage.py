import queue
import threading

from PIL import Image
from dictoimage import Pixel, PixelCanvas
from concurrent.futures import ThreadPoolExecutor, as_completed
import math


# Open the PNG image
image = Image.open('input.png')
image = image.convert('RGBA')

# Get image size
width, height = image.size

# Create a PixelCanvas object based on image size
pxc = PixelCanvas((height, width))
totalx = 0
Canvas = None
# Iterate through each pixel in the image
for y in range(height):
    for x in range(width):
        # Get RGB color tuple for the current pixel
        rgba_color = image.getpixel((x, y))
        if rgba_color[3] <= 127:
            totalx = totalx + 1
            continue

        # Create a Pixel object and add it to the PixelCanvas
        pixel = Pixel(rgba_color, (y, x))
        pxc.AddPixel(pixel.GetPixel())
        print(f"Pixel {totalx} out of {width*height}")
        totalx = totalx + 1
    Canvas = pxc.GetCanvas()
# Print or use pxc.GetCanvas() to retrieve the dictoimage format data
with open("canvas.dim", "w") as fo:
    fo.write(f"{Canvas}")
with open("canvas.dim.hdr", "w") as fo:
    fo.write(f"{pxc.CanvasHeader}")

image.close()
