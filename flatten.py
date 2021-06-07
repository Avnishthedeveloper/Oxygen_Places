# 1. Write a program to flatten the nested list.
# Input:- [1, [2, 3, [4, 5, 6], [ 7, [ 8, 9, [10, 11], 12] ]]]
# Output:- [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Input1 = [1, [2, 3, [4, 5, 6], [ 7, [ 8, 9, [10, 11], 12] ]]]

flat = []

def flatten_data(data):
	# print(data)
	for i in data:
		if type(i) == list:
			flatten_data(i)
		else:
			flat.append(i)
	return flat

print(flatten_data(Input1))

