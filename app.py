from flask import Flask, render_template, request
from data_retrieval_text import data_retrieval_text

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

if __name__ == '__main__':
    app.run(debug=True)
