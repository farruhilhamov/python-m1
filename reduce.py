from functools import reduce
items = [1,2,3,4,5]
sum_all = reduce(lambda x,y: x + y, items)

a = tuple(items)
b = ("hello")

print (b)