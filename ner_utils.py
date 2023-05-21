import spacy
import pandas as pd

nlp = spacy.load("en_core_web_md")

def get_ner(i, doc):
    entities = []
    labels = []
    indices = []

    for ent in doc.ents:
        entities.append(ent.text)
        labels.append(ent.label_)
        indices.append(i)

    ner_df = pd.DataFrame({"Index": indices, "Entities": entities, 'Labels': labels})

    return ner_df

def process_item(i):
    return get_ner(i)
