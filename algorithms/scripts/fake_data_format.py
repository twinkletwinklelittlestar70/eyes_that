"""
    To transform fake face image format from png to jpg
"""
import os
from PIL import Image

dir = './../../backend/static/images/fake'    # data folder

if __name__ == '__main__':
    imageFiles = os.listdir(dir)    # get the image files list
    filenumber = len(imageFiles)
    print('Total ', filenumber, ' images to be select')

    for index, img in enumerate(imageFiles):
        # ignore unix system file
        if img == '.DS_Store':
            continue
        
        # To transform img format from png to jpg
        image = Image.open(os.path.join(dir, img))
        image.save(os.path.join(dir, img.split('.')[0] + '.jpg'))