#case folding - tokenisasi -stop list - stemming - term weigthing


#import library
import nltk 
nltk.download('punkt')
from nltk.tokenize import RegexpTokenizer
import re
token = RegexpTokenizer(r'\w+')
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.probability import FreqDist

text = '''Sebagian besar negara memiliki sistem pendidikan 
formal yang umumnya wajib. Dalam sistem ini, siswa mengalami kemajuan melalui 
serangkaian kegiatan belajar mengajar di sekolah. Nama-nama untuk sekolah ini 
bervariasi menurut negara, tetapi umumnya termasuk sekolah dasar untuk anak-anak 
dan dilanjutkan ke sekolah menengah untuk remaja yang telah menyelesaikan pendidikan dasar'''


def case_folding(teks):
    teks = re.sub(r'@[a-zA-Z0-9]+', '', teks)
    teks = re.sub(r',', '', teks)
    teks = re.sub(r'#', '', teks)
    teks = re.sub(r'!', '', teks)
    teks = re.sub(r'&', '', teks)
    teks = re.sub(r"b'", '', teks)
    teks = re.sub(r"\'", '', teks)
    teks = re.sub(r"_.*", '', teks)
    teks = re.sub(r"wk.*wk", '', teks)
    teks = re.sub('\[.*?\]', '', teks)
    teks = re.sub(r'\[a-zA-Z0-9+', '', teks)
    teks = re.sub(r'\w*\d+\w*', '', teks)
    teks = re.sub(r'\\.*\\', "", teks)
    teks = re.sub("https*\S+", " ", teks)
    teks = re.sub('\s{2,}', " ", teks)
    teks = teks.lower()
    return teks

cas_text =case_folding(text)
# tokenisasi = token.tokenize(cas_text)
# factory = StopWordRemoverFactory()
# stopword = factory.create_stop_word_remover()
# stp_word = stopword.remove(cas_text)
tokenisasi = token.tokenize(cas_text)

def stop_words(teks):
    factory = StopWordRemoverFactory()
    stopword = factory.create_stop_word_remover()
    stp_word = stopword.remove(teks)
    return stp_word

# stop_wr = stop_words (toke)
for i, teks in enumerate(tokenisasi):
    tokenisasi[i] = stop_words(teks)
stop_wr = list(filter(None, tokenisasi))


# print(tokenisasi)
def stemming_word(teks):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    stem_word = stemmer.stem(teks)
    return stem_word

for i, teks in enumerate(stop_wr):
    stop_wr[i]=stemming_word(teks)

# stem_wr = tokenisasi.apply(stemming_word)
#hasil stemming
# print(stop_wr)

kemunculan = nltk.FreqDist(stop_wr)
print(kemunculan.most_common())

#sekarang cari cara untuk input text -> kalo misal input kata ' sekolah' maka bakal muncul kata ini itu ada sebanyak 4 kali