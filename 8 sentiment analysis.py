import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('D:\pythonProject4\\venv\Comments unitedkingdom_with_group.csv')
grouped = df.groupby('group')
sia = SentimentIntensityAnalyzer()
sentiment_scores = []
for group_number, group_data in grouped:
    combined_text = ' '.join(group_data['cleaned_text'].astype(str))
    group_sentiment = sia.polarity_scores(combined_text)
    group_sentiment['group_number'] = group_number
    sentiment_scores.append(group_sentiment)

    # Print the sentiment result for each group
    print(f"Group Number: {group_number}")
    print(f"Sentiment Scores: {group_sentiment}")
    print("----------------------------------------")

# Extract the sentiment scores for plotting
group_numbers = [score['group_number'] for score in sentiment_scores]
positive_scores = [score['pos'] for score in sentiment_scores]
negative_scores = [score['neg'] for score in sentiment_scores]
neutral_scores = [score['neu'] for score in sentiment_scores]

# Specify the desired group order
desired_order = ["Group 1", "Group 2", "Group 3", "Group 4", "Group 5", "Group 6", "Group 7", "Group 8",
                 "Group 9", "Group 10", "Group 11", "Group 12"]

# Check if a group is missing data and assign 0 values to the sentiment scores
for group in desired_order:
    if group not in group_numbers:
        group_numbers.append(group)
        positive_scores.append(0)
        negative_scores.append(0)
        neutral_scores.append(0)

# Reorder the sentiment scores based on the desired group order
reordered_positive_scores = [positive_scores[group_numbers.index(group)] for group in desired_order]
reordered_negative_scores = [negative_scores[group_numbers.index(group)] for group in desired_order]
reordered_neutral_scores = [neutral_scores[group_numbers.index(group)] for group in desired_order]

# Set the width of the bars
bar_width = 0.95

# Set the positions of the bars on the x-axis with a small offset
r = np.arange(len(desired_order)) - bar_width/2

# Set up the figure and axes
fig, ax = plt.subplots()

# Plot the sentiment scores as grouped bars
ax.bar(r, reordered_positive_scores, width=bar_width, label='Positive')
ax.bar(r, reordered_negative_scores, width=bar_width, label='Negative', bottom=reordered_positive_scores)
ax.bar(r, reordered_neutral_scores, width=bar_width, label='Neutral', bottom=np.add(reordered_positive_scores, reordered_negative_scores))

# Set labels and title for the bar chart
ax.set_xlabel('Group Number')
ax.set_ylabel('Sentiment Score')
ax.set_title('Sentiment Scores by Group')

# Set the x-axis tick labels
ax.set_xticks(range(len(desired_order)))
ax.set_xticklabels(desired_order, rotation=45, ha='right')

# Increase the scale of the vertical axis to amplify data changes
ax.set_ylim([0, 1])  # Adjust the range as needed

# Add a legend for the bar chart
ax.legend()

# Show the plot
plt.show()
