# ajax_app.py  flask + ajax

from flask import Flask,render_template,request,jsonify
import json

app = Flask(__name__)

@app.route("/")
def index():
    #テンプレート(index.html)を読み込む
    return render_template('index.html')

@app.route("/call_ajax", methods=['GET','POST'])
def call_ajax():
    if request.method == "POST":
        #formデータからの受け取り

        # fdata:ajaxで設定した名前
        form_data = request.form.get('fdata')
        # form_data = request.form['fdata']
        print(form_data)

        # 受け取りデータの加工
        data = { "key" : form_data }
        # json形式で戻す
        return jsonify(data)
    else:
        return jsonify({"test":"get-test"})

if __name__ == "__main__":
    app.run()

