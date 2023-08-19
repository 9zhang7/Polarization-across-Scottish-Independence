import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import numpy as np
import diptest

# Step 1: Load the CSV data
data = pd.read_csv('D:\pythonProject4\\venv\Comments merged.csv')

# Step 2: Preprocess the text data
# Add any additional preprocessing steps as per your requirements

# Step 3: Calculate sentiment scores using VADER for each corpus
analyzer = SentimentIntensityAnalyzer()

sentiment_scores = []

for corpus in data['cleaned_text']:
    if not pd.isnull(corpus):
        sentiment_score = analyzer.polarity_scores(str(corpus))['compound']
        sentiment_scores.append(sentiment_score)
    else:
        sentiment_scores.append(np.nan)

# Add sentiment scores to the DataFrame
data['sentiment_score'] = sentiment_scores

# Step 4: Convert 'timeline' column to datetime
data = data[data['timeline'] != 'timeline']  # Filter out rows with 'timeline' value
data['timeline'] = pd.to_datetime(data['timeline'], format='%Y-%m-%d %H:%M:%S')

# Step 5: Aggregate sentiment scores on a weekly basis
aggregated_data = data.set_index('timeline')['sentiment_score'].resample('M').mean().reset_index()

# Convert 'sentiment_score' column to a NumPy array
weekly_sentiments = aggregated_data['sentiment_score'].to_numpy()

# Apply Hartigan's Dip Test using diptest
dip_value, p_value = diptest.diptest(weekly_sentiments)

# Print the dip statistic and p-value
print("Dip Statistic:", dip_value)
print("P-value:", p_value)
