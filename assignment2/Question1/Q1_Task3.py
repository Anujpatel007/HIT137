import csv
from collections import Counter
import re

# Step 1: Read the text file
file_path = 'large_texts_final.txt'  # Replace with the actual path to your .txt file
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Step 2: Preprocess the text and count the occurrences of each word
# Converting text to lower case and using regex to find words
words = re.findall(r'\b\w+\b', text.lower())

# Step 3: Count word occurrences
word_counts = Counter(words)

# Step 4: Get the Top 30 most common words
top_30_words = word_counts.most_common(30)

# Step 5: Save the Top 30 words and their counts to a CSV file
output_file = 'top_30_common_words.csv'
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Word', 'Count'])  # Writing the header
    writer.writerows(top_30_words)  # Writing the top 30 words and counts

print(f'Top 30 words have been saved to {output_file}')