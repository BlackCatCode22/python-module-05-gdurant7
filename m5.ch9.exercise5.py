# python schoolcount.py  # cant find any information about this program
import os

schoolCount = dict()
email = dict()
file = list()

fname = input('Enter file name: ')

try:
    for dirpath, dirnames, filenames in os.walk('C:\\'):  # find file
        for filename in filenames:
            if filename.startswith(fname):
                file.append(os.path.join(dirpath, filename))  # add file path to fille list
                print(dirpath, filename)
except FileNotFoundError:
    print('File not found')
    exit()

fhand = open(file[0])
for line in fhand:
    words = line.rstrip().split()
    if len(words) == 0 or words[0] != 'From':
        continue
    if words[1] not in email:
        email[words[1]] = 1
        for words in email:
            domain = words.split('@')[1]
            if domain not in schoolCount:
                schoolCount[domain] = 1
            else:
                schoolCount[domain] += 1
    else:
        email[words[1]] += 1

print(schoolCount)