import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file
data = pd.read_csv('Comments merged with Topics.csv')

# Convert 'Topic' column to string type
data['Topic'] = data['Topic'].astype(str)

# Group the data and calculate proportions of emotions for each group
group_emotions = {}

# Iterate over unique groups
for group in data['Topic'].unique():
    group_data = data[data['Topic'].str.strip() == group.strip()]
    total_count = len(group_data)

    # Calculate the proportions of each emotion
    emotion_counts = group_data['sentiment_category'].value_counts()
    proportions = emotion_counts / total_count

    # Store the proportions for the group
    group_emotions[group] = proportions

# Extract group names and emotion proportions
groups = list(group_emotions.keys())
emotions = list(group_emotions[groups[0]].index)

# Extract the numeric values from the group names
numeric_values = [int(group.split()[-1]) for group in groups]

# Sort groups based on the numeric values in descending order
sorted_groups = [group for _, group in sorted(zip(numeric_values, groups), reverse=False)]

# Plotting
fig, ax = plt.subplots()

# Set colors for different emotions
colors = ['green', 'red', 'blue']

# Set width of each bar
bar_width = 0.2

# Calculate the position of each group on the x-axis
x = np.arange(len(groups))

# Iterate over emotions and plot bars for each emotion
for i, emotion in enumerate(emotions):
    proportions = [group_emotions[group].loc[emotion] for group in sorted_groups]
    ax.bar(x + i * bar_width, proportions, color=colors[i], width=bar_width, label=emotion)

# Set x-axis tick labels and positions
ax.set_xticks(x + (len(emotions) - 1) * bar_width / 2)
ax.set_xticklabels(sorted_groups)

# Set labels and title
ax.set_xlabel('Topic')
ax.set_ylabel('Sentiment Proportion')
ax.set_title('Sentiment Proportion across Topics')

# Set legend
ax.legend()

# Show the plot
plt.show()
