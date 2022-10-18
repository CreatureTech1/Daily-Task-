list=[100,200,488,342,768,654,845]
new_list=[list[(len(list)-i)]
            for i in range(1, len(list)+1)]
print(new_list)