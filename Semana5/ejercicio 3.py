# Crear un programa que intercambie el primer y ultimo elemento de una lista

my_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
deleted = my_list.pop(0)
deleted2 = my_list.pop(7)
my_list.insert(0, "9")
my_list.insert(9, "1")
print(my_list)
