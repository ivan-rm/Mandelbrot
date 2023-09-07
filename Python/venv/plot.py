# This program plots the Mandelbrot set on the screen using the Pillow library
# Escape time algorithm used for creating the image

from PIL import Image, ImageDraw
from mandelbrot import mandelbrot, MAX_ITER


# Printed image size in pixels
WIDTH = 1600
HEIGHT = 1200

# Plot a window
RE_START = -2
RE_END = 1
IM_START = -1
IM_END = 1

palette = []

im = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
draw = ImageDraw.Draw(im)

# Plot the pixels on the window
for x in range(0, WIDTH):
    for y in range(0, HEIGHT):
        # Pixel coordinates gets mapped to a complex number
        c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                    IM_START + (y / HEIGHT) * (IM_END - IM_START))
        # Compute the value of z after 100 iterations for the pixel
        m = mandelbrot(c)
        # Make the color dependent on the number of iterations
        color = 255 - int(m * 255 / MAX_ITER)
        draw.point([x, y], (color, color, color))

im.save('mandelbrot.png', 'PNG')