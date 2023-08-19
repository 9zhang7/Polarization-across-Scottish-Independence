import datetime
import csv

# Open the input CSV file for reading with the correct encoding
with open('D:\pythonProject4\\venv\Comments scotland239.csv', 'r', encoding='utf-8') as file:
    # Create a CSV reader object
    reader = csv.reader(file)
    # Skip the header row
    header = next(reader)
    # Read the remaining CSV data into a list of rows
    rows = list(reader)

# Iterate over the rows and convert epoch seconds to formatted time
for row in rows:
    epoch_seconds = int(float(row[2]))  # Assuming the epoch seconds are in the first column
    timestamp = datetime.datetime.fromtimestamp(epoch_seconds)
    formatted_time = timestamp.strftime('%Y-%m-%d %H:%M:%S')
    row[2] = formatted_time

# Open the same CSV file for writing with the correct encoding
with open('D:\pythonProject4\\venv\Comments scotland239.csv', 'w', newline='', encoding='utf-8') as file:
    # Create a CSV writer object
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(header)
    # Write the modified rows back to the CSV file
    writer.writerows(rows)


