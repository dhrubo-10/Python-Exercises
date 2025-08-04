file_name = input("File name: ")

try:
	fhand = open(file_name)
except:
	if len(file_name) < 1:
		fhand = open("mbox-short.txt")
	else:
		print("File not found!")
		exit()

count = dict()

for line in fhand:
	words = line.split()
	for word in words:
		count[word] = count.get(word, 0) + 1

max_count = None
wr = None

for w,c in count.items():
	if max_count is None or c > max_count:
		wr = w
		max_count = c

print(w, max_count)