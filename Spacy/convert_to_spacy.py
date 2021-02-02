import json
import pickle

# with open("data/file_1.json1" , "r") as f:
#     datafile = f.read().splitlines()
# with open("data/2nafare_label.json1" , "r") as f:
with open("data/irancook.json1" , "r") as f:
    datafile = f.read().splitlines()
# f = open("data/file.json1" , "r")
# data_temp = f.read().splitlines()
# f.close()
# datafile = datafile + data_temp
dataset = []
raw_text = []
counter = 0
final_data = []
for item in datafile:
    temp = json.loads(item)
    if len(temp["labels"]) != 0:
        text = temp["text"]
        #text = text.replace("\n", " ")
        labels = temp["labels"]
        entities = []
        for i in labels:
            entities.append(tuple(i))
        dic = {"entities": entities}

        dataset.append ( (text, dic) )
        counter+=1
    else:
        raw_text.append(temp["text"])
print(dataset[0])
print(dataset[1])
# dataset.pop(1)
with open("data/spacy_input_irancook.pickle", "wb") as f:
# with open("data/spacy_input_2nafare.pickle", "wb" ) as f:
    pickle.dump(dataset,f)
# with open("data/raw_text.pickle", "wb" ) as f:
#     pickle.dump(raw_text , f)
# print(type(dataset))
print(len(dataset))
# print(dataset)