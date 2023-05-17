import time
import string
import math
import numpy as np
from scipy.stats import rankdata

# Example using nltk for data retrieval purpose
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer, PorterStemmer

def document_retrieval (stop_word_value, wnl_value, porter_value, input_doc1, input_doc2, input_doc3, search_word):
    # arr_doc1 = []
    # arr_doc2 = []
    arr_query = data_retrieval(stop_word_value, wnl_value, porter_value, search_word)
    arr_doc1 = data_retrieval(stop_word_value, wnl_value, porter_value, input_doc1)
    arr_doc2 = data_retrieval(stop_word_value, wnl_value, porter_value, input_doc2)
    arr_doc3 = data_retrieval(stop_word_value, wnl_value, porter_value, input_doc3)    
    token_array = list(set(arr_doc1 + arr_doc2 + arr_doc3))
    
    count1 = 0
    for word in arr_doc1:
        for search in arr_query:
            if search == word:
                count1 += 1

    count2 = 0
    for word in arr_doc2:
        for search in arr_query:
            if search == word:
                count2 += 1
    
    count3 = 0
    for word in arr_doc3:
        for search in arr_query:
            if search == word:
                count3 += 1
    
    # index = my_list.index(search_word)

    # # Create a new list starting from the search word
    # token_array = my_list[index:]

    # # Append the remaining part of the list to the end of the new list
    # token_array.extend(my_list[:index])
    # # token_array = arr.array('u', arr_doc)

    q = []
    d1_count = []
    d2_count = []
    d3_count = []

    for word in token_array:
        if word in arr_query:
            count_token_query = arr_query.count(word)
            q.append(count_token_query)
        else:
            q.append(0)

        if word in arr_doc1:
            count_token_doc1 = arr_doc1.count(word)
            d1_count.append(count_token_doc1)
        else:
            d1_count.append(0)

        if word in arr_doc2:
            count_token_doc2 = arr_doc2.count(word)
            d2_count.append(count_token_doc2)
        else:
            d2_count.append(0)

        if word in arr_doc3:
            count_token_doc3 = arr_doc3.count(word)
            d3_count.append(count_token_doc3)
        else:
            d3_count.append(0)

            # match_word.append(word)

    # CEK APAKAH KATA YANG DICARI ADA DALAM DOKUMEN
    if 1 in q:
        
        # konversi nilai-nilai pada array menjadi 1 kecuali 0
        d1 = [1 if x != 0 else 0 for x in d1_count]
        d2 = [1 if x != 0 else 0 for x in d2_count]
        d3 = [1 if x != 0 else 0 for x in d3_count]

        df = []
        D = []
        log = []
        log_1 = []
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
            idf_log = float(math.log10(D_df))
            idf_log_abs = abs(idf_log)
            idf_log_formatted = format(idf_log_abs, ".3f")
            idf_1 = idf_log_abs+1
            idf_log_1_formatted = format(idf_1, ".3f")

            if q[i] == 0:
                Wq = "0"
                vector_Wq = "0"
            else:
                Wq = format(idf_1*q[i], ".3f")
                vector_Wq = format(pow(float(Wq), 2), ".3f")
                # data_vector_Wq = vector_Wq

            if d1[i] == 0:
                W1 = "0"
                vector_W1 = "0"
                vsm_W1 = "0"
            else:
                W1 = format(idf_1*d1[i], ".3f")
                vector_W1 = format(pow(float(W1), 2), ".3f")
                vsm_W1 = format(float(vector_Wq)*float(vector_W1), ".3f")

            if d2[i] == 0:
                W2 = "0"
                vector_W2 = "0"
                vsm_W2 = "0"
            else:
                W2 = format(idf_1*d2[i], ".3f")
                vector_W2 = format(pow(float(W2), 2), ".3f")
                vsm_W2 = format(float(vector_Wq)*float(vector_W2), ".3f")

            if d3[i] == 0:
                W3 = "0"
                vector_W3 = "0"
                vsm_W3 = "0"
            else:
                W3 = format(idf_1*d3[i], ".3f")
                vector_W3 = format(pow(float(W3), 2), ".3f")
                vsm_W3 = format(float(vector_Wq)*float(vector_W3), ".3f")

            # time.sleep(1)
            
            df.append(sum_d)
            D.append(D_df)
            log.append(idf_log_formatted)
            log_1.append(idf_log_1_formatted)
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

        sum_vsm_d1 = format(sum([float(x) for x in vsm_d1]), ".3f")
        sum_vsm_d2 = format(sum([float(x) for x in vsm_d2]), ".3f")
        sum_vsm_d3 = format(sum([float(x) for x in vsm_d3]), ".3f")

        cos_d1 = format(float(sum_vsm_d1) / (float(sqrt_q) * float(sqrt_d1)), ".3f")
        cos_d2 = format(float(sum_vsm_d2) / (float(sqrt_q) * float(sqrt_d2)), ".3f")
        cos_d3 = format(float(sum_vsm_d3) / (float(sqrt_q) * float(sqrt_d3)), ".3f")

        cos_document.append(cos_d1)
        cos_document.append(cos_d2)
        cos_document.append(cos_d3)
            
        cos_rank = len(cos_document) - rankdata(cos_document, method='average') + 1
        rank = [int(x) for x in cos_rank]
        
        return {'arr_doc1': arr_doc1, 'arr_doc2': arr_doc2, 'arr_doc3': arr_doc3, 'count1': count1, 'count2': count2, 'count3': count3, 'search_word': search_word, 
                'token_array': token_array, 'q': q, 'd1': d1_count, 'd2': d2_count, 'd3': d3_count, 'df': df, 'D': D, 'log': log, 'log_1': log_1, 'w_q': w_q, 'w_d1': w_d1, 'w_d2': w_d2, 'w_d3': w_d3,
                'v_q': v_q, 'v_d1': v_d1, 'v_d2': v_d2, 'v_d3': v_d3, 'sqrt_q': sqrt_q, 'sqrt_d1': sqrt_d1, 'sqrt_d2': sqrt_d2, 'sqrt_d3': sqrt_d3,
                'vsm_d1': vsm_d1, 'vsm_d2': vsm_d2, 'vsm_d3': vsm_d3, 'sum_vsm_d1': sum_vsm_d1, 'sum_vsm_d2': sum_vsm_d2, 'sum_vsm_d3': sum_vsm_d3,
                'cos_d1': cos_d1, 'cos_d2': cos_d2, 'cos_d3': cos_d3, 'cos_document': cos_document, 'cos_rank': rank}    
    
    else:
        cos_d1 = 0
        cos_d2 = 0
        cos_d3 = 0
        rank = 'x'
        
        return {'arr_doc1': arr_doc1, 'arr_doc2': arr_doc2, 'arr_doc3': arr_doc3, 'count1': count1, 'count2': count2, 'count3': count3, 'search_word': search_word, 'cos_d1': cos_d1, 'cos_d2': cos_d2, 'cos_d3': cos_d3, 'cos_rank': rank}    
        


def data_retrieval(stop_word_value, wnl_value, porter_value, input_text):
    # Create a stop word list for English
    if (stop_word_value is None):
        tokenizing_sentence = [word for word in word_tokenize(input_text.lower())]
    else:
        stop_words = ["n't", 'was', "couldn't", "hadn't", "aren't", "shouldn't", "couldn't", "hasn't", "that'll", "you've", "mightn't", "wouldn't", "doesn't", "wasn't", "haven't", "mustn'", 'mightn', 'shan', "needn't", 'that', "she's", "shouldn't", 'now', "weren't", "don't", "mustn't", "hadn't", "weren't", "won't", "you'd", "needn't", "aren't", "wasn'", "didn't", 'didn', "it's", "isn't", "hasn'", 'wouldn', "doesn'", 'to', 'how', 'we', 'not', 'where', 'he', 'itself', 'can', 'nor', 'few', 'had', 'here', 'them', 'hers', 'this', 'under', 'all', 'same', 'by', 'yourself', 'other', 'out', 'my', 'about', 'will', 'some', 'herself', 'as', 'these', 'do', 'very', 'from', 'then', 'yourselves', 'above', 'most', 'it', 'any', 'only', 'ma', 'for', 'no', 'you', 'between', 'such', 'your', 'ain', 'in', 'being', 'up', 'because', 'him', 'more', 'while', 'were', 'into', 'haven', 'his', 'both', 'having', 'myself', 'is', 'than', 'ourselves', 'but', "should've", 'when', 'hadn', 'himself', "you'll", 'its', 'until', 'are', 'and', 'further', 'if', 'off', 'won', 'who', 'i', 'has', 'during', 'so', 'isn', "you're", 'have', 'again', 'does', 'below', 'theirs', 'ours', 'the', 'through', 'own', 'those', 'too', 'be', 'on', 'doing', 'don', 'me', 'should', 'down', 'which', 'after', 're', 'once', 'their', 'against', 'whom', 'they', 'what', 'an', 'each', 'at', 'themselves', 'been', "shan't", 'she', 'did', 'with', 'our', 'there', 'just', 'over', 'why', 'll', 'before', 'of', 'her', 'or', 'yours', 've', 'am', 'y', "'s", 'o', 'm', 'd', "a"]
        tokenizing_sentence = [word for word in word_tokenize(input_text.lower()) if word not in stop_words]
    # stop_words = set(stopwords.words('english'))
    # stop_words.add('was')
    # stop_words_list = list(stop_words)
    # print(stop_words_list)

    # NEW FORMULA WITH PORTER AND WNL
    if (wnl_value is not None and porter_value is not None):    
        new_sentence = wnl_porter(tokenizing_sentence)
    elif(wnl_value is not None):
        new_sentence = wnl(tokenizing_sentence)
    elif(porter_value is not None):
        new_sentence = porter(tokenizing_sentence)
    else:
        new_sentence = tokenizing_sentence        

    # tokens_without_punct
    without_punctuation = [token for token in new_sentence if token not in string.punctuation]
    final_sentence = ' '.join(without_punctuation)
    # print(tokens_without_punct)

    # print(final_sentence)
    # , 'porter_sentence': porter_sentence, 'wnl_sentence': wnl_sentence
    # return {'final_sentence': final_sentence, "input_text": input_text}
    return without_punctuation

def wnl(tokenizing_sentence):
    wnl = WordNetLemmatizer()
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
        else:
            new_sentence.append(tokenizing_sentence[i])
        i+=1

    return new_sentence


def porter(tokenizing_sentence):
    porter = PorterStemmer()
    new_sentence = []
    i = 0
    while(i<len(tokenizing_sentence)):
        stemmed_words = porter.stem(str(tokenizing_sentence[i]))
        new_sentence.append(stemmed_words)
            # print(lemmatized_word_ed)
        i+=1
    return new_sentence

def wnl_porter(tokenizing_sentence):
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
    
    return new_sentence
    
