import os
import re

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

count = 0
total = 0.0

for line in file:
    line = line.rstrip()
    num = re.findall(r"^New Revision:(\s*[0-9]*)",line)
    if len(num) > 0:
        for number in num:
            total += float(number[0])
            count += 1

average = total/count
print('The average is: ', total, average)