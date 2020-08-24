import json


def find_str(s, char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index

            index += 1

    return -1
#
# print(find_str("Happy birthday", "day"))
# print(find_str("Happy birthday", "rth"))
# print(find_str("Happy birthday", "rh"))


with open("recipe.json", "r") as f:
    recipe_ins = json.load(f)

# with open("recipe.json", "r") as f:
#     ingredient = json.load(f)
i = 0
for item in recipe_ins:
    instruction_rec = item["recipeInstructions"]
    ingredient_item = item["recipeIngredient"]
    if ingredient_item == None:
        continue
    for material in ingredient_item:
        if material in instruction_rec:
            print("find sth")
            offset_start = find_str(instruction_rec,material)
            # offset_start = find_str(instruction_rec,ingredient[i])
        else:
            print ( "nothing" )
            continue


        print(offset_start)

