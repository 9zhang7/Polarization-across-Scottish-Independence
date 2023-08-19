import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import matplotlib.pyplot as plt

# Step 1: Load and preprocess the data
data = pd.read_csv('Comments merged.csv')
stop_words = set(stopwords.words('english'))

# Add additional stop words
additional_stop_words = ['would', 'could', 'one', 'people', 'scotland',
                         'scottish', 'lol', 'oh', 'im', 'youre', 'question',
                         'answer', 'please', 'get', 'dont', 'want', 'think']
stop_words.update(additional_stop_words)

lemmatizer = WordNetLemmatizer()

preprocessed_docs = []

for document in data['cleaned_text']:  # Replace 'text_column' with the column name containing your text
    if isinstance(document, str):  # Check if document is a string
        # Tokenize the document
        tokens = word_tokenize(document.lower())

        # Remove stopwords and perform lemmatization
        preprocessed_tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalpha() and token not in stop_words]

        # Join the preprocessed tokens back into a single string
        preprocessed_doc = ' '.join(preprocessed_tokens)

        preprocessed_docs.append(preprocessed_doc)

# Step 2: Create a bag-of-words representation
vectorizer = CountVectorizer()
bow_representation = vectorizer.fit_transform(preprocessed_docs)

# Step 3: Apply LDA
num_topics = 12  # Set the desired number of topics
lda_model = LatentDirichletAllocation(n_components=num_topics, random_state=42)
lda_model.fit(bow_representation)

# Step 4: Access the inferred topic distributions
document_topic_distributions = lda_model.transform(bow_representation)

# Step 5: Interpret the results
# Print the top words for each topic
feature_names = vectorizer.get_feature_names()
for topic_idx, topic in enumerate(lda_model.components_):
    top_words = [feature_names[i] for i in topic.argsort()[:-10 - 1:-1]]
    print(f"Topic {topic_idx + 1}: {' '.join(top_words)}")

# Visualize the distribution of topics across documents
topic_counts = document_topic_distributions.argmax(axis=1)
topic_counts = pd.Series(topic_counts, name='Topic').value_counts().sort_index()

plt.figure(figsize=(10, 6))
plt.bar(topic_counts.index, topic_counts.values)
plt.xlabel('Topic')
plt.ylabel('Number of Documents')
plt.title('Distribution of Topics')
plt.show()
