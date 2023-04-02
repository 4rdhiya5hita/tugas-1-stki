import string
# Example using nltk for data retrieval purpose
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer, PorterStemmer

from flask import Flask, request, render_template
# app = Flask(__name__)

# @app.route('/data_retrieval_text', methods=['GET', 'POST'])
def uji_data_retrieval_text():
    # nama = f"Hello, {name}!"
    # if request.method == 'POST':
    #     name = request.form['name']
    #     result = f"Hello, {name}!"    
    # input_text = request.form['input_text']
    input_text = "Should he write it down? That was the question running through his mind. He couldn't believe what had just happened and he knew nobody else would believe him as well. Even if he documented what had happened by writing it down, he still didn't believe anyone would still believe it. So the question remained. Was it be worth it to actually write it down?"

    # note: a simple code for case folding a sentence
    # folded_sentence = input_text.lower()
    # print(folded_sentence)
    # list_data.append(folded_sentence)

    #  note: a simple code for tokenizing a sentence
    # tokenizing_sentence = nltk.word_tokenize(folded_sentence)
    # print(tokenizing_sentence)    

    # Create a stop word list for English
    stop_words = ["was", "couldn't", "hadn't", "aren't", "shouldn't", "couldn't", "hasn't", "that'll", "you've", "mightn't", "wouldn't", "doesn't", "wasn't", "haven't", "mustn'", 'mightn', 'shan', "needn't", 'that', "she's", "shouldn't", 'now', "weren't", "don't", "mustn't", "hadn't", "weren't", "won't", "you'd", "needn't", "aren't", "wasn'", "didn't", 'didn', "it's", "isn't", "hasn'", 'wouldn', "doesn'", 'to', 'how', 'we', 'not', 'where', 'he', 'itself', 'can', 'nor', 'few', 'had', 'here', 'them', 'hers', 'this', 'under', 'all', 'same', 'by', 'yourself', 'other', 'out', 'my', 'about', 'will', 'some', 'herself', 'as', 'these', 'do', 'very', 'from', 'then', 'yourselves', 'above', 'most', 'it', 'any', 'only', 'ma', 'for', 'no', 'you', 'between', 'such', 'your', 'ain', 'in', 'being', 'up', 'because', 'him', 'more', 'while', 'were', 'into', 'haven', 'his', 'both', 'having', 'myself', 'is', 'than', 'ourselves', 'but', "should've", 'when', 'hadn', 'himself', "you'll", 'its', 'until', 'are', 'and', 'further', 'if', 'off', 'won', 'who', 'i', 'has', 'during', 'so', 'isn', "you're", 'have', 'again', 'does', 'below', 'theirs', 'ours', 'the', 'through', 'own', 'those', 'too', 'be', 'on', 'doing', 'don', 'me', 'should', 'down', 'which', 'after', 're', 'once', 'their', 'against', 'whom', 'they', 'what', 'an', 'each', 'at', 'themselves', 'been', "shan't", 'she', 'did', 'with', 'our', 'there', 'just', 'over', 'why', 'll', 'before', 'of', 'her', 'or', 'yours', 've', 'am', 'y', "'s", 'o', 'm', 'd', "a"]
    # stop_words = set(stopwords.words('english'))
    # stop_words_list = list(stop_words)
    # print(stop_words_list)

    tokenizing_sentence = [word for word in word_tokenize(input_text.lower()) if word not in stop_words]

    # for words in tokenizing_sentence:
    #     if words in stop_words:
    #         tokenizing_sentence.remove(words)
    #     else:
    #         continue
    # print(tokenizing_sentence)

    porter = PorterStemmer()
    # stemmed_words = [porter.stem(word) for word in tokenizing_sentence]
    # porter_sentence = ' '.join(stemmed_words)
    
    wnl = WordNetLemmatizer()
    # wnl_sentence = ' '.join([wnl.lemmatize(w) for w in tokenizing_sentence])
    
    # NEW FORMULA WITH PORTER AND WNL
    new_sentence = []
    i = 0
    while(i<len(tokenizing_sentence)):
        if(str(tokenizing_sentence[i]).endswith('e')):
            lemmatized_word_e = wnl.lemmatize(str(tokenizing_sentence[i]))
            new_sentence.append(lemmatized_word_e)
            # print("-- lemmatized --")
            # print(lemmatized_word)
            # print("-- lemmatized --")
        # elif(str(tokenizing_sentence[i]).endswith('s')):
        #     lemmatized_word_s = wnl.lemmatize(str(tokenizing_sentence[i]))
        #     new_sentence.append(lemmatized_word_s)
            # print(lemmatized_word_s)
        elif(str(tokenizing_sentence[i]).endswith('ed')):
            lemmatized_word_ed = wnl.lemmatize(str(tokenizing_sentence[i]), pos='v')
            new_sentence.append(lemmatized_word_ed)
            # print(lemmatized_word_ed)
        else:
            stemmed_words = porter.stem(str(tokenizing_sentence[i]))
            new_sentence.append(stemmed_words)
            # print(stemmed_words)

        i+=1

    # filter out punctuation
    # tokens_without_punct
    final_sentence = [token for token in new_sentence if token not in string.punctuation]
    # print(tokens_without_punct)

    print(final_sentence)
    
    # without_e = []
    # join_words = ' '.join(tokens_without_punct)
    # if (join_words.endswith('e')):
    #     print(join_words)
    #     wnl_words = wnl.lemmatize(join_words)
    #     wnl_words_token = nltk.word_tokenize(wnl_words)

    #     stemmed_wnl = [porter.stem(word) for word in wnl_words_token]
    #     wnl_porter_sentence = ' '.join(stemmed_wnl)
        # porter.stem(wnl_sentence)  
    
    # 'wnl_porter_sentence': wnl_porter_sentence, 

    # return {'wnl_porter_sentence': wnl_porter_sentence, 'porter_sentence': porter_sentence, 'wnl_sentence': wnl_sentence}

uji_data_retrieval_text()