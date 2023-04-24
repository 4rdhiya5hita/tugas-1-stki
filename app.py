import subprocess

from flask import Flask, render_template, request, send_file
# from data_retrieval_text import data_retrieval_text
# from data_retrieval_txt import data_retrieval_txt
from data_retrieval import document_retrieval

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
        input_text1 = request.form['input_text1']
        input_text2 = request.form['input_text2']
        input_text3 = request.form['input_text3']
        search_word = request.form['search_word']
        result = document_retrieval(input_text1, input_text2, input_text3, search_word)
        return render_template('result_text.html', result=result, search_word=search_word)    
    

@app.route('/txt', methods=['GET'])
def txt():
    return render_template('index_txt.html')


@app.route('/data_retrieval_txt', methods=['GET', 'POST'])
def data_result_txt():
    if request.method == 'POST':
        file1 = request.files['myfile1']
        file_contents1 = file1.read() # read the content
        input_text1 = file_contents1.decode('utf-8') # To convert the bytes to a string
        
        file2 = request.files['myfile2']
        file_contents2 = file2.read()
        input_text2 = file_contents2.decode('utf-8')

        search_word = request.form['search_word']
        
        result = document_retrieval(input_text1, input_text2, search_word)
        # print(result)

        # return file_contents
        return render_template('result_txt.html', result=result, search_word=search_word)


@app.route('/', methods=['GET'])
def index():
    image_url = '/img_01.jpg'
    return render_template('index.html', image_url=image_url)
    
if __name__ == '__main__':
    app.run(debug=True)
