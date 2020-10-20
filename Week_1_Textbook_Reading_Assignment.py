#list comprehension
a_list = ['mat', 'cad', 'peekaboo', 'whattaboutery', 'conclusion']

new_list = [x.upper() for x in a_list if len(x) > 3]
print(new_list)

#make a dictionary with key values of string lengths
a_dict = {len(name) : name for name in a_list}
print(a_dict)

#make a dictionary with key values of string indexes
another_dict = {index : value for index, value in enumerate(a_list)}
print(another_dict)
