from flask import Flask, render_template, redirect, request, url_for
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("sendmail.html")


@app.route("/check/", methods=["POST"])
def func_send_mail():
    message = "hi im use github copilot. this is test mail."
    subject = "copilot test mail"
    # 受信者
    mailTo = "user01@10.141.113.80"
    # 送信者
    mailForm = "user01@10.141.113.80"
    msg = MIMEText(message, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = mailForm
    msg["To"] = mailTo
    msg["Date"] = formatdate()

    # localhost = 127.0.0.1
    host = "10.141.113.80"  # "smtp.gmail.com"  #SMTPサーバーのアドレス
    port = 25  # 587  #SMTPサーバーのポート番号
    user = "soninoo7mod@gmail.com"  # SMTPサーバーのユーザー名
    password = "Touhou47901"
    server = SMTP(host, port)
    server.set_debuglevel(1)  # SMTPサーバーとのやり取りのログを出力

    # server.starttls()
    server.ehlo()
    # server.login(user, password)
    server.ehlo()
    server.send_message(msg)
    server.close()

    mailForm = request.form.get("form")
    mailTo = request.form.get("to")
    subject = request.form.get("subject")
    message = request.form.get("message")

    return render_template(
        "mailcheck.html",
        mailForm=mailForm,
        mailTo=mailTo,
        subject=subject,
        message=message,
    )
