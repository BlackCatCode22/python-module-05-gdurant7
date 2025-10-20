import os


fname = input('Enter file name: ')
file = list()

try:
    for dirpath, dirnames, filenames in os.walk('C:\\'):  # find file
        for filename in filenames:
            if filename.startswith(fname):
                file.append(os.path.join(dirpath, filename))  # add file path to fille list
                print(dirpath, filename)
except FileNotFoundError:
    print('File not found')
    exit()

letterCount = dict()
for line in file:
    words = line.rstrip().split()
    for word in words:
        word = word.lower()
        for letter in word:
            if not 'a' <= letter <= 'z':
                continue
            letterCount[letter] = letterCount.get(letter, 0) + 1

temp_list = sorted([(v, k) for (k, v) in letterCount.items()], reverse=True)
for (v, k) in temp_list:
    print(k, v)