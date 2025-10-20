import os

dayCount = dict()
file = list()

fname = input('Enter file name: ')

try:
    for dirpath, dirnames, filenames in os.walk('C:\\'):        #find file
        for filename in filenames:
            if filename.startswith(fname):
                file.append(os.path.join(dirpath, filename))    #add file path to fille list
                print(dirpath, filename)
except FileNotFoundError:
    print('File not found')
    exit()

fhand=open(file[0])
for line in fhand:
    words = line.rstrip().split()                           #strip text file
    if len(words) == 0 or words[0] != 'From':               #skip empty line, or lines with no dates
        continue
    if words[2] not in dayCount:                            #add new words to dayCount dictionary
        day = words[2]
        dayCount[day] = 1
    else:
        dayCount[words[2]] += 1                           #increase day count

print(dayCount)



