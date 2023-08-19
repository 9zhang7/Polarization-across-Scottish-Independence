import re
import string
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer


def clean_text(text):
    # Remove URLs
    text = re.sub(r'http\S+', '', text)

    # Remove special characters and punctuation
    text = re.sub(r'[^\w\s]', '', text)

    # Tokenization
    tokens = word_tokenize(text)

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token.lower() not in stop_words]

    # Lowercasing
    tokens = [token.lower() for token in tokens]

    # Stemming or Lemmatization
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

    # Join tokens back into a single string
    cleaned_text = ' '.join(lemmatized_tokens)

    return cleaned_text


# Read data from CSV
df = pd.read_csv('D:\pythonProject4\\venv\Comments scotland239.csv')

# Clean the text in a specific column
df['cleaned_text'] = df['comment'].apply(clean_text)

# Save cleaned data to a new CSV file
df.to_csv('D:\pythonProject4\\venv\Comments scotland239.csv', index=False)
