import dictoimage

Pixel = dictoimage.Pixel
Canvas = dictoimage.PixelCanvas
px = Pixel((255, 0, 0, 0), (0, 0))
pxc = Canvas((2, 2))

print(f"{px.GetPixel()}\n", px.GetPixelColour(), px.GetPixelTransparency(), px.GetPixelPosition())

pxc.AddPixel(px.GetPixel())
pxc.AddPixel(Pixel((0, 255, 0, 0), (0, 1)).GetPixel())
pxc.AddPixel(Pixel((255, 0, 0, 0), (1, 1)).GetPixel())
pxc.AddPixel(Pixel((0, 255, 0, 0), (1, 0)).GetPixel())

print(f"{pxc.GetCanvas()}")

px.Destroy()