### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #Incialmente es un diccionario

my_other_set = {"Aaron","Planas", 41}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Fantan")

print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add("Fantan") # Un set no adminte repetidos

print(my_other_set)

print("Aaron" in my_other_set) # Existe en my_other_set ( true )
print("Aaro" in my_other_set) # Existe en my_other_set ( false )

my_other_set.remove("Aaron") 
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set 
#print(my_other_set) # NameError: name 'my_other_set' is not defined ( Borra completo el my_other_set )

my_set = {"Aaron","Planas", 41}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin","Swift", "Pyhton"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))

print(my_new_set.difference(my_set))




