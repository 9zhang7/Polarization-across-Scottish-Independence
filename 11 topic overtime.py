import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file
data = pd.read_csv('Comments filename with Topics.csv')

# Parse the datetime column
data['timeline'] = pd.to_datetime(data['timeline'], format='%Y-%m-%d %H:%M:%S', errors='coerce')

# Remove rows with NaT values
data = data.dropna(subset=['timeline'])

# Set the datetime column as the index
data.set_index('timeline', inplace=True)

# Convert the 'topic' column to float
data['Topic'] = data['Topic'].astype(float)

# Resample the data to a desired time frequency (e.g., daily, hourly)
resampled_data = data.resample('D').count()

# Convert index to numpy array
dates = np.array(resampled_data.index)

# Get unique topics
unique_topics = data['Topic'].dropna().unique()

# Create a colormap for topics
colormap = plt.cm.get_cmap('tab10', len(unique_topics))

# Plot the distribution over time
for i, topic in enumerate(unique_topics):
    topic_data = resampled_data[resampled_data['Topic'] == topic]
    if len(topic_data) > 0:
        plt.scatter(topic_data.index, topic_data['Topic'], color=colormap(i))

plt.xlabel('Date')
plt.ylabel('Topic number')
plt.title('Distribution over Time')
plt.xticks(rotation=45)
plt.legend()
plt.show()
