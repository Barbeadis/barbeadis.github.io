import os
import sys

from PIL import Image, ImageDraw, ImageFont

DESTS = {
    2: {"img": (400, 400)},
    3: {"img": (500, 500)},
    16: {"img": (200, 200)},
    19: {"img": (500, 500)},
    79: {"img": (500, 500)},
    82: {"img": (500, 500)},
}
DEST_DEFAULTS = {
    "img_big": (800, 800),
    "img": (300, 300),
}
TEXTS = {
    75: "Pasqua 2022",
    78: "Mandi Mandi!",
}
TEXT_COLOR = "violet"


def resize(src_dir, name, extension):
    index = int(name)
    src_path = os.path.join(src_dir, name + extension)
    im = Image.open(src_path)
    dests = DESTS.get(index, {})
    for dest_dir, max_size_default in DEST_DEFAULTS.items():
        max_size = dests.get(dest_dir, max_size_default)
        dst_path = os.path.join(dest_dir, name + extension)
        print(dst_path, max_size)
        im.thumbnail(max_size, Image.LANCZOS)
        # im.resize(max_size, Image.LANCZOS)
        text = TEXTS.get(index)
        if dest_dir == 'img' and text:
            left, top, right, bottom = im.getbbox()
            print(index, text, left, top, right, bottom)
            font = ImageFont.truetype("Verdana.ttf", size=25)
            draw = ImageDraw.Draw(im)
            draw.text((left + 50, bottom - 50), text, fill=TEXT_COLOR, font=font)
            del draw
        im.save(dst_path)


def main(src_dir):
    print("PROCESS ALL IMAGES FROM", src_dir)
    for filename in os.listdir(src_dir):
        name, extension = os.path.splitext(filename)
        if extension != '.jpg':
            continue
        resize(src_dir, name, extension)


if __name__ == '__main__':
    main(*sys.argv[1:])
