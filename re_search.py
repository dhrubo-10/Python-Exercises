import re
count = 0

fhand = open("clown.txt")
for line in fhand:
	line = line.rstrip()
	if re.search("^the", line):
		count+=1
		print(line)
print(count)
