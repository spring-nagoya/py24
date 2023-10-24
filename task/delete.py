from flask import Flask, render_template, redirect, request, url_for


app = Flask(__name__)

import mysql.connector


# MySQLへの接続設定を行う関数
def conn_db():
    # DBへの接続オブジェクトを作成
    conn = mysql.connector.connect(
        # MySQLがどこにあるのか
        host="127.0.0.1",
        # 誰がDBを使うのか
        user="root",
        # DB使用の認証情報
        passwd="P@ssw0rd",
        # 使用するデータベース名
        db="py23",
    )
    return conn


@app.route("/")
def index():
    try:
        conn = conn_db()
        cursor = conn.cursor()
        sql = "SELECT * FROM T_sample;"
        cursor.execute(sql)
        result = cursor.fetchall()
    except mysql.connector.Error as e:
        print(e)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    return render_template("delete_list.html", records=result)


@app.route("/delete/")
def delete():
    conn = ""
    cursor = ""
    try:
        id = request.args.get("id","")
        conn = conn_db()
        cursor = conn.cursor()
        sql = "DELETE FROM T_sample WHERE id= {0};".format(id)
        cursor.execute(sql)
        conn.commit()
    # SQLインジェクション対策の為に、SQLパラメータを使用したパターン
    # sql = "DELETE FROM T_sample WHERE id= %s"
    # executeメソッドの第二引数にタプル型で値を渡すことで、SQLパラメータに値を当てはめることが可能。
    # ただし、パラメータが1つでも最後にカンマを付ける必要がある。
    # cursor.execute(sql, (id,))
    except mysql.connector.Error as e:
        print(e)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    return redirect(url_for("index"))

@app.route("/create/", methods=["POST"])
def create():
    conn = ""
    cursor = ""
    # IDをserial型にしているので、idは自動採番される
    sql = "INSERT INTO T_sample (name, password, email) VALUES (%s, %s, %s);", (name, password, email)
    try:
        name = request.form.get("name")
        password = request.form.get("password")
        email = request.form.get("email")
        conn = conn_db()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    except mysql.connector.Error as e:
        print(e)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    return redirect(url_for("index"))

@app.route("/update/", methods=["POST"])
def update():
    conn = ""
    cursor = ""
    sql = "UPDATE T_sample SET name = %s, password = %s email = %s WHERE id = %s;", (name, password, email, id)
    try:
        id = request.form.get("id")
        name = request.form.get("name")
        password = request.form.get("password")
        email = request.form.get("email")
        conn = conn_db()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    except mysql.connector.Error as e:
        print(e)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
    return redirect(url_for("index"))