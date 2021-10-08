from flask import Flask, render_template, request, jsonify, send_from_directory
import config
import random
from error import InvalidAPIError

# 通过 static_folder 指定静态资源路径，以便 index.html 能正确访问 CSS 等静态资源
# template_folder 指定模板路径，以便 render_template 能正确渲染 index.html
# static_url_path 指定访问的路径
app = Flask(
    __name__,
    static_folder="./static",
    static_url_path="/",
    template_folder="./static")

@app.errorhandler(InvalidAPIError)
def invalid_api_usage(e):
    return jsonify(e.to_dict())


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

    # if request.method != "GET":
    number_of_image = request.args.get('number')

    if number_of_image is None:
        raise InvalidAPIError("No number query", status_code=1) # 抛出业务异常。返回code和message

    result = {
        "list": [],
        "error": 0
    }

    # TODO: fake or real 也改成随机
    id_list = random.sample(range(1, config.max_image_id), int(number_of_image))    
    for i in id_list:
        result["list"].append({
            "url": request.url_root + "images/fake/" + str(i) + ".png",
            "type": 0
        })

    return jsonify(result)


if __name__ == '__main__':
    app.run()