import spacy
from spacy.gold import GoldParse
from spacy.scorer import Scorer
import pickle

def evaluate(ner_model, examples):
    scorer = Scorer()
    for input_, annot in examples:
        annot = annot["entities"]
        doc_gold_text = ner_model.make_doc(input_)
        gold = GoldParse(doc_gold_text, entities=annot)
        pred_value = ner_model(input_)
        scorer.score(pred_value, gold)
    return scorer.scores

# example run

with open("data/TEST_DATA.pickle" , "rb") as f:
    examples = pickle.load(f)
# examples = [
#     ('Who is Shaka Khan?',
#      [(7, 17, 'PERSON')]),
#     ('I like London and Berlin.',
#      [(7, 13, 'LOC'), (18, 24, 'LOC')])
# ]

ner_model = spacy.load("Model_full_E50_D2") # for spaCy's pretrained use 'en_core_web_sm'
results = evaluate(ner_model, examples)
print(results)