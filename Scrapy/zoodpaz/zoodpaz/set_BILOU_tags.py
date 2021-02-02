import json
import re
import numpy as np


with open("recipe.json", "r") as f:
    recipes = json.load(f)


i,j = 0,0
food_list = []
label_material = "GRC"
label_title = "TIT"
ff = open("doccano_input.json","w")

#recognize instruction
for item in recipes:
    food_title = item["foodTitle"]
    instruction_rec = item["recipeInstructions"]
    instruction_rec = " ".join(instruction_rec)
    instruction_rec = food_title+"\n"+instruction_rec
    binary_recipe = [0] * len ( instruction_rec )

    food_id = item["ID"]
    food_dic = {
        "id" : food_id,
        "text": instruction_rec,
    }
    labels = []
    ingredient_item = item["recipeIngredientName"]
    ingredient_item = list ( set ( ingredient_item ) )
    ingredient_item = list ( sorted ( ingredient_item , key = len ) )

    # for material in ingredient_item:
    #     if material in instruction_rec:
    #         try:
    #             # index_matrial = instruction_rec.index(material)
    #
    #             start_point = [m.start () for m in re.finditer ( material , instruction_rec)]
    #             len_material= len(material)
    #             for point in start_point:
    #                 end_point = point+len_material
    #                 temp_binary = [0]*len(instruction_rec)
    #                 temp_binary[point:end_point] = [1]*(end_point-point)
    #                 if (1 in (np.array(temp_binary) & np.array(binary_recipe))):
    #                     pass
    #                     # print ( ingredient_item )
    #                     # print ( material )
    #                 else:
    #                     labels.append ( [point , end_point , label_material] )
    #                     binary_recipe[point:end_point] = [1] * (end_point - point)
    #         except:
    #             print("error")
    #             pass
    #
    #         # offset_start = find_str(instruction_rec,material)
    #         # offset_start = find_str(instruction_rec,ingredient[i])
    #     else:
    #         j+=1
    #         continue
    # food_dic["labels"] = labels
    food_list.append(food_dic)
    json.dump(food_dic,ff)
    ff.write("\n")
ff.close()


with open("food_dataset.json", "w", encoding = "utf-8") as f:
    json.dump(food_list,f, ensure_ascii = False ,indent = 2)

print("There are {} valid and {} invalid cases.".format(i,j))

