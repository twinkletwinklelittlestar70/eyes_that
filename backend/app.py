from flask import Flask, render_template, request, jsonify
from .error import InvalidAPIError
from .utils import gen_uuid
from .api.handlers import img_dir_handler
from .api.Model import recog_model
from .api.TaskManager import task_manager
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
        当在浏览器访问网址时，通过 render_template 方法渲染 dist 文件夹中的 index.html。
        页面之间的跳转交给前端路由负责，后端不用再写大量的路由
    '''
    return render_template("index.html")


# Get all images randomly
@app.route('/api/get_images', methods=['GET'])
def get_images():

    number_of_image= request.args.get('number')
    if number_of_image is None:
        raise InvalidAPIError("No number query", status_code=1) # 抛出业务异常。返回code和message

    result = {
        "list": [],
        "error": 0
    }
    # 随机选取一组图片
    result["list"] = img_dir_handler(number_of_image)
    # print('len list', len(result["list"]))

    # 为这组图片成为任务id，并把任务存起来
    task_id = gen_uuid()
    result["task_id"] = task_id
    task_manager.add_task(task_id, result["list"])

    return jsonify(result)


# Submit answers from FE.
# Run prediction and return the accuracy
@app.route('/api/submit_answers', methods=['POST'])
def submit_images():
    # TODO: Step1: 判断参数正常，不正常抛出业务异常。
    # TODO: Step2: 从请求参数中取task_id，替换下面那个

    data = request.json
    task_id = data['task_id']
    print('submit_answers for task', task_id)

    if task_id is None:
        raise InvalidAPIError("No number query", status_code=1)  # 抛出业务异常。返回code和message

    # 模型预测
    result = recog_model.predict(task_id, is_multi_thread=False) # 预测的结果，类似这样 [{img:'xxx', 'predict':0, 'standard': 1}]
    print('result =====> ', result)
    all_score = {
        "ai_score":{
         "accuracy": 0},
        "error": 0
    }

    # TODO: Step3: 计算模型准确率，并返回给前端
    sum_of_correct=0
    for item in result:
        img = item['img']
        standard=item['standard']
        predict=item['predict']
        if predict == standard:
            sum_of_correct += 1
    accuracy = sum_of_correct/len(result)
    all_score["ai_score"]["accuracy"] = accuracy

    
    return jsonify(all_score)


if __name__ == '__main__':
    app.run()