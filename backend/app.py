from flask import Flask, render_template, request, jsonify, send_from_directory
import config
from error import InvalidAPIError
import utils
from api.handlers import img_dir_handler

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

    number_of_image = request.args.get('number')
    if number_of_image is None:
        raise InvalidAPIError("No number query", status_code=1) # 抛出业务异常。返回code和message

    result = {
        "list": [],
        "error": 0
    }
    # 随机选取一组图片
    result["list"] = img_dir_handler(number_of_image)
    # print('len list', len(result["list"]))

    # 为这组图片成为任务id
    task_id = utils.gen_uuid()
    result["task_id"] = task_id
    # TODO: store the task_id

    # print('json', jsonify(result))

    return jsonify(result)


if __name__ == '__main__':
    app.run()