### Lists ###

my_list = list()
my_other_list = [ ]

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [41, 1.83, "Aaron", "Planas"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(30))
#print(my_other_list[4]) IndexError: list index out of range
#print(my_other_list[-5]) IndexError: list index out of range

age, height, name, surname = my_other_list
print(name) 

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

print(my_list + my_other_list)
#print(my_list * my_other_list) TypeError: 'my_list' is an invalid keyword argument for print()

my_other_list.append("Fantan")
print(my_other_list)

my_other_list.insert(1, "Rojo")
print(my_other_list)

my_other_list[1] = "Naranja"
print(my_other_list)

my_other_list.remove("Naranja")
print(my_other_list)    

my_list.remove(30)
print(my_list)    

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:2])

my_list = "Hola Python"
print(my_list)
print(type(my_list))

