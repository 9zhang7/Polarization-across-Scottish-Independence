import csv
from datetime import datetime

# Specify the input and output filenames and structure of the CSV file
input_filename = r'D:\pythonProject4\venv\Comments worldnews 7.csv'  # Use raw string (r'') to avoid escape characters
output_filename = r'D:\pythonProject4\venv\Comments worldnews_with_group.csv'
date_column = 'timeline'  # Assuming the column containing the date is named 'date'

# Define the date range for each group (adjust the dates as needed)
group_dates = [
    ('2022-06-14', '2022-07-13'),
    ('2022-07-14', '2022-08-13'),
    ('2022-08-14', '2022-09-13'),
    ('2022-09-14', '2022-10-13'),
    ('2022-10-14', '2022-11-13'),
    ('2022-11-14', '2022-12-13'),
    ('2022-12-14', '2023-01-13'),
    ('2023-01-14', '2023-02-13'),
    ('2023-02-14', '2023-03-13'),
    ('2023-03-14', '2023-04-13'),
    ('2023-04-14', '2023-05-13'),
    ('2023-05-14', '2023-06-13')
]

# Load the data from the input CSV file
data = []
with open(input_filename, 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        data.append(row)

# Convert the date strings to datetime objects
for row in data:
    row[date_column] = datetime.strptime(row[date_column], "%Y-%m-%d %H:%M:%S")

# Create a dictionary to store the divided data
divided_data = {i: [] for i in range(1, 13)}  # 12 groups, numbered from 1 to 12

# Iterate over the data and assign each entry to the appropriate group
for row in data:
    row_date = row[date_column].date()  # Extract only the date from datetime object
    for group_number, (start_date, end_date) in enumerate(group_dates, 1):
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        if start_date <= row_date <= end_date:
            divided_data[group_number].append(row)

# Add group name to each row in the divided data
for group_number, rows in divided_data.items():
    group_name = f"Group {group_number}"
    for row in rows:
        row['group'] = group_name

# Write the updated data to the output CSV file
fieldnames = list(data[0].keys()) + ['group']  # Assuming all rows have the same keys
with open(output_filename, 'w', encoding='utf-8', newline='') as file:
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(data)

print("Output CSV file created successfully.")
