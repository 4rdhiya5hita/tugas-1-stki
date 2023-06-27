import numpy as np
import pandas as pd
import nltk
import re
import glob
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

Doc_1 = "Innovative medication for diabetes control"
Doc_2 = "Novel medication for the control and treatment of diabetes at the same time of medication"
Doc_3 = "State-of-the-art treatment for controlling diabetes with advanced treatment"
docs = [Doc_1,Doc_2,Doc_3]

# Preprosessing
def preprosess(text, stoptog):

    # Menghapus tanda baca "-"
    text = re.sub(r"\b-\b", "", text)

    # Tokenisasi
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
def build_incident_matrix():
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


def document_ranking(query, doc_term_matrix):
        query_words = query.split(' ')
        document_scores = {}

        for doc_idx, doc in enumerate(docs):
            score = 0
            for word in query_words:
                if word in doc_term_matrix:
                    score += doc_term_matrix[word][doc_idx]
            document_scores[doc_idx + 1] = score

        sorted_documents = sorted(document_scores.items(), key=lambda x: x[1], reverse=True)
        ranking_table = pd.DataFrame(columns=['Document', 'Score'])
        for doc, score in sorted_documents:
          ranking_table.loc[len(ranking_table)] = ['Doc_' + str(doc), score]

        return ranking_table

stoppick = 'y'
        
# Inverted Inddex
def build_inverted_index():
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
           docrefs.append(docs_pros[-1])
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
        for doc_num, doc in enumerate(docrefs,start=1):
            word_count = 0
            word_pos = 0
            word_pos_list = []
            if term in doc:
                for word_pos, word in enumerate(doc, start=1):
                    if word == term:
                        word_count += 1
                        word_pos_list.append(word_pos)
                doc_inverse_index[term].append([doc_num, word_count, word_pos_list])

    # Menampilkan inverted index
    print("Inverted List : ")
    for item in doc_inverse_index:
        print (item + " :", doc_inverse_index[item])

    return doc_inverse_index

def document_ranking_inverted(query, inverted_index):
    query_words = query.split(' ')
    document_scores = {}

    for term in query_words:
        if term in inverted_index:
            docs_list = inverted_index[term]
            for doc_info in docs_list:
                doc_idx = doc_info[0]
                score = doc_info[1]
                if doc_idx in document_scores:
                    document_scores[doc_idx] += score
                else:
                    document_scores[doc_idx] = score

    sorted_documents = sorted(document_scores.items(), key=lambda x: x[1], reverse=True)
    ranking_table = pd.DataFrame(columns=['Document', 'Score'])
    for doc, score in sorted_documents:
        ranking_table.loc[len(ranking_table)] = ['Doc_' + str(doc), score]

    return ranking_table
stoppick = 'y'
                
# Pilihan menu
print("Please choose between 2 menu below:")
print("1. Incident matrix")
print("2. Inverted index")
mode = input("Enter your choice: ")
print('')

    # Pilihan penghapusan Stopword
    stoppick = input("Hapus Stopword? (y/n): ")
    print('')
    stoppick = stoppick.lower()

# Jalankan fungsi sesuai mode
if mode == "1":
    # Panggil fungsi build_incident_matrix() untuk membangun incident matrix
    doc_term_matrix = build_incident_matrix()

    while True:
        # Lakukan peringkat dokumen berdasarkan query menggunakan incident matrix
        query = input("Masukkan query: ")
        ranking_table = document_ranking(query, doc_term_matrix)

        print("\nQuery Ranking (Incident Matrix):")
        print(ranking_table)

        # Tanya pengguna apakah ingin melakukan query ranking lainnya
        choice = input("Apakah Anda ingin melakukan query ranking lainnya? (y/n) ")
        if choice.lower() != 'y':
            break

elif mode == "2":
    # Panggil fungsi build_inverted_index() untuk membangun inverted index
    inverted_index = build_inverted_index()

    while True:
        # Lakukan peringkat dokumen berdasarkan query menggunakan inverted index
        query = input("Masukkan query: ")
        ranking_table = document_ranking_inverted(query, inverted_index)

        print("\nQuery Ranking (Inverted Index):")
        print(ranking_table)

        # Tanya pengguna apakah ingin melakukan query ranking lainnya
        choice = input("Apakah Anda ingin melakukan query ranking lainnya? (y/n) ")
        if choice.lower() != 'y':
            break

else:
    print("Invalid input!")
