import pandas as pd
import nltk
from nltk.tokenize import word_tokenize

# Download NLTK tokenizer data
nltk.download('punkt')

# List of CSV file paths
csv_files = ['CSV1.csv', 'CSV2.csv', 'CSV3.csv', 'CSV4.csv']

# Function to find the column with the largest text using NLTK
def find_large_text_columns_nltk(df):
    text_lengths = {}
    # Iterate over each column
    for column in df.columns:
        if df[column].dtype == object:
             avg_length = df[column].apply(lambda x: len(word_tokenize(str(x))) if isinstance(x, str) else 0).mean()
             text_lengths[column] = avg_length
             
    return text_lengths

with open('all_large_texts.txt', 'w', encoding='utf-8') as output_file:
    # Iterate over each CSV file in the list
    for csv_file in csv_files:
        print(f"Processing file: {csv_file}")
        
        #Read the CSV file into a DataFrame
        df = pd.read_csv(csv_file)
           
             