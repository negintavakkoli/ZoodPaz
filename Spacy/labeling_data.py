import spacy
import random
import pickle

nlp = spacy.load("food_dataset")
with open("data/raw_text.pickle", "rb") as f:
    raw_text = pickle.load(f)

text = random.choice(raw_text)
doc = nlp ( text )
for ent in doc.ents:
    print ( ent.text , ent.start_char , ent.end_char , ent.label_ )

print(text)