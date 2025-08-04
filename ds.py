import re

fhand = open("mbox-short.txt")

lst = list()
for line in fhand:
	line = line.rstrip()
	words = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
	if len(words) != 1: continue
	num = float(words[0])
	lst.append(num)
m = max(lst)

print(m)