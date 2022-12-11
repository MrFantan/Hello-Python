### Clases ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname} ({alias})" # Propiedad Pública
        self.__name = name # Propiedad privada ( con __ se vuelve privada)
        
    def get_name (self):
        return self.__name  

    def walk (self):
        print(f"{self.full_name} Está caminando")

my_person = Person("Aaron", "Planas",)
print(my_person.full_name)
my_person.walk()

my_other_person = Person("Aaron", "Planas", "Fantan")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Héctor de Leon El loco de los perros"
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)
