### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple= (41, 1.83, "Aaron", "Planas","Aaron" )
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError: tuple index out of range (fuera de rango)
#print(my_tuple[-6]) IndexError: tuple index out of range (fuera de rango)

print(my_tuple.count("Aaron"))
print(my_tuple.index("Planas"))
print(my_tuple.index("Aaron"))

#my_tuple[1] = 1.85 TypeError: 'tuple' object does not support item assignment

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Fantan"
my_tuple.insert(1, "Naranja")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(tuple(my_tuple))

#del my_tuple[2] ypeError: 'tuple' object doesn't support item deletion

del my_tuple
#print(my_tuple) NameError: name 'my_tuple' is not defined