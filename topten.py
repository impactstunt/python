inFile = input('Enter filename: ')
try:
    file = open(inFile, 'r')
except:
    print('Invalid file {}'.format(inFile))
    exit()
# create a list and insert in the dict with counts.
counts = {}
for words in file:
    words = words.split()
    for word in words:
        word.lower()
        counts[word] = counts.get(word, 0) + 1

#Append dict items into the list in reverse order (value, key)
lst = []
for key,val in counts.items():
    wordslist = (val, key)
    lst.append(wordslist)

#sorted in reverse to get top used words
lst.sort(reverse=True)

#print top ten words (value, key) order.
for key, val in lst[0:10]:
    print(val, key)




