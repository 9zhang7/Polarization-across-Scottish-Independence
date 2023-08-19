import csv
from collections import Counter
from datetime import datetime
import matplotlib.pyplot as plt

date_format = "%Y-%m-%d %H:%M:%S"

with open('D:\pythonProject4\\venv\Comments scotland239.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    # Skip the header if necessary
    next(reader)

    dates = []
    for row in reader:
        if len(row) > 0:
            try:
                date = datetime.strptime(row[2], date_format).date()
                dates.append(date)
            except ValueError:
                print(f"Invalid date format: {row[2]}")
        else:
            print("Empty row encountered")

    date_counts = Counter(dates)

    sorted_results = sorted(date_counts.items(), key=lambda x: x[0])

    sorted_dates = [date.strftime("%Y-%m-%d") for date, count in sorted_results]
    sorted_counts = [count for date, count in sorted_results]

    # Create a bar chart
    plt.bar(sorted_dates, sorted_counts)
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.title('Date Count Chart')
    plt.xticks(rotation=45)

    plt.show()
