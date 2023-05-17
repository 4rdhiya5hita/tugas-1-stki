import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import pandas as pd

# Preprocessing Dokumen
def preprocess_document(doc_text):
    tokens = word_tokenize(doc_text.lower())  # Tokenisasi dan konversi ke huruf kecil
    tokens = [token for token in tokens if token.isalpha()]  # Hanya menyimpan token yang berisi huruf saja
    stop_words = set(stopwords.words('english'))  # Menggunakan stop words bahasa Inggris
    tokens = [token for token in tokens if token not in stop_words]  # Menghapus stop words
    return tokens

# Pembuatan Inverted Index
def build_inverted_index(documents):
    inverted_index = {}
    for doc_id, doc_text in documents.items():
        tokens = preprocess_document(doc_text)
        for token in tokens:
            if token in inverted_index:
                inverted_index[token].add(doc_id)
            else:
                inverted_index[token] = {doc_id}
    return inverted_index

# Pencarian dengan Inverted Index
def boolean_retrieval(query, inverted_index, documents):
    query_terms = preprocess_document(query)
    stack = []
    output_queue = []
    precedence = {'AND': 2, 'OR': 1, 'NOT': 3}
    operators = set(['AND', 'OR', 'NOT'])

    # Mengonversi query menjadi notasi postfix menggunakan algoritma Shunting Yard
    for term in query_terms:
        if term in operators:
            while stack and stack[-1] != '(' and precedence[term] <= precedence[stack[-1]]:
                output_queue.append(stack.pop())
            stack.append(term)
        elif term == '(':
            stack.append(term)
        elif term == ')':
            while stack and stack[-1] != '(':
                output_queue.append(stack.pop())
            stack.pop()
        else:
            output_queue.append(term)
    
    while stack:
        output_queue.append(stack.pop())

    # Mengevaluasi notasi postfix dengan inverted index
    for term in output_queue:
        if term in operators:
            operand2 = stack.pop()
            if term == 'NOT':
                result = set(inverted_index.keys()) - inverted_index[operand2]
            else:
                operand1 = stack.pop()
                if term == 'AND':
                    result = inverted_index[operand1] & inverted_index[operand2]
                elif term == 'OR':
                    result = inverted_index[operand1] | inverted_index[operand2]
            stack.append(result)
        else:
            stack.append(inverted_index[term])

    # Hasil akhir adalah operand terakhir yang tersisa di stack
    
    result = stack.pop()
    return {'doc': result, 'text': [documents[doc_id] for doc_id in result]}

# Data contoh
documents = {
    1: "Saya suka makan nasi goreng",
    2: "Ayah saya bekerja sebagai dokter",
    3: "Ibu saya menyukai bunga",
    4: "Saya sedang membaca buku tentang sejarah",
    5: "Anjing dan kucing adalah hewan peliharaan"
}

# Membangun inverted index


# Contoh penggunaan boolean retrieval dengan inverted index
# query = "saya AND makan OR buku NOT ibu"
# result = boolean_retrieval(query, inverted_index)