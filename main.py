from flask import Flask,request
from docutils.core import publish_parts
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
 
@app.route('/',methods=['GET'])
def r():
    return 'helo'
 
@app.route('/rsttohtml',methods=['POST'])
def rst_html():
    try:
        if request.method == 'POST':
            rst_input = request.get_json()
            output = publish_parts(rst_input['data'], writer_name='html')['body']
            # output = publish_parts(stttr, writer_name='html')['body']
            return {"status_code":200,"res":output}
    except Exception as e:
        return {"status_code":500,"res":e}
        

