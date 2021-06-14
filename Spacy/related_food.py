import networkx as nx
import pickle
from collections import Counter

#Load ID_ing pickle file
with open("ID_ing.pickle", "rb") as f:
    ID_ing = pickle.load(f)

#Load database
G = nx.read_gml("database.gml")


#Get the ingerdiant from user

ing_list = []
# Getting text from UI


#Test Sample text



#defin function input list of ingrdiant and the output list of correlated ingerdiant
def related_food (ing_list):
    list_of_foods = []
    #Finding the ID of ingrediant
    for item in ing_list:
        id_temp = ID_ing[item]
        #Finding related Food: Finding neighbors nodes
        foods = [n for n in G.neighbors( id_temp )]
        list_of_foods.append(foods)

    #Finding related food based on all ingredients
    common_foods = set(list_of_foods[0]).intersection(*list_of_foods)
    common_foods = list(common_foods)
    print(common_foods)

    #Finding related ingredient
    list_of_ing = []
    for food in common_foods:
        ing_negbr = [n for n in G.neighbors ( food )]
        list_of_ing = list_of_ing + ing_negbr

    list_of_ing = Counter ( list_of_ing )
    suggested_ing = list_of_ing.most_common ( 20 )
    print(suggested_ing)

    return 0


ing_list = ["برنج"]
related_food(ing_list)


