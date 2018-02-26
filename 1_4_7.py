from PIL import Image, ImageFilter
import os
import matplotlib.pyplot as plt
import scipy.misc as misc
'''
#Task 1
for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        i.save('pngs/{}.png'.format(fn))







#Task3
#size_300 = (300,300)
#size_700 = (700,700)

#for f in os.listdir('.'):
    if f.endswith('.jpg'):
        
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        
        i.thumbnail(size_700)
        i.save('700/{}_700{}'.format(fn, fext))
        
        i.thumbnail(size_300)
        i.save('300/{}_300{}'.format(fn, fext))


image1 = Image.open('skip.jpg')
image1.filter(ImageFilter.GaussianBlur(15)).save('skip_mod.jpg')

#Task 4
imageupsidedown = Image.open('highland.jpg')
imageupsidedown.rotate(180).save('highland_mod.jpg')

'''
#Task 5
def load_img(filename):
    img = Image.open(filename)
    data = np.array(img)
    return data

def all_square_pixels(row, col, height, width):
    for y in xrange(int(round(row*square_h)),int(round((row+1_*square_h))):
        for x in xrange(int(round(col*square_w)), int(round((col+1)*square_w))):
            yield y, x