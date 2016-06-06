# Create a function that takes a list as a parameter,
# and returns a new list with all it's element value doubled.
# It should raise an error if the parameter is not a list

def doubler(lista):
	try:
		return [i*2 for i in lista]
	except TypeError:
		return "Input must be iterable! {} is not a valid parameter.".format(lista)


print(doubler([1,2,3,4,5]))
print(doubler(5))
