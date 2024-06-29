from PIL import Image
from dictoimage import Pixel, PixelCanvas

# Open the PNG image
image = Image.open('input.png')
image = image.convert('RGBA')

# Get image size
width, height = image.size

# Create a PixelCanvas object based on image size
pxc = PixelCanvas((height, width))

# Iterate through each pixel in the image
for y in range(height):
    for x in range(width):
        # Get RGB color tuple for the current pixel
        rgba_color = image.getpixel((x, y))


        # Create a Pixel object and add it to the PixelCanvas
        pixel = Pixel(rgba_color, (y, x))
        pxc.AddPixel(pixel.GetPixel())

# Print or use pxc.GetCanvas() to retrieve the dictoimage format data
with open("example_dim_files/canvas.dim", "w") as fo:
    fo.write(f"{pxc.GetCanvas()}")
with open("example_dim_files/canvas.dim.hdr", "w") as fo:
    fo.write(f"{pxc.CanvasHeader}")

image.close()
