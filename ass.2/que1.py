# import scipy
# import scispacy

import spacy

# Load the small biomedical model
nlp = spacy.load("en_core_sci_sm")

# Process some text
doc = nlp("The patient was diagnosed with diabetes and was prescribed metformin.")
for entity in doc.ents:
    print(entity.text, entity.label_)
