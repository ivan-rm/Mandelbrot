# This function iterates 100 times through the function f(z) = z^2 + c and returns the result. It takes as an input
# argument the seed value c.

MAX_ITER = 100


def mandelbrot(c):
    z = 0
    n = 0

    while abs(z) <= 2 and n < MAX_ITER:
        z = z * z + c
        n += 1

    return n
