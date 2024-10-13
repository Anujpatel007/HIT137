import warnings
from transformers import AutoTokenizer
from collections import Counter

def count_top_tokens_chunked(text_file_path, tokenizer_name='bert-base-uncased', top_n=30, chunk_size=1024):
    """
    Counts the unique tokens in a text file by reading in chunks and returns the top N tokens with their counts.
    
    Parameters:
    - text_file_path (str): Path to the text file (in this case 'large_texts_final.txt').
    - tokenizer_name (str): Name of the tokenizer model (default is 'bert-base-uncased').
    - top_n (int): Number of top tokens to display (default is 30).
    - chunk_size (int): Number of characters to read at a time (default is 1024).
    
    Returns:
    - List of tuples with top tokens and their counts.
    """
    
    # Suppress the specific FutureWarning and UserWarning
    warnings.filterwarnings('ignore', category=FutureWarning)
    warnings.filterwarnings('ignore', category=UserWarning)
    
    # Step 1: Load the tokenizer using AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
    
    token_counts = Counter()
    
    # Step 2: Read the text file in chunks
    with open('large_texts_final.txt', 'r', encoding='utf-8') as file:
        while True:
            text_chunk = file.read(chunk_size)
            if not text_chunk:
                break
            
            # Step 3: Tokenize the chunk
            tokens = tokenizer.tokenize(text_chunk)
            
            # Step 4: Update the token counts
            token_counts.update(tokens)
    
    # Step 5: Get the top N most common tokens
    top_tokens = token_counts.most_common(top_n)
    
    # Step 6: Return the top tokens
    return top_tokens

# Example usage (ensure the file 'large_texts_final.txt' exists in the same directory):
top_tokens = count_top_tokens_chunked('large_texts_final.txt')
for token, count in top_tokens:
    print(f"Token: {token}, Count: {count}")