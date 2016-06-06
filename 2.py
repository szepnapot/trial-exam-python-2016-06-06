# Create a function that takes a filename as string parameter,
# and counts the occurances of the letter "a", and returns it as a number.
# It should not break if the file not exists just return 0

def a_letter_count(filename, letter):
	try:
		with open(filename) as f:
			read_data = f.read()
			return occurence_dict(read_data, letter)
	except FileNotFoundError:
		return 0

def occurence_dict(data, lookup):
	letter_occurence = {}
	for letters in data:
		letter_occurence[letters] = letter_occurence.get(letters, 0) + 1
	try:
		return letter_occurence[lookup]
	except KeyError:
		return "No {} found in the file.".format(lookup)

print(a_letter_count('testfile.txt', 'f'))