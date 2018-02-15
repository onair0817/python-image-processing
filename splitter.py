from PIL import Image
import os
import random


def split(infile):
    # read input file
    im = Image.open(infile)

    # size of image
    imgwidth, imgheight = im.size

    print 'Image size is: %d x %d' % (imgwidth, imgheight)

    height = imgheight / 2
    width = imgwidth / 2
    start_num = 0

    # split & rotate image
    for k, piece in enumerate(crop(im, height, width), start_num):
        print piece

        img = Image.new('RGB', (width, height), 255)
        img.paste(piece)
        img = rotate(img)
        path = os.path.join("img/%s" % (filename[k + 1]))
        img.save(path)


def crop(im, height, width):
    # size of image
    imgwidth, imgheight = im.size

    for i in range(imgheight // height):
        for j in range(imgwidth // width):
            # print (i,j)
            box = (j * width, i * height, (j + 1) * width, (i + 1) * height)
            yield im.crop(box)


def rotate(im):
    rotation = [90, -90, 180, -180]
    x = random.choice(rotation)
    im = im.rotate(x, expand=1)

    return im


if __name__ == '__main__':
    # input image names
    filename = [str(x) for x in raw_input().split()]

    print 'Input file name: %s' % filename[0]
    print 'Output file names : %s %s %s %s' % (filename[1], filename[2], filename[3], filename[4])

    # make input file format
    infile = os.path.join('../image/img', filename[0])

    # split input image and rotate images
    split(infile)

