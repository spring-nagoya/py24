from flask import Flask, render_template, request
from logger import Logger, LOG_DEBUG
# from sendmail import *

l = Logger('.log/log.txt', LOG_DEBUG)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('sendmail.html')

@app.route('/check', methods=['POST'])
def send_mail():
    From = request.form.get('From')
    To = request.form.get('To')
    Subject = request.form.get('Subject')
    Message = request.form.get('Message')
    
    l.DEBUG("fromAddress={} ,toAddress={} ,subject={} ,message={}".format(From,To,Subject,Message))
    
    return render_template('sendmail.html')
    
if __name__ == '__main__':
    app.run(debug=True)