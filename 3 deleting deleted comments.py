import csv
import os

def delete_rows_with_character(csv_file, character):
    # Open the input and output files
    with open(csv_file, 'r', encoding='utf-8') as file_in, open('output.csv', 'w', newline='', encoding='utf-8') as file_out:
        reader = csv.reader(file_in)
        writer = csv.writer(file_out)

        # Iterate over each row in the input file
        for row in reader:
            # Check if the character exists in any cell of the row
            if any(character in cell for cell in row):
                continue  # Skip the row if the character is found
            writer.writerow(row)  # Write the row to the output file if the character is not found

    # Replace the input file with the output file
    os.replace('output.csv', csv_file)

# Usage example
delete_rows_with_character('D:\pythonProject4\\venv\Comments worldnews 7.csv', '[deleted]')
