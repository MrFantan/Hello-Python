### Loops ###

# While 

my_condition = 0

while my_condition < 10: 
    print(my_condition)
    my_condition += 2
else: # Es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)

print("Mi condición continúa")

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple= (41, 1.83, "Aaron", "Planas","Aaron" )

for element in my_tuple:
    print(element)

my_set = {"Aaron","Planas", 41}

for element in my_set:
    print(element)

my_dict = {"Nombre":"Aaron", "Apellido": "Planas", "Edad":41, 1:"Python"}

for element in my_dict:
    print(element)
    if element == "Edad":
        break # Corta de raiz lo siguiente y se para aqui.
else: 
    print("El bucle for para diccionario ha finalizado")
    
print("La ejecucion continúa")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue # Vuelve al for sin continuar lo de abajo.
else: 
    print("El bucle for para diccionario ha finalizado")