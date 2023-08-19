import pandas as pd

# Read data from CSV
df = pd.read_csv('D:\pythonProject4\\venv\Comments scotland239.csv')

# Convert timeline column to datetime if needed
df['timeline'] = pd.to_datetime(df['timestamp'])

# Sort DataFrame by timeline
df_sorted = df.sort_values('timeline')

# Reset the index if desired
df_sorted = df_sorted.reset_index(drop=True)

# Print the sorted DataFrame
df_sorted.to_csv('D:\pythonProject4\\venv\Comments scotland239.csv', index=False)
