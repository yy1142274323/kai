from flask import Flask, request, jsonify
import json

app = Flask(__name__)
app.debug = True


@app.route('/url=', methods=['post'])
def add_stu():
    if not request.data:  # 检测是否有数据
        return ('fail')
    student = request.data.decode('utf-8')
    # 获取到POST过来的数据，因为我这里传过来的数据需要转换一下编码。根据晶具体情况而定
    student_json = json.loads(student)
    # 把区获取到的数据转为JSON格式。
    print(student_json)
    # return jsonify(student_json)
    # 返回JSON数据。
    return '54154154184'


if __name__ == '__main__':
    app.run(host='10.10.30.46')
    # 这里指定了地址和端口号。

    


