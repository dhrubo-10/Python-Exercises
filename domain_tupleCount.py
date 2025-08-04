fname = input("File name: ")

if len(fname) < 1: fname = "mbox-short.txt"

fhand = open(fname)

di = dict()

for line in fhand:
	if line.startswith("From: "):
		words = line.split()
		count = words[1]
		di[count] = di.get(count, 0) + 1


tmp = list()
for k,v in di.items():
	newt = v,k
	tmp.append(newt)
	tmp = sorted(tmp, reverse=True)
	highest = tmp[0]

print(highest[1], highest[0])