import json

sentence = ['Mary had a little lamb',
'His fleece was white as snow',
'And everywhere the child went',
'That little lamb was sure to go']
# word_sentence = sentence.split(" ")
with open('Mary.txt', 'w') as outfile:
    for line in sentence:
        outfile.write(line + '\n')

with open('Mary.txt', 'r') as infile:
    for line in infile:
        print(line.strip())


name_dict = {
    1:'Hill',
    2:'Bill',
    3:'Mill'
}

with open('name_dict.json', 'w') as outfile:
    json.dump(name_dict, outfile)

with open('name_dict.json', 'r') as infile:
    name_map = json.load(infile)
    print(name_map)