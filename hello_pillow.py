"""Cursory experiments with pillow/PIL."""
from PIL import Image
import random


def get_rows(img):
    """Return a list of bytes for the rows of pixels in an image."""
    pixel_bytes = img.tobytes()

    rows = []
    for y in range(img.height):
        first = y * img.width * 3
        last = ((y+1) * img.width * 3)
        rows.append(pixel_bytes[first:last])

    return rows


def get_pixels(pixel_bytes):
    """Return a list of 3-tuples of bytes for the RGB channels in each pixel."""
    pixels = []
    for i in range((len(pixel_bytes) // 3)):
        pixels.append(pixel_bytes[i*3:(i+1)*3])

    return pixels


def pixels_to_bytes(pixels):
    """Return a bytes object from pixel tuple lists."""
    return b''.join(pixels)


def from_rows(rows):
    """Return a PIL image from a list of bytes for rows of pixels."""
    return Image.frombytes(img.mode, img.size, b''.join(rows))


def sort_pixels(row, mask=0xFFFFFF):
    """Sort a list of pixels, with an optional bit mask."""
    # in_order = False
    # while not in_order:
    #     for i in range(len(row) - 1):
    #         if (row[i] & mask) > (row[i+1] & mask):
    #             row[i], row[i+1] = row[i+1], row[i]

    #     in_order = True
    #     for i in range(len(row) - 1):
    #         if (row[i] & mask) > (row[i+1] & mask):
    #             in_order = False

    return pixels_to_bytes(sorted(get_pixels(row), key=lambda x: sum(x)//len(x) & mask))

img = Image.open('profile.jpeg')

mask = random.randint(0, 0xFFFFFF)


rows = get_rows(img)
new_rows = []

for i, row in enumerate(rows):
    new_rows.append(bytes(sort_pixels(row, mask)))

re_img = from_rows(new_rows)
re_img.show()
