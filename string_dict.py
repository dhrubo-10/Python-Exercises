import string

file_name = input("File name: ")

try:
	file = open(file_name)
except:
	print("File not found: ",file_name)
	exit()
dictionary = dict()

for line in file:
	words = line.rstrip()
	line = line.translate(line.maketrans('', '', string.punctuation))
	line = line.lower()
	words = line.split()
	for word in words:
		if word not in dictionary:
			dictionary[word] = 1

		else:
			dictionary[word] += 1
print(dictionary)