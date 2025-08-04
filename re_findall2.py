import re

fhand = open("mbox-short.txt")
ls = list()
for line in fhand:
	line = line.rstrip()
	words = re.findall('^From .* ([0-9]{2}):([0-9]{2}):([0-9]{2})', line)
	if len(words) != 1: continue
	x = words[0]
	ls.append(x)
print(ls)