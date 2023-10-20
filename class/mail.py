from flask import *
from logger import *
# from sendmail import *

l = Logger('.log/log.txt', 0)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('sendmail.html')

@app.route('/check', methods=['POST'])
def send_mail():
    fromAddress = request.form.get('from')
    toAddress = request.form.get('to')
    subject = request.form.get('subject')
    message = request.form.get('message')
    
    l.DEBUG("fromAddress={} ,toAddress={} ,subject={} ,message={}".format(fromAddress,toAddress,subject,message))
    
    return render_template('sendmail.html')
    
if __name__ == '__main__':
    app.run(debug=True)