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
def data_retrieval_text(input_text):
    input_text = request.form['input_text']
    # input_text = "She sat down with her notebook in her hand, her mind wandering to faraway places. She paused and considered all that had happened. It hadn't gone as expected. When the day began she thought it was going to be a bad one, but as she sat recalling the day's events to write them down, she had to admit, it had been a rather marvelous day."

    # Create a stop word list for English
    stop_words = ["n't", 'was', "couldn't", "hadn't", "aren't", "shouldn't", "couldn't", "hasn't", "that'll", "you've", "mightn't", "wouldn't", "doesn't", "wasn't", "haven't", "mustn'", 'mightn', 'shan', "needn't", 'that', "she's", "shouldn't", 'now', "weren't", "don't", "mustn't", "hadn't", "weren't", "won't", "you'd", "needn't", "aren't", "wasn'", "didn't", 'didn', "it's", "isn't", "hasn'", 'wouldn', "doesn'", 'to', 'how', 'we', 'not', 'where', 'he', 'itself', 'can', 'nor', 'few', 'had', 'here', 'them', 'hers', 'this', 'under', 'all', 'same', 'by', 'yourself', 'other', 'out', 'my', 'about', 'will', 'some', 'herself', 'as', 'these', 'do', 'very', 'from', 'then', 'yourselves', 'above', 'most', 'it', 'any', 'only', 'ma', 'for', 'no', 'you', 'between', 'such', 'your', 'ain', 'in', 'being', 'up', 'because', 'him', 'more', 'while', 'were', 'into', 'haven', 'his', 'both', 'having', 'myself', 'is', 'than', 'ourselves', 'but', "should've", 'when', 'hadn', 'himself', "you'll", 'its', 'until', 'are', 'and', 'further', 'if', 'off', 'won', 'who', 'i', 'has', 'during', 'so', 'isn', "you're", 'have', 'again', 'does', 'below', 'theirs', 'ours', 'the', 'through', 'own', 'those', 'too', 'be', 'on', 'doing', 'don', 'me', 'should', 'down', 'which', 'after', 're', 'once', 'their', 'against', 'whom', 'they', 'what', 'an', 'each', 'at', 'themselves', 'been', "shan't", 'she', 'did', 'with', 'our', 'there', 'just', 'over', 'why', 'll', 'before', 'of', 'her', 'or', 'yours', 've', 'am', 'y', "'s", 'o', 'm', 'd', "a"]
    # stop_words = set(stopwords.words('english'))
    # stop_words.add('was')
    # stop_words_list = list(stop_words)
    # print(stop_words_list)

    tokenizing_sentence = [word for word in word_tokenize(input_text.lower()) if word not in stop_words]
    # print(tokenizing_sentence)

    porter = PorterStemmer()    
    wnl = WordNetLemmatizer()    
    
    # NEW FORMULA WITH PORTER AND WNL
    new_sentence = []
    i = 0
    while(i<len(tokenizing_sentence)):
        if(str(tokenizing_sentence[i]).endswith('e')):
            lemmatized_word_e = wnl.lemmatize(str(tokenizing_sentence[i]))
            new_sentence.append(lemmatized_word_e)
            # print(lemmatized_word)
        elif(str(tokenizing_sentence[i]).endswith('s')):
            lemmatized_word_s = wnl.lemmatize(str(tokenizing_sentence[i]))
            new_sentence.append(lemmatized_word_s)
            # print(lemmatized_word_s)
        elif(str(tokenizing_sentence[i]).endswith('y')):
            new_sentence.append(str(tokenizing_sentence[i]))
        elif(str(tokenizing_sentence[i]).endswith('ed')):
            lemmatized_word_ed = wnl.lemmatize(str(tokenizing_sentence[i]), pos='v')
            new_sentence.append(lemmatized_word_ed)
            # print(lemmatized_word_ed)
        else:
            stemmed_words = porter.stem(str(tokenizing_sentence[i]))
            new_sentence.append(stemmed_words)
            # print(stemmed_words)

        i+=1

    # tokens_without_punct
    without_punctuation = [token for token in new_sentence if token not in string.punctuation]
    final_sentence = ' '.join(without_punctuation)
    # print(tokens_without_punct)

    # print(final_sentence)
    # , 'porter_sentence': porter_sentence, 'wnl_sentence': wnl_sentence
    return {'final_sentence': final_sentence, "input_text": input_text}

# data_retrieval_text()