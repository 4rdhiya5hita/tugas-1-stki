import subprocess

from flask import Flask, render_template, request, send_file
# from data_retrieval_text import data_retrieval_text
# from data_retrieval_txt import data_retrieval_txt
from data_retrieval import document_retrieval
# from boolean import boolean_retrieval

from bool_try2 import main_co

app = Flask(__name__)

@app.route('/boolean', methods=['GET'])
def boolean():
    # if request.method == 'POST':
    #     name = request.form['name']
    #     data_retrieval_text(name)
        # return f'Hello, {name}!'
    return render_template('index_text.html')

@app.route('/data_retrieval_boolean', methods=['GET', 'POST'])
def boolean_result():
    if request.method == 'POST':
        input_text1 = request.form['input_text1']
        input_text2 = request.form['input_text2']
        input_text3 = request.form['input_text3']
        documents={
            '1': input_text1,
            '2': input_text2,
            '3': input_text3
        }
        query = request.form['search_word']
        # result = boolean_retrieval(query, documents)
        
        result = main_co(query, documents)

        return render_template('result_boolean.html', result=result,  search_word=query)  

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
        stop_word_value = request.form.get('checkbox1')
        wnl_value = request.form.get('checkbox2')
        porter_value = request.form.get('checkbox3')

        input_text1 = request.form['input_text1']
        input_text2 = request.form['input_text2']
        input_text3 = request.form['input_text3']
        search_word = request.form['search_word']
        result = document_retrieval(stop_word_value, wnl_value, porter_value, input_text1, input_text2, input_text3, search_word)
        return render_template('result_text.html', result=result, search_word=search_word)    
    

@app.route('/txt', methods=['GET'])
def txt():
    return render_template('index_txt.html')


@app.route('/data_retrieval_txt', methods=['GET', 'POST'])
def data_result_txt():
    if request.method == 'POST':
        stop_word_value = request.form.get('checkbox1')
        wnl_value = request.form.get('checkbox2')
        porter_value = request.form.get('checkbox3')

        # reading file proccess
        file1 = request.files['myfile1']
        file_contents1 = file1.read() # read the content
        input_text1 = file_contents1.decode('utf-8') # To convert the bytes to a string
        
        file2 = request.files['myfile2']
        file_contents2 = file2.read()
        input_text2 = file_contents2.decode('utf-8')

        file3 = request.files['myfile3']
        file_contents3 = file3.read()
        input_text3 = file_contents3.decode('utf-8')

        search_word = request.form['search_word']
        
        result = document_retrieval(stop_word_value, wnl_value, porter_value, input_text1, input_text2, input_text3, search_word)
        # print(result)

        # return file_contents
        return render_template('result_txt.html', result=result, search_word=search_word)


@app.route('/', methods=['GET'])
def index():
    image_url = '/img_01.jpg'
    return render_template('index.html', image_url=image_url)

@app.route('/submit', methods=['POST'])
def submit():
    checkbox1_value = request.form.get('checkbox1')
    checkbox2_value = request.form.get('checkbox2')
    checkbox3_value = request.form.get('checkbox3')

    # Lakukan sesuatu dengan nilai checkbox yang diterima
    # Misalnya, cetak nilai ke konsol
    print("Checkbox 1:", checkbox1_value)
    print("Checkbox 2:", checkbox2_value)
    print("Checkbox 3:", checkbox3_value)

    return f"Data checkbox telah diterima. Checkbox 1: {checkbox1_value}, Checkbox 2: {checkbox2_value}, Checkbox 3: {checkbox3_value}"
    
if __name__ == '__main__':
    app.run(debug=True)
