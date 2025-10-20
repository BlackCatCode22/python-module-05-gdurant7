import os
import re

regrep = input('Enter an Expression: ')
fhand = open(r'C:\\school\cit95Python\files\mbox.txt')

count = 0

for line in fhand:
    line = line.rstrip()
    if re.search(regrep, line):
        count += 1

print('mbox.txt had ', count, ' lines that matched ', regrep )