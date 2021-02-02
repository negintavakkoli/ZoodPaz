import json

with open("doccano_input.json", "r") as f:
    food_list = f.read()



food_list = food_list.split("\n")

chunks = [food_list[x:x + 150] for x in range( 0 , len( food_list ) , 150 )]
print( len(chunks) , len( food_list ) )
print(len(chunks[-1]))
counter =1

for index, item in enumerate(chunks):
    with open("doccano_input_files/doccano_input_"+str(index)+".json" , "w") as f:
        f.write("\n".join(item))
