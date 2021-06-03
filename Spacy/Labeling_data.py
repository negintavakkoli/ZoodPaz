import json
import spacy
import networkx as nx
from networkx.algorithms import bipartite

#loading model
ner_model = spacy.load("Model_full_E50_D2") # for spaCy's pretrained use 'en_core_web_sm'

#loading test data
with open("data/recipe_model_input.json", "r") as f:
    test_data = json.load(f)

#Definign Graph
G=nx.Graph()
ID_ing = {}
id_counter = 1
# Test your text
for item in test_data:
    Ing_test = item["Text"]
    # Ing_test.insert(0,item["Title"])
    Ing_test = " ".join(Ing_test)
    doc = ner_model ( Ing_test )
    # ents = [(e.text, e.label_) for e in doc.ents]
    ing_list = []
    title_list=[]
    #Filtering ingredients
    for e in doc.ents:
        if e.label_ == 'GRC':
            ing_list.append(e.text)
    ing_list = list(set(ing_list))
    # print(ing_list)

    #Filtering Titles
    doc = ner_model(item["Title"])
    for e in doc.ents:
        if e.label_ == "TIT":
            title_list.append(e.text)

    if len(title_list) == 0:
        title_list.append(item["Title"])
    # print(title_list)
    #Adding titles to graph as a node
    G.add_node(item["ID"], bipartite = 0 )
    nx.set_node_attributes(G,{item["ID"]:title_list[0]}, "name")

    #Adding ingredients to graph as nodes
    for ing in ing_list:
        try:
            #Checking the existence of ingredients
            id_temp = ID_ing[ing]
        except KeyError:
            id_temp = "ING_"+str(id_counter)
            ID_ing[ing] = id_temp
            G.add_node(id_temp, bipartite=1)
            nx.set_node_attributes(G, {id_temp:ing}, "name")
            id_counter+=1

        #Connecting ingredients to foods by the edges of graph
        G.add_edge(item["ID"], id_temp)


    #Saving graph



    #Finding the neighbours of nodes



    #Saving ID_ing[ing]



    if(int(item["ID"])>10):
        break


#Adding ingrediant nodes and title to graph
print(G.nodes())
print(G.edges())
print(G.nodes["ING_2"]["name"])
