from PIL import Image, ImageColor
import numpy as np
import math

if __name__ == '__main__':
    canvas_width, canvas_height = 960, 960
    x0, y0 = 480, 480
    n = 8
    alpha = 10 * (n + 1) * math.pi / 180
    arr = np.zeros([canvas_height, canvas_width, 3], dtype=np.uint8)
    for x in range(canvas_width):
        for y in range(canvas_height):
            arr[y, x, 0] = 255
            arr[y, x, 1] = 255
            arr[y, x, 2] = 255
    i = 0
    with open('datasets/DS8.txt') as ds:
        for line in ds:
            [y, x] = list(map(int, line.split()))
            x, y = x - x0, y - y0
            x, y = x * math.cos(alpha) - y * math.sin(alpha), x * math.sin(alpha) + y * math.cos(alpha)
            x, y = int(x + x0), int(y + y0)
            y = canvas_height - y - 1
            i += 1
            if 0 <= x < canvas_width and 0 <= y < canvas_height:
                arr[y, x, 0] = 0
                arr[y, x, 1] = 0
                arr[y, x, 2] = 255
    print(i)
    img = Image.fromarray(arr)
    img.save('images/canvas.png')
