from urllib.parse import urlparse
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

from api.TaskManager import task_manager
from api import ThreadClass
import config

import time

class RecogModel():
  def __init__(self):
    # Load the model
    self.model = tf.keras.models.load_model(config.MODEL_PATH)
    pass


  def predictImage(self, filepath):
    '''Predic one image

    The function will read the imags data from disk, put image
    np array data into the model and get the result.

    Args:
        filepath(str): The file path of one image

    Returns:
        0: for fake face
        1: for real face
    '''
    # 预处理图片
    print('loading image', filepath)
    img = image.load_img(filepath, grayscale=True, target_size=config.INPUT_SIZE)
    input_arr = image.img_to_array(img)
    input_rescale = np.array([input_arr])
    # 模型识别
    result = self.model.predict(input_rescale)
    isReal = result[0][0] >= 0.5 # >= 0.5 表示 real, <0.5 表示 fake

    print('isReal=======>', isReal)

    return int(isReal)
  
  def predictImageList(self, filelist):
      result = []
      for filepath in filelist:
          result.append(self.predictImage(filepath))
      
      return result

  def predict (self, id, is_multi_thread = False):
    '''Get predict result for a task (10 images)

    The function will read the imags data from task manager first.
    And then predict the result one by one.

    Args:
        id (str): The id of a task

    Returns:
        [{img:'xxx', 'predict':0, 'standard': 1}]
        img: the path of image
        predict: predict result from our fake face recognition model
        standard: the ground truth
    '''

    task_list = task_manager.get_task_byid(id)
    print('Getting task list id=', id)
    print(task_list)
    result = []

    # 单线程用时 2.7627809047698975 s
    # 10个多线程用时 4.012258052825928 s
    # 2个多线程用时 2.3256211280822754 s
    if is_multi_thread:
        # 10个线程版本
        # thread_list = []
        # time_start=time.time()

        # for item in task_list:
        #     url = item['url'] # http://127.0.0.1:5000/images/real/5.png
        #     standard = item['type']
        #     filepath = './static' + urlparse(url).path # ./static/images/real/5.png

        #     result.append({
        #         "img": url, # 图片路径
        #         "standard": standard, # 标准答案
        #     })
        
        #     work_task = ThreadClass.TaskThread(self.predictImage.__func__, (self, filepath))
        #     thread_list.append(work_task)
        #     work_task.start()
    
        # for index, work_task in enumerate(thread_list):
        #     predict_result = work_task.get_result()
        #     result[index]["predict"] = predict_result # 模型预测答案
    
        # time_end=time.time()
        # print('model predict time cost', time_end - time_start, 's')
        
        # return result
        
        # 2个线程版本
        time_start=time.time()

        thread_list = []
        filepath_list_1 = []
        filepath_list_2 = []

        list_len = len(task_list) / 2 # 10个分两组

        for tidex, item in enumerate(task_list):
            url = item['url'] # http://127.0.0.1:5000/images/real/5.png
            standard = item['type']
            filepath = './static' + urlparse(url).path # ./static/images/real/5.png
            if tidex < list_len: # 5个一组
                filepath_list_1.append(filepath)
            else:
                filepath_list_2.append(filepath)
            
            result.append({
                "img": url, # 图片路径
                "standard": standard, # 标准答案
            })
            
        for file_list in [filepath_list_1, filepath_list_2]:
            work_task = ThreadClass.TaskThread(self.predictImageList.__func__, (self, file_list))
            thread_list.append(work_task)
            work_task.start()
    
        for index, work_task in enumerate(thread_list):
            predict_result_list = work_task.get_result()
            for ridx, rst in enumerate(predict_result_list):
                real_index = int(index * list_len + ridx)
                result[real_index]["predict"] = rst # 模型预测答案
    
        time_end=time.time()
        print('model predict time cost', time_end - time_start, 's')
        
        return result
    
    else:
        time_start=time.time()

        for item in task_list:
            url = item['url'] # http://127.0.0.1:5000/images/real/5.png
            standard = item['type']
            filepath = './static' + urlparse(url).path # ./static/images/real/5.png
            predict_result = self.predictImage(filepath)

            result.append({
                "img": url, # 图片路径
                "standard": standard, # 标准答案
                "predict": predict_result # 模型预测答案
            })
    
        time_end=time.time()
        print('model predict time cost', time_end - time_start, 's')
        
        return result


recog_model = RecogModel()