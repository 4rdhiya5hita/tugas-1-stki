import string
# Example using nltk for data retrieval purpose
import nltk
# import numpy as np # numpy for NaN support

# Stop word testing requirements
nltk.download('stopwords')
from nltk.corpus import stopwords # Import the stopwords module from the nltk.corpus package

# Stemming testing requirements
nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer, PorterStemmer

# Example using the mysql-connector-python module for MySQL
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_sentence"
)
cursor = conn.cursor()

def data_retrieval_db():
    # Main array in order to get the final result
    list_data = ''

    # note: looping and fetching every sentences to an array
    len_data = 100
    i = 0
    while i<len_data:
        cursor.execute("SELECT * FROM tb_sentences")
        data = cursor.fetchall()
        # print(data)

        # note: variable to define how many sentences will be tokenizing
        index = [x[0] for x in data]
        len_data = len(index) # len_data = 4, length of the len_data in database is 4
        
        # note: this will get the string sentence at index 2 in variable "data"
        sentences = data[i][1]
        # print(sentences)

        # note: a simple code for case folding a sentence
        folded_sentence = sentences.lower()
        # print(folded_sentence)
        # list_data.append(folded_sentence)
        list_data = str(list_data) + ' ' + folded_sentence

        i += 1


    # print(list_data)

    #  note: a simple code for tokenizing a sentence
    tokenizing_sentence = nltk.word_tokenize(list_data)
    # print(tokenizing_sentence)

    # filter out punctuation
    tokens_without_punct = [token for token in tokenizing_sentence if token not in string.punctuation]
    # print(tokens_without_punct)

    # Create a stop word list for English
    stop_words = set(stopwords.words('english'))
    # stop_words_list = list(stop_words)
    # print(stop_words_list)

    for words in tokens_without_punct:
        if words in stop_words:
            tokens_without_punct.remove(words)
            # print(tokens_without_punct)
        else:
            continue
    token_sentence = ' '.join(tokens_without_punct)
    # print(tokenizing_sentence)

    porter = PorterStemmer()
    wnl = WordNetLemmatizer()
    
    # Stem each word in the sentence using the Porter Stemmer
    # stemmed_words = [stemmer.stem(word) for word in tokens_without_punct]
    
    # Upgrade to WNL for 'e' problem in word
    stemmed_words = wnl.lemmatize(token_sentence) if wnl.lemmatize(token_sentence).endswith('e') else porter.stem(token_sentence)
    print(stemmed_words)

    # Join the stemmed words back into a sentence
    # stemmed_sentence = ' '.join(stemmed_words)
    # print(stemmed_sentence)

    # len_tokens = len(tokenizing_sentence)
    # len_stopwords = len(stop_words)
    # j = 0
    # k = 0

    # while j<len_tokens:
    #     # print(tokenizing_sentence[j])
    #     while k<len_stopwords:
    #         # print(stop_words[k])
    #         if tokenizing_sentence[j] == stop_words[k]:
    #             list_data.remove(tokenizing_sentence[j])        
    #         k += 1
    #     j += 1

    # print(list_data)        

    conn.close()

data_retrieval_db()
    # array = []

    # sentence = "This is a sample sentence to tokenize."
    # array.extend(tokens)

    # print(tokens)
    # print(array)
