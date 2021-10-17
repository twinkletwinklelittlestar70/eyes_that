import os
from urllib.parse import urlparse
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

from taskmanager import task_manager
import config


class RecogModel():
  def __init__(self):
    # Load the model
    self.model = tf.keras.models.load_model(config.MODEL_PATH)
    pass

  def predictImage(self, filepath):
    # 预处理图片
    print('loading image', filepath)
    img = image.load_img(filepath, grayscale=True, target_size=(224, 224, 1))
    input_arr = image.img_to_array(img)
    input_rescale = np.array([input_arr])
    # 模型识别
    result = self.model.predict(input_rescale)
    print('result of test', result)
    isReal = result[0][0] >= 0.5 # >= 0.5 表示 real, <0.5 表示 fake

    return int(isReal)

  #  @return: [{img:'xxx', 'predict':0, 'standard': 1}]
  def predict (self, id):
    task_list = task_manager.get_task_byid(id)
    print('Getting task list id=', id)
    print(task_list)
    result = []
    for item in task_list:
        url = item['url'] # http://127.0.0.1:5000/images/real/5.png
        standard = item['type']
        filepath = './static' + urlparse(url).path # ./static/images/real/5.png
        predict_result = self.predictImage(filepath)
        
        result.append({
            "img": filepath, # 图片路径
            "standard": standard, # 标准答案
            "predict": predict_result # 模型预测答案
        })
        
    return result


recog_model = RecogModel()