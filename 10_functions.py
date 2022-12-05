### Functions ###

def my_function (): # Forma de definir una Función.
    print("Esto es una función")

my_function ()
my_function ()
my_function ()

def sum_two_values(first_value, second_value):
    print(first_value + second_value)

sum_two_values(5 , 7) # Añadir valores para que el def realice el resultado.
sum_two_values(54754 , 71231)
sum_two_values("5", "7") # Es como texto y lo concatena.
sum_two_values(1.4, 5.2)

def sum_two_values_with_return (first_value, second_value):
    my_sum = first_value + second_value 
    return my_sum 

my_result = sum_two_values(1.4, 5.2)
print(my_result) # None

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname = "Planas", name = "Aaron")

def print_name_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default ("Aaron", "Planas")
print_name_with_default ("Aaron", "Planas", "Fantan")

def print_upper_texts(*texts):
    for text in texts:
        print(text.upper()) # Para imprimir el texto en mayúsculas

print_upper_texts("Hola", "Python", "Fantan")
print_upper_texts("Hola")

