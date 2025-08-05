import re

fhand = open("mbox-short.txt")
ls = list()
for line in fhand:
	line = line.rstrip()
	words = re.findall('^Details: .*rev=([0-9]+)', line)
	if len(words) != 1: continue
	x = float(words[0])
	ls.append(x)
print(ls)