import json

dog_list = ['dalmation', 'german sheperd', 'labrador', 'chow chow']

with open('dogs.json', 'w') as outfile:
    json.dump(dog_list, outfile)

with open('dogs.json', 'r') as infile:
    restored_list = json.load(infile)
    print(restored_list)