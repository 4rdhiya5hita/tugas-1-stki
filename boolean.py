# Data contoh
from data_retrieval import data_retrieval
documents = {
    1: "Saya suka makan nasi goreng",
    2: "Ayah saya bekerja sebagai dokter",
    3: "Ibu saya menyukai bunga",
    4: "Saya sedang makan buku tentang sejarah",
    5: "Anjing dan kucing adalah hewan peliharaan"
}

# Fungsi untuk melakukan boolean retrieval dengan penanganan tanda kurung
def boolean_retrieval(query, documents):
    query_terms = query.lower().split()  # Memisahkan query menjadi term-term terpisah
    stack = []
    output_queue = []
    precedence = {'and': 2, 'or': 1, 'not': 3}
    operators = set(['and', 'or', 'not'])

    # Mengonversi query menjadi notasi postfix menggunakan algoritma shunting yard
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

    # Mengevaluasi notasi postfix
    for term in output_queue:
        if term in operators:
            operand2 = stack.pop()
            if term == 'not':
                result = set(documents.keys()) - set(operand2)
            else:
                operand1 = stack.pop()
                if term == 'and':
                    result = set(operand1) & set(operand2)
                elif term == 'or':
                    result = set(operand1) | set(operand2)
            stack.append(list(result))
        else:
            stack.append(documents_containing_term(term, documents))

    # Hasil akhir adalah operand terakhir yang tersisa di stack
    result = stack.pop()
    # return {'doc': result, 'text': [documents[doc_id] for doc_id in result]}
    return result

# Fungsi untuk mencari dokumen yang mengandung suatu term
def documents_containing_term(term, documents):
    result = []
  
    for doc_id, doc_text in enumerate(documents):
        if term in doc_text:
            result.append(doc_id)
    return result

query = "saya AND makan NOT buku"
result = boolean_retrieval(query, documents)

print("Hasil Pencarian:")
for doc_id in result:
    print(f"Dokumen {doc_id}: {documents[doc_id]}")

import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import pandas as pd

# Data contoh


# Fungsi untuk menghitung term frequency (tf)
def calculate_tf(documents):
    tf_table = {}
    tokenized_docs = {}
    
    # Tokenisasi dokumen dan menghitung frekuensi kemunculan term dalam setiap dokumen
    for doc_id, doc_text in documents.items():
        tokens = word_tokenize(doc_text.lower())  # Tokenisasi dan konversi ke huruf kecil
        tokenized_docs[doc_id] = tokens
        fd = FreqDist(tokens)
        tf_table[doc_id] = fd
    
    # Menggabungkan semua term unik dalam semua dokumen
    all_terms = set()
    for tokens in tokenized_docs.values():
        all_terms.update(tokens)
    
    # Membuat dataframe untuk tabel term frequency
    tf_df = pd.DataFrame(columns=['Term'] + list(documents.keys()))
    
    # Mengisi nilai term frequency dalam dataframe
    for term in all_terms:
        tf_values = []
        for doc_id, tokens in tokenized_docs.items():
            tf_values.append(tf_table[doc_id][term])
        tf_df.loc[len(tf_df)] = [term] + tf_values
    
    return tf_df

# Contoh penggunaan untuk menghitung term frequency
tf_table = calculate_tf(documents)

print("Tabel Term Frequency:")
print(tf_table)

