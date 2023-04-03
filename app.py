import subprocess

from flask import Flask, render_template, request, send_file
# from data_retrieval_text import data_retrieval_text
# from data_retrieval_txt import data_retrieval_txt
from data_retrieval import data_retrieval

app = Flask(__name__)

@app.route('/text', methods=['GET'])
def text():
    # if request.method == 'POST':
    #     name = request.form['name']
    #     data_retrieval_text(name)
        # return f'Hello, {name}!'
    return render_template('index_text.html')


@app.route('/data_retrieval_text', methods=['GET', 'POST'])
def data_result():
    if request.method == 'POST':
        input_text = request.form['input_text']
        result = data_retrieval(input_text)
        return render_template('result_text.html', result=result)    
    

@app.route('/txt', methods=['GET'])
def txt():
    return render_template('index_txt.html')


@app.route('/data_retrieval_txt', methods=['GET', 'POST'])
def data_result_txt():
    if request.method == 'POST':
        file = request.files['myfile']
        file_contents = file.read() # read the content
        
        # To convert the bytes to a string
        input_text = file_contents.decode('utf-8')
        result = data_retrieval(input_text)
        # print(result)

        # return file_contents
        return render_template('result_txt.html', result=result)    


@app.route('/', methods=['GET'])
def index():
    image_url = '/img_01.jpg'
    return render_template('index.html', image_url=image_url)
    
if __name__ == '__main__':
    app.run(debug=True)
