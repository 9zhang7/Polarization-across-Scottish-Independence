import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Load the CSV data
data = pd.read_csv('D:\pythonProject4\\venv\Comments merged.csv')

# Step 2: Preprocess the text data
# Add any additional preprocessing steps as per your requirements

# Step 3: Calculate sentiment scores using VADER for each corpus
analyzer = SentimentIntensityAnalyzer()

sentiment_scores = []
sentiment_categories = []


# Add sentiment scores and categories to the DataFrame
data['sentiment_score'] = sentiment_scores
data['sentiment_category'] = sentiment_categories

# Step 4: Convert 'timeline' column to datetime
data = data[data['timeline'] != 'timeline']  # Filter out rows with 'timeline' value
data['timeline'] = pd.to_datetime(data['timeline'], format='%Y-%m-%d %H:%M:%S')

# Step 5: Aggregate sentiment scores
aggregated_data = data.set_index('timeline')['sentiment_score'].resample('M').mean().reset_index()

# Convert 'timeline' and 'sentiment_score' columns to NumPy arrays
timestamps = aggregated_data['timeline'].to_numpy()
sentiments = aggregated_data['sentiment_score'].to_numpy()

# Step 6: Calculate proportion of sentiments
proportions = data.groupby(['timeline', 'sentiment_category']).size().unstack(fill_value=0)
proportions['Total'] = proportions.sum(axis=1)
proportions['Positive_Proportion'] = proportions['Positive'] / proportions['Total']
proportions['Negative_Proportion'] = proportions['Negative'] / proportions['Total']
proportions['Neutral_Proportion'] = proportions['Neutral'] / proportions['Total']


# Step 7: Visualize the proportions
plt.figure(figsize=(12, 6))
plt.bar(proportions.index, proportions['Positive_Proportion'], color='limegreen', label='Positive')
plt.bar(proportions.index, proportions['Negative_Proportion'], color='red', label='Negative')
plt.bar(proportions.index, proportions['Neutral_Proportion'], color='white')

plt.title('Sentiment Proportions Over Time')
plt.xlabel('Time')
plt.ylabel('Proportion')
plt.xticks(rotation=45)
plt.legend(loc='upper left')
plt.grid(True)
plt.show()