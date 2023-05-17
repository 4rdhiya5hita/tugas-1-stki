import string
import math
import numpy as np
from scipy.stats import rankdata

# Example using nltk for data retrieval purpose
import nltk
nltk.download('omw-1.4')
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer, PorterStemmer


   
def boolean_retrieval (input_doc1, input_doc2, input_doc3, search_word):
    # Tokenize the documents
    documents = [input_doc1, input_doc2, input_doc3]

    tokens = [word_tokenize(doc.lower()) for doc in documents]

# Remove stopwords
    stopwords_list = stopwords.words("english")
    filtered_tokens = [[token for token in doc if token not in stopwords_list] for doc in tokens]

# Apply stemming
    stemmer = PorterStemmer()
    stemmed_tokens = [[stemmer.stem(token) for token in doc] for doc in filtered_tokens]

# Define the query
    query = search_word

# Tokenize and stem the query
    query_tokens = [stemmer.stem(token.lower()) for token in word_tokenize(query) if token.lower() not in stopwords_list]
    result = []
    docs = []  # Dictionary untuk menyimpan nomor dokumen
    for i, doc in enumerate(stemmed_tokens):
        if all(term in doc for term in query_tokens):
            result.append(documents[i])
            docs.append(i+1)   # Tambahkan nomor dokumen ke dalam dictionary
    return {'doc': docs, 'text': result}


def document_retrieval (input_doc1, input_doc2, input_doc3, search_word):
    # arr_doc1 = []
    # arr_doc2 = []
    arr_doc1 = data_retrieval(input_doc1)
    arr_doc2 = data_retrieval(input_doc2)
    arr_doc3 = data_retrieval(input_doc3)
    token_array = list(set(arr_doc1 + arr_doc2 + arr_doc3))
    # token_array = arr.array('u', arr_doc)


    q = []
    d1 = []
    d2 = []
    d3 = []

    for word in token_array:
        if word == search_word:
            q.append(1)
        else:
            q.append(0)

        if word in arr_doc1:
            d1.append(1)
        else:
            d1.append(0)

        if word in arr_doc2:
            d2.append(1)
        else:
            d2.append(0)

        if word in arr_doc3:
            d3.append(1)
        else:
            d3.append(0)

            # match_word.append(word)

    df = []
    D = []
    log = []
    w_q = []
    w_d1 = []
    w_d2 = []
    w_d3 = []
    v_q = []
    v_d1 = []
    v_d2 = []
    v_d3 = []
    vsm_d1 = []
    vsm_d2 = []
    vsm_d3 = []
    cos_document = []
    data_vector_Wq = 0
    i = 0
    while i < len(token_array):
        sum_d = int(d1[i]) + int(d2[i]) + int(d3[i])
        D_df = 3/sum_d
        idf_log = format(math.log10(D_df), ".3f")

        if q[i] == 0:
            Wq = "0"
            vector_Wq = "0"
        else:
            Wq = idf_log*q[i]
            vector_Wq = format(pow(float(Wq), 2), ".3f")
            data_vector_Wq = vector_Wq

        if d1[i] == 0:
            W1 = "0"
            vector_W1 = "0"
            vsm_W1 = "0"
        else:
            W1 = idf_log*d1[i]
            vector_W1 = format(pow(float(W1), 2), ".3f")
            vsm_W1 = format(float(data_vector_Wq)*float(vector_W1), ".5f")

        if d2[i] == 0:
            W2 = "0"
            vector_W2 = "0"
            vsm_W2 = "0"
        else:
            W2 = idf_log*d2[i]
            vector_W2 = format(pow(float(W2), 2), ".3f")
            vsm_W2 = format(float(data_vector_Wq)*float(vector_W2), ".5f")

        if d3[i] == 0:
            W3 = "0"
            vector_W3 = "0"
            vsm_W3 = "0"
        else:
            W3 = idf_log*d3[i]
            vector_W3 = format(pow(float(W3), 2), ".3f")
            vsm_W3 = format(float(data_vector_Wq)*float(vector_W3), ".5f")
        
        df.append(sum_d)
        D.append(D_df)
        log.append(idf_log)
        w_q.append(Wq)
        w_d1.append(W1)
        w_d2.append(W2)
        w_d3.append(W3)
        v_q.append(vector_Wq)
        v_d1.append(vector_W1)
        v_d2.append(vector_W2)
        v_d3.append(vector_W3)
        vsm_d1.append(vsm_W1)
        vsm_d2.append(vsm_W2)
        vsm_d3.append(vsm_W3)

        i += 1

    sqrt_q = format(pow(sum([float(x) for x in v_q]), 1/2), ".3f")
    sqrt_d1 = format(pow(sum([float(x) for x in v_d1]), 1/2), ".3f")
    sqrt_d2 = format(pow(sum([float(x) for x in v_d2]), 1/2), ".3f")
    sqrt_d3 = format(pow(sum([float(x) for x in v_d3]), 1/2), ".3f")

    sum_vsm_d1 = format(sum([float(x) for x in vsm_d1]), ".4f")
    sum_vsm_d2 = format(sum([float(x) for x in vsm_d2]), ".4f")
    sum_vsm_d3 = format(sum([float(x) for x in vsm_d3]), ".4f")

    cos_d1 = format(float(sum_vsm_d1) / (float(sqrt_q) * float(sqrt_d1)), ".4f")
    cos_d2 = format(float(sum_vsm_d2) / (float(sqrt_q) * float(sqrt_d2)), ".4f")
    cos_d3 = format(float(sum_vsm_d3) / (float(sqrt_q) * float(sqrt_d3)), ".4f")

    cos_document.append(cos_d1)
    cos_document.append(cos_d2)
    cos_document.append(cos_d3)    
    cos_rank = len(cos_document) - rankdata(cos_document, method='average') + 1
    rank = [int(x) for x in cos_rank]

    valid_search_word = search_word.lower()
    count1 = 0
    for word in arr_doc1:
        if valid_search_word == word:
            count1 += 1

    count2 = 0
    for word in arr_doc2:
        if valid_search_word == word:
            count2 += 1
    
    count3 = 0
    for word in arr_doc3:
        if valid_search_word == word:
            count3 += 1
    
    

    return {'arr_doc1': arr_doc1, 'arr_doc2': arr_doc2, 'arr_doc3': arr_doc3, 'count1': count1, 'count2': count2, 'count3': count3, 'search_word': search_word, 
            'token_array': token_array, 'q': q, 'd1': d1, 'd2': d2, 'd3': d3, 'df': df, 'D': D, 'log': log, 'w_q': w_q, 'w_d1': w_d1, 'w_d2': w_d2, 'w_d3': w_d3,
            'v_q': v_q, 'v_d1': v_d1, 'v_d2': v_d2, 'v_d3': v_d3, 'sqrt_q': sqrt_q, 'sqrt_d1': sqrt_d1, 'sqrt_d2': sqrt_d2, 'sqrt_d3': sqrt_d3,
            'vsm_d1': vsm_d1, 'vsm_d2': vsm_d2, 'vsm_d3': vsm_d3, 'sum_vsm_d1': sum_vsm_d1, 'sum_vsm_d2': sum_vsm_d2, 'sum_vsm_d3': sum_vsm_d3,
            'cos_d1': cos_d1, 'cos_d2': cos_d2, 'cos_d3': cos_d3, 'cos_document': cos_document, 'cos_rank': rank}    


def data_retrieval(input_text):
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
    # return {'final_sentence': final_sentence, "input_text": input_text}
    return without_punctuation

