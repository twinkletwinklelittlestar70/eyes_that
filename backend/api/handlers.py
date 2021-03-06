"""
    API handlers
"""
import sys
sys.path.append("..")
from flask import request
import random
from .. import config

def img_dir_handler(number):
    list = []

    fake_number = random.randint(3,7)
    real_number = 10 - fake_number

    url_root = request.url_root
    print('url_root', url_root)
    # url_root = 'http://'

    for index, num in enumerate([fake_number, real_number]):
        facetype = 'fake' if index == 0 else "real"
        id_list = random.sample(range(1, config.MAX_FAKE_IMAGE_ID), int(num))
        for i in id_list:
            list.append({
                "url": url_root + config.IMAGE_DIR + "/" + facetype + "/" + str(i) + config.IMAGE_FORMAT,
                "type": index,
            })
    
    random.shuffle(list)

    return list
