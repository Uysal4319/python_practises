import matplotlib.pyplot as plt

dosya = open("text", encoding="utf8")
line = dosya.read()
dosya.close()
splitWords = line.split()
allWords = {}
for key in splitWords:
    if key not in allWords:
        allWords[key] = 1
    else:
        allWords[key] += 1
key = input('write the word:')
if key in allWords.keys():
    print("Word count: %s =>%s " % (key, allWords[key]))
else:
    print('Word could not founded!')

# creating the dataset
data = {'C': 20, 'C++': 15, 'Java': 30,
        'Python': 35}
courses = list(data.keys())
values = list(data.values())

# creating the bar plot
plt.bar(courses, values, color='maroon',
        width=0.4)

plt.savefig('test2.png')
