import json


with open("data/recipe.json", "rb") as f:
    data = json.load(f)
Food_list = []
for item in data:

    ID = item["ID"]
    foodTitle = item["foodTitle"]
    recipeInstructions = item["recipeInstructions"]
    temp_dic = {"ID": ID,
                "Title": foodTitle,
                "Text": recipeInstructions}
    Food_list.append(temp_dic)
with open("data/recipe_model_input.json", "w", encoding = "utf-8") as f:
    json.dump(Food_list, f, ensure_ascii = False, indent = 2)

# print(item["foodTitle"],item["ID"], item["recipeInstructions"])