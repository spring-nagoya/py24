from smtplib import SMTP
from email.mime.text import MIMEText
from email.utils import formatdate

MESSAGE = "pyhton送信テスト"
SUBJECT = "件名"
MAIL_FROM = "take.ep91.s15@gmail.com"
MAIL_TO = "take_s15_sr20de@hotmail.co.jp"
MSG = MIMEText(MESSAGE, "plain")
MSG["Subject"] = SUBJECT
