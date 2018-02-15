from PIL import Image
import os


# merge 4 images into 1
def merge(fl):

    images = []

    # rotate images for merging
    for index, file in enumerate(fl):
        # read one of input files
        im = Image.open(fl[index])
        imgwidth, imgheight = im.size

        if imgheight > imgwidth:
            im = im.rotate(90, expand=1)
            images.append(im)
            imgwidth, imgheight = imgheight, imgwidth
        else:
            images.append(im)

    outwidth, outheight = imgwidth*2, imgheight*2
    outimage = Image.new("RGB", (outwidth, outheight))

    # merge images
    for index, file in enumerate(images):
        images[index].thumbnail((imgwidth, imgheight), Image.ANTIALIAS)
        x = index // 2 * imgwidth
        y = index % 2 * imgheight
        w, h = images[index].size
        print('pos {0},{1} size {2},{3}'.format(x, y, w, h))
        outimage.paste(images[index], (x, y, x + w, y + h))

    path = os.path.join("../image/img/%s" % (filename[4]))
    outimage.save(path)


if __name__ == '__main__':
    # input image names
    filename = [str(x) for x in raw_input().split()]

    print 'Input file names : %s %s %s %s' % (filename[0], filename[1], filename[2], filename[3])
    print 'Output file name: %s' % filename[4]

    # make list format of input files
    filelist = []

    for k in range(0, 4):
        filelist.append(os.path.join('../image/img', filename[k]))
        #print filelist[k]

    # merge 4 images into 1
    merge(filelist)