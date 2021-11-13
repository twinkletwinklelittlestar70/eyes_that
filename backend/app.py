from flask import Flask, render_template, request, jsonify
import numpy as np
# import cv2
from .error import InvalidAPIError
from .utils import gen_uuid
from .api.handlers import img_dir_handler
from .api.Model import recog_model
from .api.TaskManager import task_manager
from . import config

# 通过 static_folder 指定静态资源路径，以便 index.html 能正确访问 CSS 等静态资源
# template_folder 指定模板路径，以便 render_template 能正确渲染 index.html
# static_url_path 指定访问的路径
app = Flask(
    __name__,
    static_folder="./static",
    static_url_path="/",
    template_folder="./static")

# Error Handler
@app.errorhandler(InvalidAPIError)
def invalid_api_usage(e):
    return jsonify(e.to_dict())

# Route Handler
# Reture the page
@app.route('/')
def index():
    '''
        When browser access this router，use render_template to render ./static/dist/index.html.
        Page router would be handled by the fe itself.
    '''
    return render_template("index.html")


# Get all images randomly
@app.route('/api/get_images', methods=['GET'])
def get_images():

    number_of_image = request.args.get('number')
    if number_of_image is None:
        # 抛出业务异常。返回code和message
        raise InvalidAPIError("No number query", status_code=1)

    result = {
        "list": [],
        "error": 0
    }
    # random pick a group of images
    result["list"] = img_dir_handler(number_of_image)
    # print('len list', len(result["list"]))

    # generate task_id and save the task
    task_id = gen_uuid()
    result["task_id"] = task_id
    task_manager.add_task(task_id, result["list"])

    return jsonify(result)


# Submit answers from FE.
# Run prediction and return the accuracy
@app.route('/api/submit_answers', methods=['POST'])
def submit_images():

    data = request.json
    task_id = data['task_id']
    print('submit_answers for task', task_id)

    # Step1: check the paramters
    if task_id is None:
        # throw error
        raise InvalidAPIError("No number query", status_code=1)

    # predict
    # result of prediction looks like this: [{img:'xxx', 'predict':0, 'standard': 1}]
    result = recog_model.predict(task_id, is_multi_thread=False)
    print('result =====> ', result)
    all_score = {
        "ai_score": {
            "accuracy": 0},
        "error": 0
    }

    # Step3: calculate the accuracy and return
    sum_of_correct = 0
    for item in result:
        img = item['img']
        standard = item['standard']
        predict = item['predict']
        if predict == standard:
            sum_of_correct += 1
    accuracy = sum_of_correct/len(result)
    all_score["ai_score"]["accuracy"] = accuracy

    return jsonify(all_score)

# Recognize the image user uploaded and return result
@app.route('/api/upload_to_recog', methods=['POST', 'PUT'])
def image_upload():
    # get upload image, preprocess and do the recognition
    try:
        filestr = request.files['file'].read()
        npimg = np.fromstring(filestr, np.uint8)

        result, faces_coordinate = recog_model.predicAnyImage(image_data=npimg)

        return_data = {"is_real": result, "error": 0, "coordinates": faces_coordinate}

    except Exception as e:
        print("Upload: An exception occurred", e)
        raise InvalidAPIError("prediction error", status_code=2)

    return jsonify(return_data)


if __name__ == '__main__':
    app.run()
