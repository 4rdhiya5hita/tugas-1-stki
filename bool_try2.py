import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer
import pandas as pd
from nltk.corpus import stopwords
import re
# Data contoh
# documents = {
#     1: "Blue is my favorite color",
#     2: "Sky is blue and sea is blue",
#     3: "sky is blue and sky is beautiful",
#     4: "color of sky and sea is blue",
#     5: "I saw a blue car yesterday"
# }

# Fungsi untuk menghitung term frequency (tf)
def calculate_tf(documents):
    tf_table = {}
    tokenized_docs = {}
    stemmer = PorterStemmer()  # Inisialisasi stemmer
    
    # Tokenisasi dokumen dan menghitung frekuensi kemunculan term dalam setiap dokumen
    for doc_id, doc_text in documents.items():
        tokens = word_tokenize(doc_text.lower())  # Tokenisasi dan konversi ke huruf kecil
        stop_words = set(stopwords.words('english'))  # Menggunakan stop words bahasa Inggris
        tokens = [token for token in tokens if token not in stop_words]  # Menghapus stop words
        stemmed_tokens = [stemmer.stem(token) for token in tokens]  # Stemming
        tokenized_docs[doc_id] = stemmed_tokens
        fd = FreqDist(stemmed_tokens)
        tf_table[doc_id] = fd
    
    # Menggabungkan semua term unik dalam semua dokumen
    all_terms = set()
    for tokens in tokenized_docs.values():
        all_terms.update(tokens)

    # Membuat dataframe untuk tabel term frequency
    tf_df = pd.DataFrame(columns=['Term'] + list(documents.keys()))
    
    for term in all_terms:
        tf_values = []
        for doc_id, tokens in tokenized_docs.items():
            tf_values.append(int(term in tokens))  # Jika term ada dalam tokens, nilai biner = 1, jika tidak = 0
        tf_df.loc[len(tf_df)] = [term] + tf_values
    tf_df['Binary_Total'] = tf_df.iloc[:, 1:].apply(lambda x: ''.join(map(str, x)), axis=1)
    return tf_df

 #membuat dataframe-> jadi masing2 kata menjadi bilangan biner

def documents_containing_term(term, tf_df):
    term_lower = term.lower()
    if ' ' in term_lower:
        # Split the term while preserving parentheses
        terms = re.findall(r'\(|\)|\w+|\S+\s*', term_lower)
        binary_values = []
        for t in terms:
            if t == '(' or t == ')':
                binary_values.append(t)
            else:
                binary_value = tf_df.loc[tf_df['Term'] == t.strip('()'), 'Binary_Total'].values[0] if len(tf_df.loc[tf_df['Term'] == t.strip('()')]) > 0 else None
                binary_values.append(binary_value)
        return ''.join(binary_values) if all(v is not None for v in binary_values) else None
    else:
        result = tf_df.loc[tf_df['Term'] == term_lower, 'Binary_Total'].values
        return result[0] if len(result) > 0 else None

#langsung mengubah query menjadi biner


def boolean_retrieval(documents):
   
    stack = []
    output_queue = []
    precedence = {'AND': 2, 'OR': 1, 'NOT': 3}
    operators = set(['AND', 'OR', 'NOT'])

    # Mengonversi query menjadi notasi postfix menggunakan algoritma shunting yard
    for term in documents:
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

    # Mengevaluasi notasi postfix
    for term in output_queue:
        if term in operators:
            operand2 = stack.pop()
            if term == 'NOT':
                result = bin(int(operand2, 2) ^ int('1' * len(operand2), 2))[2:].zfill(len(operand2))
            else:
                operand1 = stack.pop()
                if term == 'AND':
                    result = bin(int(operand1, 2) & int(operand2, 2))[2:].zfill(len(operand1))
                elif term == 'OR':
                    result = bin(int(operand1, 2) | int(operand2, 2))[2:].zfill(len(operand1))
            stack.append(result)
        else:
            stack.append(term)

    # Hasil akhir adalah operand terakhir yang tersisa di stack
    result = stack.pop()
    return result

# Contoh penggunaan
def main_co(query, documents):
    tf_df = calculate_tf(documents)
    query = query
    query_terms = re.findall(r'\(|\)|\w+|\S+\s*', query)
    binary_values = [documents_containing_term(term, tf_df) or term for term in query_terms]
    results = boolean_retrieval(binary_values)
    matching_documents = [doc_id for doc_id, result in enumerate(results, start=1) if result == '1']
    # boolean = [documents[id] for id in matching_documents if id in documents]
    result = {
        'doc': matching_documents,
        'text': documents,
        # 'text': [documents[id] for id in matching_documents if id in documents]
    }
    
    #documents[doc_id] for doc_id in matching_documents if doc_id in documents
    return result
    # return result
   



# result = main_co('blue AND sky', documents)
# print(result)