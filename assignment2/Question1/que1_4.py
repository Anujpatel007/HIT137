import spacy
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

# Load the SpaCy models
spacy_model1 = spacy.load("en_core_sci_sm")  
spacy_model2 = spacy.load("en_ner_bc5cdr_md")  

# Load BioBERT model
bert_tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
bert_model = AutoModelForTokenClassification.from_pretrained("dmis-lab/biobert-base-cased-v1.1")
bert_ner = pipeline("ner", model=bert_model, tokenizer=bert_tokenizer, aggregation_strategy="simple")

# Function to extract entities using SpaCy
def extract_spacy_entities(text, spacy_model):
    doc = spacy_model(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Function to extract entities using BioBERT
def extract_bert_entities(text):
    entities = bert_ner(text)
    return entities

# Function to compare and analyze the entities
def compare_entities(entities1, entities2):
    entities1_set = set(entities1)
    entities2_set = set(entities2)
    
    common_entities = entities1_set & entities2_set
    unique_to_entities1 = entities1_set - entities2_set
    unique_to_entities2 = entities2_set - entities1_set
    
    print("=== Comparison of Entities ===")
    print(f"Total Entities (Entities 1): {len(entities1)}")
    print(f"Total Entities (Entities 2): {len(entities2)}")
    print(f"Common Entities: {len(common_entities)}")
    print(f"Unique to Entities 1: {len(unique_to_entities1)}")
    print(f"Unique to Entities 2: {len(unique_to_entities2)}\n")

# Read the .txt file
file_path = "path_to_your_file.txt"
with open(file_path, 'r') as file:
    text_data = file.read()

# Extract entities using SpaCy (SciSpaCy small and BC5CDR models)
entities_model1 = extract_spacy_entities(text_data, spacy_model1)
entities_model2 = extract_spacy_entities(text_data, spacy_model2)

# Extract entities using BioBERT
entities_bert = extract_bert_entities(text_data)

# Compare entities
compare_entities(entities_model1, entities_bert)
compare_entities(entities_model2, entities_bert)
