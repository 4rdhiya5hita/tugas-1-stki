import subprocess

from flask import Flask, render_template, request
from data_retrieval_text import data_retrieval_text
from data_retrieval_txt import data_retrieval_txt

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # if request.method == 'POST':
    #     name = request.form['name']
    #     data_retrieval_text(name)
        # return f'Hello, {name}!'
    
    return render_template('index.html')

@app.route('/data_retrieval_text', methods=['GET', 'POST'])
def data_result():
    if request.method == 'POST':
        input_text = request.form['input_text']
        result = data_retrieval_text(input_text)
        return render_template('result.html', result=result)    
    
@app.route('/txt', methods=['GET', 'POST'])
def txt():
    # if request.method == 'POST':
    #     name = request.form['name']
    #     data_retrieval_text(name)
        # return f'Hello, {name}!'
    
    return render_template('data_txt.html')


@app.route('/data_retrieval_txt', methods=['GET', 'POST'])
def data_result_txt():
    with open('example.txt', 'r') as file:
        contents = file.read()
        subprocess.call(['python', 'uji_data_retrieval_txt.py', contents])

    # if request.method == 'POST':
    #     # Get the uploaded file
    #     file = request.files['file']

    #     # read the contents of the file
    #     contents = file.read()

    #     # pass the contents as an argument to the other script
    #     subprocess.call(['python', 'script2.py', contents])

        # Read the contents of the file
        # contents = file.read()
        # result = data_retrieval_txt(file)
        # return render_template('result_txt.html', result=result)    

if __name__ == '__main__':
    app.run(debug=True)
