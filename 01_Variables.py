#varilabeles 
from operator import le


my_variable = "My variable"
print (my_variable)

variable_int = 5
print (variable_int)

variable_int_to_str_variable = str(variable_int)
print (variable_int_to_str_variable)
print (type(variable_int_to_str_variable))

variable_bool = False
print (variable_bool)
print ("este es el valor de :",variable_bool)


# variables en una sola linea 

name, surname, edad = "Abraham", "Torres", 21

print ("Me llamo:", name, surname, "My edad es:", edad    )

# concatenacion de variables en un print
print(my_variable, str (variable_int), variable_bool)

# funciones del sistema

print (len(my_variable))