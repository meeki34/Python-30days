# We will be focus on data structure and algorithms in python
# just basic syntax of python is required and there type 

# list, tuple, set, dictionary
# list is mutable
# tuple is immutable
# set is mutable but it does not allow duplicate values
# dictionary is mutable and it allows key-value pairs

# list is defined by []

my_list = [1,2,3,4,5]
print(my_list)

# what can we do with the list?
# we can add, remove, update, access elements in the list
# add elements to the list

my_list.append(6)
print(my_list)
my_list.insert(0,0)
print(my_list)

my_list.extend([7,8,9])
print(my_list)
# remove elements from the list
my_list.remove(9)
print(my_list)
my_list.pop(0)
print(my_list)
my_list.pop()
print(my_list)
# update elements in the list
my_list[0] = 10
print(my_list)
# access elements in the list
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
print(my_list[4])
print(my_list[5])
# slicing in the list
print(my_list[0:3])
print(my_list[3:6])



