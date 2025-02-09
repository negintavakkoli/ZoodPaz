import spacy
import random
import pickle

with open("data/spacy_input.pickle" , "rb") as f:
    TRAIN_DATA = pickle.load(f)

def train_spacy(data , iterations):
    TRAIN_DATA = data
    nlp = spacy.blank ( 'fa' )  # create blank Language class
    # create the built-in pipeline components and add them to the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe ( 'ner' )
        nlp.add_pipe ( ner , last = True )

    # add labels
    for _ , annotations in TRAIN_DATA:
        for ent in annotations.get ( 'entities' ):
            ner.add_label ( ent[2] )



    # get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes ( *other_pipes ):  # only train NER
        optimizer = nlp.begin_training ()
        for itn in range ( iterations ):
            print ( "Statring iteration " + str ( itn ) )
            random.shuffle ( TRAIN_DATA )
            losses = {}
            for text , annotations in TRAIN_DATA:
                nlp.update (
                    [text] ,  # batch of texts
                    [annotations] ,  # batch of annotations
                    drop = 0.2 ,  # dropout - make it harder to memorise data
                    sgd = optimizer ,  # callable to update weights
                    losses = losses )
            print ( losses )
    return nlp

random.shuffle(TRAIN_DATA)
TEST_DATA = []
# for i in range(20):
#     TEST_DATA.append(TRAIN_DATA.pop(0))
# with open("data/TEST_DATA.pickle" , "wb") as f:
#     pickle.dump(TEST_DATA, f)
print(len(TRAIN_DATA),len(TEST_DATA))
print("**********************")
# print(TEST_DATA[0])
prdnlp = train_spacy ( TRAIN_DATA , 50 )

# Save our trained Model
# Model_number of test data_E
# modelfile = input ( "Enter your Model Name: " )
modelfile = "Model_full_E50_D2"
prdnlp.to_disk ( modelfile )

# Test your text
# test_text = input ( "Enter your testing text: " )
# doc = prdnlp ( test_text )
# for ent in doc.ents:
#     print ( ent.text , ent.start_char , ent.end_char , ent.label_ )

