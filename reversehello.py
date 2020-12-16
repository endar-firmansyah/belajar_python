#input = ["Hello"," World"]

#x = input.split()


#print(input[6:11])
#print(input[0:5])


def flipWords(word):
	return " ".join(word.split()[::-1])

print(flipWords("Hello World!"))

