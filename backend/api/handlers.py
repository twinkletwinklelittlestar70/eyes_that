"""
    API handlers
"""
from flask import request
import random
import config

def img_dir_handler(number):
    list = []

    fake_number = random.randint(3,7)
    real_number = 10 - fake_number

    for index, num in enumerate([fake_number, real_number]):
        facetype = 'fake' if index == 0 else "real"
        id_list = random.sample(range(1, config.MAX_FAKE_IMAGE_ID), int(num))
        for i in id_list:
            list.append({
                "url": request.url_root + config.IMAGE_DIR + "/" + facetype + "/" + str(i) + config.IMAGE_FORMAT,
                "type": index,
            })
    
    random.shuffle(list)

    return list
