filepath = r"C:\\school\cit95Python\files\words.txt"
fhand = open(filepath)

words = dict ()

for line in fhand:
    line = line.strip()
    wds = line.split()
    for w in wds:
        if w in words:
            words[w] = words[w] + 1

        else:
            words[w] = 1


print("Dictionary Length is: ", len(words),'\n', words)
print('"', max(words, key=words.get), '"', 'was used', max(words.values()), 'times')
