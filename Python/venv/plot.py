# This program plots the Mandelbrot set on the screen using the Pillow library
# Escape time algorithm used for creating the image
# To add colour to the image we use HSV (Hue, Saturation, Value) coloring instead
# of RGB. This way we can colour the image making the Hue value dependent on the number
# of iterations.

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

im = Image.new('HSV', (WIDTH, HEIGHT), (0, 0, 0))
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
        hue = int(255 * m / MAX_ITER)
        saturation = 255
        value = 255 if m < MAX_ITER else 0

        draw.point([x, y], (hue, saturation, value))

im.convert('RGB').save('mandelbrot_colour.png', 'PNG')
