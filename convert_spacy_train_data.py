import json
import codecs

filename = input("Enter your train data filename : ")
print(filename)


with open(filename, encoding="utf-8") as f:
    train = json.load(f)

TRAIN_DATA = []
for data in train:
	ents = [tuple(entity) for entity in data['entities']]
	TRAIN_DATA.append((data['content'],{'entities':ents}))


with codecs.open('{}'.format(filename.replace('json','log')),'w', "utf-8") as write:
	write.write(str(TRAIN_DATA))

print('-------------Copy and Paste to spacy training-------------')
print()
print()
print()
print(TRAIN_DATA)
print()
print()
print()
print('--------------------------End-----------------------------')