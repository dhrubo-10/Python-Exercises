import re

hand = open("mbox-short.txt")
count = 0
# ct = 0
# for line in hand:
# 	line = line.strip()
# 	if line.find('From: ') != -1:
# 		ct+=1
# print(ct)

for line in hand:
	line = line.rstrip()
	if re.search('^From:',line):
		count+=1
print(count)