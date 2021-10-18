"""
    To rename and move real people face data from dataset to project folder
"""
import os, shutil

fileDir = "./../dataset/real_vs_fake/real-vs-fake/test/real"  # origin
tarDir = './../../backend/static/images/real'    # move to

image_number = 200 # How many images we need

if __name__ == '__main__':
    imageFiles = os.listdir(fileDir)    # get the image files list
    filenumber = len(imageFiles)
    print('Total ', filenumber, ' images to be select')

    for index, img in enumerate(imageFiles):
        # ignore unix system file
        if img == '.DS_Store':
            continue
        if index >= image_number:
            break
        
        # Rename and move to target dir
        # print('image name=', img) # 432323.jpg
        new_name = str(index+1) + '.' + img.split('.')[-1]
        shutil.move(os.path.join(fileDir, img), os.path.join(tarDir, new_name))