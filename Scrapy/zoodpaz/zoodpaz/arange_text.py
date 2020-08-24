import json
import pickle

with open("recipe.json", "r") as f:
    f = json.load(f)
counter = 0
recipeInstructions_list = []
for item in f:
    recipeInstructions = item["recipeInstructions"]
    #
    if len(recipeInstructions)>0:
        counter +=1
        recipeInstructions = str ( recipeInstructions )
        recipeInstructions = recipeInstructions.replace ( " " , "\n" )
        recipeInstructions_list.append(recipeInstructions)
        print(recipeInstructions)


with open("recipeInstructions.text", "w") as f:
    json.dump(recipeInstructions_list,f)



print(counter)