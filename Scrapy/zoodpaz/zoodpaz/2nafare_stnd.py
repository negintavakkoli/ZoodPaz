import json
import glob

# path_to_file = "spiders/Sample recipe/*.text"
path_to_file = "spiders/Sample-recipe-irancook/*.txt"
g = glob.glob(path_to_file)
# f = open("doccano_input_files/2nafare.json", "w")
f = open("doccano_input_files/irancook.json" , "w")
for index, item in enumerate(g):
    with open(item , "r") as ff:
        text = ff.read()
    food_dic = {
        "id" : index,
        "text" : text
    }
    print(food_dic)


    json.dump(food_dic,f)
    f.write("\n")
f.close()

