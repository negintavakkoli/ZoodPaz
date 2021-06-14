import json
import pickle
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
for index, item in enumerate(test_data):
    if index%50==0:
        print(index)
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
    id_food = "Food_"+str(item["ID"])
    G.add_node( id_food , bipartite = 0 )
    nx.set_node_attributes( G , {id_food:title_list[0]} , "name" )



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
        G.add_edge( id_food , id_temp )

#Last id_counter: 1980 --13 june 2021
print("ID:" ,id_counter)

#Last id_food: 1744 --13 june 2021
print(f"The last food id is {id_food}.")

#Saving graph as GML for database
nx.write_gml ( G , "database.gml" )

# Saving ID_ing[ing] as pickle
with open("ID_ing.pickle", "wb") as f:
    pickle.dump(ID_ing,f)

