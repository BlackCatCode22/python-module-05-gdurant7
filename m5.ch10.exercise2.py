# python schoolcount.py  # cant find any information about this program
import os

time = dict()
hourCount = dict()
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
    if words[5] not in time:
        time[words[5]] = 1
        for words in time:
            hour = words.split(':')[0]
            if hour not in hourCount:
                hourCount[hour] = 1
            else:
                hourCount[hour] += 1
    else:
        time[words[5]] += 1

keySort = list(hourCount.keys())
keySort.sort()

sortedTime = {i: hourCount[i] for i in keySort}

for (key, value) in sortedTime.items():
    print('{key}: {value}'.format(key=key, value=value))