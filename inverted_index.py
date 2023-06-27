import numpy as np
import pandas as pd
import nltk
import re
import glob
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

Doc_1 = "breakthrough drug for schizophrenia drug"
Doc_2 = "new schizophrenia drug"
Doc_3 = "new approach for new treatment of schizophrenia"
Doc_4 = "new hopes for schizophrenia patients"
docs = [Doc_1,Doc_2,Doc_3,Doc_4]

# Preprosessing
def preprosess(text, stoptog):

    # Tokenisasai
    words = word_tokenize(text)

    print("Tokenisasi :")
    print(words, "\n")

    # Mengubah menjadi huruf kecil dan menghapus tanda baca
    words_clean = [word.lower() for word in words if word.isalpha()]

    print("Cleaning :")
    print(words_clean, "\n")

    # Stemming dan Stopword
    stemmer = PorterStemmer()
    stop_words = set(stopwords.words('english'))

    if stoptog == 'y':
        words_tokens = [stemmer.stem(word) for word in words if word not in stop_words]
    else:
        words_tokens = [stemmer.stem(word) for word in words]

    print("Stopword Removal dan Stemming :")
    print(words_tokens, "\n")

    return words_tokens


# Incident Matrix
def im(stoppick):
    # Preprocessing masing-masing doc
    docs_pros = []
    n = 1
    for doc in docs :
        print("prosessing doc #",n)
        print("---------------------------------")
        docs_pros.append(preprosess(doc, stoppick))
        n += 1

    print("---------------------------------")
    print("Preprosesing :")
    print(docs_pros, "\n")

    # Mencari kata unik
    unique_terms = []
    for doc in docs_pros:
        for term in doc:
            if term not in unique_terms:
                unique_terms.append(term)

    print("Unique Terms :")
    print(unique_terms, "\n")

    # Membuat incident matrix
    doc_term_matrix = {}
    for term in unique_terms:
        doc_term_matrix[term] = []

        for doc in docs_pros:
            if term in doc:
                doc_term_matrix[term].append(1)
            else: doc_term_matrix[term].append(0)

    # Menampilkan incident matrix
    df = pd.DataFrame(doc_term_matrix)
    df = df.rename(index=lambda x: "Doc_" + str(x+1))
    print("Matrix :")
    print(df.transpose())
    return doc_term_matrix

# Inverted Inddex
def inver_i(stoppick):
    # Preprocessing masing-masing doc
    docs_pros = []
    docrefs = []
    n = 1
    for doc in docs :
        print("prosessing doc #",n)
        print("---------------------------------")
        docs_pros.append(preprosess(doc, stoppick))
        if stoppick == 'y':
            docrefs.append(preprosess(doc, 'n'))
        else:
            docrefs = docs_pros
        n += 1

    print("---------------------------------")
    print("Preprosesing :")
    print(docs_pros, "\n")

    # Mencari kata unik
    unique_terms = []
    for doc in docs_pros:
        for term in doc:
            if term not in unique_terms:
                unique_terms.append(term)

    print("Unique Terms :")
    print(unique_terms, "\n")   

    # Membuat inverted index
    doc_inverse_index = {}
    for term in unique_terms:
        doc_inverse_index[term] = []
        for doc in docrefs:
            wordcount = 0
            wordpos = 0
            wordposlist = []
            if term in doc:
                docnum = docrefs.index(doc)+1
                for word in doc:
                    wordpos += 1
                    if word == term:
                        wordcount += 1
                        wordposlist.append(wordpos)
                doc_inverse_index[term].append([docnum,wordcount,wordposlist])

    # Menampilkan inverted index
    print("Inverted Index : ")
    for item in doc_inverse_index:
        print (item + " :", doc_inverse_index[item])


# Jalankan fungsi sesuai mode
def match_mode():
    # Pilihan mode
    print("1. incident matrix")
    print("2. inverted index")
    mode = input("Input your choice: ")
    print('')

    # Pilihan penghapusan Stopword
    stoppick = input("Hapus Stopword? (y/n): ")
    print('')
    stoppick = stoppick.lower()

    if mode == "1":
        im(stoppick)
    elif mode == "2":
        inver_i(stoppick)
    else:
        print("Mode tidak ditemukan")

match_mode()