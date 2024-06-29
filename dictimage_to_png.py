from PIL import Image
from dictoimage import *
import ast

with open("example_dim_files/canvas.dim") as fo:
    data = fo.read()
with open("example_dim_files/canvas.dim.hdr") as fo:
    hdr = fo.read()

data = ast.literal_eval(data)
hdr = ast.literal_eval(hdr)

pxc = PixelCanvas(hdr["Size"])
pxc.SetCanvas(data)
# Determine the size of the image based on the PixelCanvas dimensions
canvas_size = pxc.CanvasHeader["Size"]  # Replace with the actual dimensions of your canvas
image_size = (canvas_size[1], canvas_size[0])  # Pillow expects (width, height)

# Create a new image with white background (you can set a different background if needed)
image = Image.new('RGB', image_size, 'white')

# Iterate through the canvas and set pixels in the image
for pixel_dict in pxc.GetCanvas():
    if pixel_dict:
        hex_color = pixel_dict['HexValue']
        position = pixel_dict['Position']
        x, y = position[1], position[0]  # Pillow uses (x, y) coordinates

        # Convert hex color to RGB tuple
        rgb_color = tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))

        # Set the pixel in the image
        image.putpixel((x, y), rgb_color)

# Save the image as PNG
image.save('output.png')
