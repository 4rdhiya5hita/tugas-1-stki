import math

# Contoh dokumen
documents = [
    "Ini adalah dokumen pertama.",
    "Ini adalah dokumen kedua.",
    "Ini adalah dokumen ketiga.",
    "Ini adalah dokumen keempat."
]

# Kata kunci
keywords = ["pertama", "ketiga"]

# Hitung TF
tf_values = []
for doc in documents:
    tf_doc = []
    for keyword in keywords:
        tf = doc.lower().count(keyword.lower())
        tf_doc.append(tf)
    tf_values.append(tf_doc)
print(" ")
print(tf_values)

# Hitung IDF
idf_values = []
num_documents = len(documents)
for keyword in keywords:
    num_documents_with_keyword = sum(keyword.lower() in doc.lower() for doc in documents)
    idf = math.log(num_documents / (1 + num_documents_with_keyword))
    idf_values.append(idf)

print(" ")
print(idf_values)

# Hitung TF-IDF
tfidf_values = []
for tf_doc in tf_values:
    tfidf_doc = []
    for tf, idf in zip(tf_doc, idf_values):
        tfidf = tf * idf
        tfidf_doc.append(tfidf)
    tfidf_values.append(tfidf_doc)

print(" ")
print(tfidf_values)

# Perankingan berdasarkan nilai TF-IDF
ranking = sorted(range(len(tfidf_values)), key=lambda i: sum(tfidf_values[i]), reverse=True)

# Tampilkan hasil perankingan
print(" ")
for rank in ranking:
    print("Rank {}: {}".format(rank+1, documents[rank]))
