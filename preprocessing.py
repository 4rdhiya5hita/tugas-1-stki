import string
# Example using nltk for data retrieval purpose
import nltk
nltk.download('omw-1.4')
nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer, PorterStemmer

def wnl(tokenizing_sentence):
    wnl = WordNetLemmatizer()
    new_sentence = []
    i = 0
    while(i<len(tokenizing_sentence)):
        lemmatized_word = wnl.lemmatize(str(tokenizing_sentence[i]))
        new_sentence.append(lemmatized_word)
        i+=1
    return new_sentence


def porter(tokenizing_sentence):
    porter = PorterStemmer()
    new_sentence = []
    i = 0
    while(i<len(tokenizing_sentence)):
        stemmed_words = porter.stem(str(tokenizing_sentence[i]))
        new_sentence.append(stemmed_words)
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

    # tokens_without_punct
    without_punctuation = [token for token in new_sentence if token not in string.punctuation]
    final_sentence = ' '.join(without_punctuation)
    # print(tokens_without_punct)

    # print(final_sentence)
    # , 'porter_sentence': porter_sentence, 'wnl_sentence': wnl_sentence
    # return {'final_sentence': final_sentence, "input_text": input_text}
    return without_punctuation