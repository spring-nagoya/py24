# ajax_app.py  flask + ajax

from flask import Flask,render_template,request,jsonify
import json
import mysql.connector

app = Flask(__name__)

def connect_db():
    conn = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "Passw0rd",
        db = "2023py24db",
    )
    return conn


@app.route("/")
def index():
    #テンプレート(index.html)を読み込む
    return render_template('index.html')

@app.route("/call_ajax", methods=['GET','POST'])
def call_ajax():
    if request.method == "POST":
        #formデータからの受け取り

        # fdata:ajaxで設定した名前
        json_data = request.get_json(force=True)
        print(json_data["fdata"])
        form_data = json_data["fdata"]
        
        sql = " select * from user where name like '%"+form_data+"%';"
        try:
            conn = connect_db()
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql)
            rows = cursor.fetchall()
            cursor.close()
            conn.close()
        except Exception as e:
            print(e)
            return jsonify({"error":"error"})
        
        ret_data = []
        for row in rows:
            ret_data.append(row)
        # form_data = request.form.get('fdata')
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

