from urllib.parse import urlparse
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import cv2
import os

from .TaskManager import task_manager
from . import ThreadClass
from .. import config

import time


class RecogModel():
    def __init__(self):
        # Load the model
        self.model = tf.keras.models.load_model(config.MODEL_PATH)
        # self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
        pass
    
    def _preprocess(self, img):
        # img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        img = cv2.resize(img, config.INPUT_SIZE_2D)
        return img

    def predictImage(self, filepath, image_data=None):
        '''Predic one image

        The function will read the imags data from disk, put image
        np array data into the model and get the result.

        Args:
            filepath(str): The file path of one image
            image_data: Or specify the image data without filepath

        Returns:
            0: for fake face
            1: for real face
        '''
        # 预处理图片
        if len(filepath) > 0:
            print('loading image', filepath)
            img = image.load_img(filepath, grayscale=True,
                                 target_size=config.INPUT_SIZE)
        else:
            img = self._preprocess(image_data)
            
        input_arr = image.img_to_array(img)
        input_rescale = np.array([input_arr])

        # 模型识别
        result = self.model.predict(input_rescale)
        isReal = result[0][0] >= 0.5  # >= 0.5 表示 real, <0.5 表示 fake

        print('isReal=======>', isReal)

        return int(isReal)

    def predictImageList(self, filelist):
        result = []
        for filepath in filelist:
            result.append(self.predictImage(filepath))

        return result

    def predict(self, id, is_multi_thread=False):
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

        # single thread time cost 2.7627809047698975 s
        # 10 threads time cost 4.012258052825928 s
        # 2 threads time cost 2.3256211280822754 s
        if is_multi_thread:
            # For 10 threads:
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

            # For 2 thread: and this is the fastest one
            time_start = time.time()

            thread_list = []
            filepath_list_1 = []
            filepath_list_2 = []

            list_len = len(task_list) / 2  # 10个分两组

            for tidex, item in enumerate(task_list):
                url = item['url']  # http://127.0.0.1:5000/images/real/5.png
                standard = item['type']
                # ./static/images/real/5.png
                filepath = './static' + urlparse(url).path
                if tidex < list_len:  # 5个一组
                    filepath_list_1.append(filepath)
                else:
                    filepath_list_2.append(filepath)

                result.append({
                    "img": url,  # 图片路径
                    "standard": standard,  # 标准答案
                })

            for file_list in [filepath_list_1, filepath_list_2]:
                work_task = ThreadClass.TaskThread(
                    self.predictImageList.__func__, (self, file_list))
                thread_list.append(work_task)
                work_task.start()

            for index, work_task in enumerate(thread_list):
                predict_result_list = work_task.get_result()
                for ridx, rst in enumerate(predict_result_list):
                    real_index = int(index * list_len + ridx)
                    result[real_index]["predict"] = rst  # 模型预测答案

            time_end = time.time()
            print('model predict time cost', time_end - time_start, 's')

            return result

        else:
            # For single thread
            time_start = time.time()

            for item in task_list:
                url = item['url']  # http://127.0.0.1:5000/images/real/5.png
                standard = item['type']
                # ./static/images/real/5.png
                filepath = './static' + urlparse(url).path
                predict_result = self.predictImage(filepath)

                result.append({
                    "img": url,  # 图片路径
                    "standard": standard,  # 标准答案
                    "predict": predict_result  # 模型预测答案
                })

            time_end = time.time()
            print('model predict time cost', time_end - time_start, 's')

            return result

    def predicAnyImage (self, image_data=None):
        if image_data is None:
            return [],[]
        
        # preprocess the image
        # gray = cv2.imdecode(image_data, cv2.IMREAD_GRAYSCALE)
        gray = cv2.imdecode(image_data, cv2.IMREAD_GRAYSCALE)
        (o_r, o_c) = gray.shape

        try:
            # Face detection
            faces_coordinate = self.face_cascade.detectMultiScale(gray, 1.3, 1)
        except Exception as e:
            faces_coordinate = []
            print('Face detection error: ', e)
        
        if len(faces_coordinate) == 0:
            print('No faces were detected')
            return [], []

        print(len(faces_coordinate), ' faces were detected', faces_coordinate)
        
        # Find all the face and crops them
        cropped_faces = []
        coords_list = []
        # index = 0
        for (x, y, w, h)  in faces_coordinate:
            exp = 0.3
            y1 = int(max(0, y - exp * h))
            y2 = int(min(y + (1 + exp) * h, o_r))
            x1 = int(max(0, x - exp * w))
            x2 = int(min(x + (1 + exp) * w, o_c))
            print('crop area', y1, y2, x1, x2)
            cropped_image = gray[y1:y2, x1:x2]
            
            cropped_faces.append(cropped_image)# (1024, 1024)   [y:y+h, x:x+w] [[187 214 675 675]]
            
            # test code to save image to check the crop scale
            # my_file = os.path.join('/Users/karenlin/workspace/eyes_that/backend/', 'test' + str(index) + '.jpg')
            # print('write', my_file)
            # cv2.imwrite(my_file, cropped_image)
            # index += 1

            coords_list.append([int(x), int(y), int(w), int(h)])

        result = []
        for face_image in cropped_faces: # [gray]:  cropped_faces:
            print('shape of face image', face_image.shape)
            result.append(self.predictImage(filepath='', image_data = face_image))
        
        # compare the resut from whole image
        # Log to test the crop result
        whole_image_result = self.predictImage(filepath='', image_data = gray)
        print('The result of whole image should be the same with cropped', whole_image_result)
        
        return result, coords_list


recog_model = RecogModel()
