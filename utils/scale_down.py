import os
import sys

from PIL import Image

SRC_DIR = "original_images"
DESTS = (
    ("barbeadis.info/img_big", (800, 800)),
    ("barbeadis.info/img", (300, 300)),
)


def resize(name):
    print name
    src = os.path.join(SRC_DIR, name)
    im = Image.open(src)
    for dest_dir, max_size in DESTS:
        dst = os.path.join(dest_dir, name)
        im.thumbnail(max_size, Image.ANTIALIAS)
        im.save(dst)


def main(names):
    if names:
        for name in names:
            resize(name)
    else:
        print "PROCESS ALL IMAGES"
        fs = os.listdir(SRC_DIR)
        for name in fs:
            if "jpg" in name:
                resize(name)


if __name__ == '__main__':
    main(sys.argv[1:])
