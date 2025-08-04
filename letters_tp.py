import re

fname = input("File name: ")

if len(fname) < 1: fname = "mbox-short.txt"

fhand = open(fname)

di = dict()
total = 0
for line in fhand:
	words = re.sub('[^a-z]', '', line.lower())
	for char in words:
		di[char] = di.get(char, 0) + 1

total = sum(di.values())
for k,v in sorted(di.items(),key = lambda x: x[1], reverse= True):

	print(f"{k}, {((v/total)*100):.2f}%")

# print(sorted(di.items()))

# txtC = re.sub('[^a-z]', '', text.lower())
# print(txtC)