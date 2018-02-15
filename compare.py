from PIL import ImageChops
from PIL import Image
import math
import os


def compare(inf1, inf2):
    im1 = Image.open(inf1)
    im2 = Image.open(inf2)

    # calculate rms (root mean square)
    diff = ImageChops.difference(im1, im2)
    h = diff.histogram()
    sq = (value * ((idx % 256) ** 2) for idx, value in enumerate(h))
    sum_of_squares = sum(sq)
    rms = math.sqrt(sum_of_squares / float(im1.size[0] * im1.size[1]))
    print 'Difference of two images: ' + rms
    print '(A result close to 0 means a good match.)'


if __name__ == '__main__':
    # input image names
    filename = [str(x) for x in raw_input().split()]

    print 'Input file names: %s %s' % (filename[0], filename[1])

    # make input file format
    infile1 = os.path.join('../image/img', filename[0])
    infile2 = os.path.join('../image/img', filename[1])

    # compare two images
    compare(infile1, infile2)