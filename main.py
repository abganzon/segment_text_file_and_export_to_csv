# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import re
import openai
import csv
from textblob import TextBlob
import re

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Load text from file
    with open("C:/Users/Ferret9 PC/Documents/Pinebrooke_Declarations_Reformatted_Segmented_OpenAI.txt", "r", encoding='utf-8') as file:
        text = file.read()

    # Split text into segments
    data = []
    current_title = ""
    current_heading = ""
    current_content = ""

    max_line_length = max(len(line) for line in text.split("\n"))
    strip_length = max(0, max_line_length - 9)  # Adjust strip length to account for longest heading or content label
    for line in text.strip().split("\n"):
        if line.startswith("Title:"):
            current_title = line[7:].strip()
        elif line.startswith("Heading:"):
            current_heading = line[9:].strip()[:strip_length]
        elif line.startswith("Content:"):
            current_content = line[9:].strip()[:strip_length]
            token = str(len(current_content))
            data.append([current_title, current_heading, current_content, token])

    # Write data to CSV file
    output_file_path = "pinebrooke-output-final.csv"
    with open(output_file_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["title", "heading", "content", "token"])
        writer.writerows(data)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
