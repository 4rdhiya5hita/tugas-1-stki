def my_import():
    # Example using nltk for data retrieval purpose
    import nltk
    # import numpy as np # numpy for NaN support

    # Stop word testing requirements
    nltk.download('stopwords')
    from nltk.corpus import stopwords # Import the stopwords module from the nltk.corpus package

    # Stemming testing requirements
    nltk.download('punkt')
    from nltk.stem import PorterStemmer
